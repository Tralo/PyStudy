# coding:utf-8
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue


class Queuemanager(BaseManager):
    pass
if __name__ == '__main__':

    Queuemanager.register('get_task_queue', callable=return_task_queue)
    Queuemanager.register('get_result_queue', callable=return_result_queue)

    manager = Queuemanager(address=('127.0.0.1', 8001), authkey=b'qiye')

    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for url in ["ImageUrl_"+str(i) for i in range(10)]:
        print('put task %s ...' % url)
        task.put(url)

    print('try get result ...')

    for i in range(10):
        print('result is %s' % result.get(timeout=10))
    manager.shutdown()





