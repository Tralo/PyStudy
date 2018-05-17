# coding:UTF-8

import pickle
import gzip
import numpy as np


def load_data(data_file):
    with gzip.open(data_file, 'rb') as f:
        train_set, valid_set, test_set = pickle.load(f)
    return train_set[0], train_set[1], test_set[0], test_set[1]


def cal_distance(x, y):
    return ((x - y) * (x - y).T)[0, 0]


def get_prediction(train_y, result):
    result_dict = {}
    for i in range(len(result)):
        if train_y[result[i]] not in result_dict:
            result_dict[train_y[result[i]]] = 1
        else:
            result_dict[train_y[result[i]]] += 1
    predict = sorted(result_dict.items(), key=lambda d: d[1])
    return predict[0][0]


def k_nn(train_data, train_y, test_data, k):
    # print test_data
    m = np.shape(test_data)[0]  # 需要计算的样本的个数
    m_train = np.shape(train_data)[0]
    predict = []

    for i in range(m):
        # 对每一个需要计算的样本计算其与所有的训练数据之间的距离
        distance_dict = {}
        for i_train in range(m_train):
            distance_dict[i_train] = cal_distance(train_data[i_train, :], test_data[i, :])
            # 对距离进行排序，得到最终的前k个作为最终的预测
        distance_result = sorted(distance_dict.items(), key=lambda d: d[1])
        # 取出前k个的结果作为最终的结果
        result = []
        count = 0
        for x in distance_result:
            if count >= k:
                break
            result.append(x[0])
            count += 1
            # 得到预测
        predict.append(get_prediction(train_y, result))
    return predict


def get_correct_rate(result, test_y):
    m = len(result)

    correct = 0.0
    for i in range(m):
        if result[i] == test_y[i]:
            correct += 1
    return correct / m


if __name__ == "__main__":
    # 1、导入
    print
    "---------- 1、load data ------------"
    train_x, train_y, test_x, test_y = load_data("mnist.pkl.gz")
    # 2、利用k_NN计算
    train_x = np.mat(train_x)
    test_x = np.mat(test_x)
    print
    "---------- 2、K-NN -------------"
    result = k_nn(train_x, train_y, test_x[:10, :], 10)
    print
    result
    # 3、预测正确性
    print
    "---------- 3、correct rate -------------"
    print
    get_correct_rate(result, test_y)