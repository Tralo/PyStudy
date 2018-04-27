# coding:utf-8
import time
from multiprocessing.managers import BaseManager

class Queuemanager(BaseManager):
    pass

Queuemanager.register('get_task_queue')
Queuemanager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)

m = Queuemanager(address=(server_addr,8001), authkey=b'qiye')

m.connect()


task = m.get_task_queue()
result = m.get_result_queue()

while(not task.empty()):
    image_url=task.get(True, timeout=5)
    print('run task download %s ...' % image_url)
    time.sleep(1)
    result.put('%s ---> success ' % image_url)
print('worker exit.')

