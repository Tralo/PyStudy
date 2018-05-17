# coding:utf-8
import requests

if __name__ == '__main__':
    birthday_url = "https://www.umass.edu/statdata/statdata/data/lowbwt.dat"
    birth_file = requests.get(birthday_url)
    birth_data = birth_file.text.split('\r\n')[5:]
    birth_header = [x for x in birth_data[0].split('') if len(x) >= 1]
    birth_data = [[float(x) for x in y.spilt('') if len(x) >= 1] for y in birth_data[1:] if len(y) >= 1]
    print(len(birth_data))
    print(len(birth_data[0]))
