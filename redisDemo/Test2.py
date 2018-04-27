# coding:utf-8
import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    # r.set('name','qiye', ex=3)
    # print(r.get('name'))

    # r.hset('age','zhangsan',33)
    # print( r.hget('age', 'zhangsan'))

    # r.setnx('name','lisi')
    #
    # print(r.get('name'))



    # r.setex('name','wangwu', 10)
    # print(r.get('name'))
    # r.set('name','qiye安全博客')
    # print(r.getrange('name',0, 9))

    # r.lpush('digit',11,22,33)
    # print(r.lrange('digit',0, 2))
    # print(r.lpop('digit'))

    # r.sadd('num',33,44,55,66,77)
    # print(r.scard('num'))
    # print(r.smembers('num'))

    # r.sadd('num1', 88, 99, 55, 66, 77)

    # print(r.sdiff('num1','num'))
    # print(r.sinter('num','num1'))
    # print(r.sunion('num','num1'))

    r.zadd('z_num',num1=11,num2=22)
    print(r.zcard('z_num'))





