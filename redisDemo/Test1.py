# coding:utf-8

import redis

if __name__ == '__main__':

    pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
    r = redis.Redis(connection_pool=pool)
    print(r.get('name'))







