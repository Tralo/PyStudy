# coding:utf-8
import time
import random
import threading

class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls
    def run(self):
        print('Current %s is running....' % threading.current_thread().name)
        for url in self.urls:
            print('%s ---->>>> %s'  % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended' % threading.current_thread().name)


if __name__ == '__main__':
    t1 = myThread(name='Thread-1',urls=['url_1','url_2','url_3'])
    t2 = myThread(name='Thread-2', urls=['url_4444', 'url_55555', 'url_66666'])

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended' % threading.current_thread().name)





