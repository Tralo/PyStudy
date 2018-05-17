# coding:utf-8
import requests
import io
from zipfile import ZipFile

if __name__ == '__main__':
    zip_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
    r = requests.get(zip_url)
    z = ZipFile(io.BytesIO(r.content))
    file = z.read('SMSSpamCollection')
    text_data = file.decode()
    text_data = text_data.encode('ascii', errors='ignore')
    text_data = text_data.decode().split('\n')
    text_data = [x.split('\t') for x in text_data if len(x) >= 1]
    [text_data_target, text_data_train] = [list(x) for x in zip(*text_data)]
    print(len(text_data_train))
    print(set(text_data_target))
    print(text_data_train[1])
