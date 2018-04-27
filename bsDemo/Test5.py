# coding:utf-8
import csv
if __name__ == '__main__':
    headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
    rows = [
        {1001, 'qiye', 'qiye_pass', 24, 'China'},
        {1001, 'Mary', 'Mary_pass', 20, 'USA'},
        {1001, 'Jack', 'Jack_pass', 20, 'USA'}
    ]
    with open('qiye.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)





