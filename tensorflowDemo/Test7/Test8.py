# coding:utf-8
import tensorflow as tf
import numpy as np
import string
import random

def create_type(s, prob=0.75):
    if random.uniform(0, 1) < prob:
        rand_ind = random.choice(range(len(s)))
        s_list = list(s)
        s_list[rand_ind] = random.choice(string.ascii_lowercase)
        s = ''.join(s_list)
    return (s)

def sparse_from_word_vec(word_vec):
    num_words = len(word_vec)
    indices = [[xi, 0, yi] for xi, x in enumerate(word_vec) for yi,y in enumerate(x)]
    chars = list(''.join(word_vec))
    return (tf.SparseTensorValue(indices, chars, [num_words, 1, 1]))


if __name__ == '__main__':
    n = 10
    street_names = ['abbey', 'baker', 'canal', 'donner', 'elm']
    street_types = ['rd', 'st', 'ln', 'pass', 'ave']
    rand_zips = [random.randint(65000, 65999) for i in range(5)]
    numbers = [random.randint(1, 9999) for i in range(n)]
    streets = [random.choice(street_names) for i in range(n)]
    street_suffs = [random.choice(street_types) for i in range(n)]
    zips = [random.choice(rand_zips) for i in range(n)]
    full_streets = [str(x) + ' ' + y + ' ' + z for x,y,z in zip(numbers, streets, street_suffs)]
    # print(full_streets)
    reference_data = [list(x) for x in zip(full_streets, zips)]
    # print(reference_data)
    typo_streets = [create_type(x) for x in streets]
    typo_full_streets = [str(x) + ' ' + y + ' ' + z for x, y, z in zip(numbers, typo_streets, street_suffs)]
    test_data = [list(x) for x in zip(typo_full_streets, zips)]

    sess = tf.Session()
    test_address = tf.sparse_placeholder(dtype=tf.string)
    test_zip = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    ref_address = tf.sparse_placeholder(dtype=tf.string)
    ref_zip = tf.placeholder(shape=[None, n], dtype=tf.float32)

    zip_dist = tf.square(tf.subtract(ref_zip, test_zip))
    address_dist = tf.edit_distance(test_address, ref_address, normalize=True)

    zip_max = tf.gather(tf.squeeze(zip_dist), tf.argmax(zip_dist, 1))
    zip_min = tf.gather(tf.squeeze(zip_dist), tf.argmin(zip_dist, 1))
    zip_sim = tf.div(tf.subtract(zip_max, zip_dist), tf.subtract(zip_max, zip_min))

    address_sim = tf.subtract(1., address_dist)

    address_weight = 0.5
    zip_weight = 1. - address_weight
    weighted_sim = tf.add(tf.transpose(tf.multiply(address_weight, address_sim)), tf.multiply(zip_weight, zip_sim))
    top_match_index = tf.argmax(weighted_sim, 1)

    reference_addresses = [x[0] for x in reference_data]
    reference_zips = np.array([[x[1] for x in reference_data]])
    sparse_ref_set = sparse_from_word_vec(reference_addresses)
    for i in range(n):
        test_address_entry = test_data[i][0]
        test_zip_entry = [[test_data[i][1]]]

        test_address_repeated = [test_address_entry] * n
        sparse_test_set = sparse_from_word_vec(test_address_repeated)

        feeddict = {
            test_address: sparse_test_set,
            test_zip: test_zip_entry,
            ref_address: sparse_ref_set,
            ref_zip: reference_zips
        }
        best_match = sess.run(top_match_index, feed_dict=feeddict)
        print(best_match)
        best_street = reference_addresses[best_match]
        [best_zip] = reference_zips[0][best_match]
        [[test_zip]] = test_zip_entry
        print('Address: ' + str(test_address_entry) + ' , ' + str(test_zip))
        print('Match: ' + str(best_street) + ' , ' + str(best_zip))






