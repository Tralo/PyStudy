# coding:utf-8
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
    headers = {'User-Agent': user_agent}

    r = requests.get('http://seputu.com/', headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')

        if(h2 != None):
            h2_title = h2.string
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.get('title')
                print('href  ---> %s' % href)
                print('title ---> %s' % box_title)







