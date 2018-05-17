# coding:utf-8
import requests

if __name__ == '__main__':
    housing_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
    housing_header = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDVO']
    housing_file = requests.get(housing_url)
    housing_data = [[float(x) for x in y.split(' ')if len(x) >= 1] for
                    y in housing_file.text.split('\n') if len(y) >= 1]
    # print(housing_data)
    print(len(housing_data))
    print(len(housing_data[0]))
    print(housing_data[0])


