# coding:utf-8
import random
import time,threading
def thread_run(urls):
    print('Current %s is running...' % (threading.current_thread().name))
    for url in urls:
        print('%s ------>>>> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)



if __name__ == '__main__':
    t1 = threading.Thread(target=thread_run, args=(['url_1','url_2','url_3'],))
    t2 = threading.Thread(target=thread_run, args=(['url_444444', 'url_55555', 'url_6666'],))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)




