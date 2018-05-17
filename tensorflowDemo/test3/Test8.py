# coding:utf-8
import requests


if __name__ == '__main__':
    shakespeare_url = 'http://www.gutenberg.org/cache/epub/100/pg100.txt'
    response = requests.get(shakespeare_url)
    shakespeare_file = response.content
    shakespeare_text = shakespeare_file.decode('utf-8')
    shakespeare_text = shakespeare_text[7675:]
    print(shakespeare_text)
