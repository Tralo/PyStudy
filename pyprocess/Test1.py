# coding:utf-8
from multiprocessing import Process,Queue
import os,time,random

def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':
    q = Queue()
    proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2 = Process(target=proc_write,args=(q,['url_444','url_555','url_666']))
    proc_reader = Process(target=proc_read,args=(q,))
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()

    proc_writer1.join()
    proc_writer2.join()

    proc_reader.terminate()






