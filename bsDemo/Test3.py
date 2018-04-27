# coding:utf-8
import json

if __name__ == '__main__':
    str = [{'username': '七夜', 'age': 24}, (2, 3), 1]
    json_str=json.dumps(str, ensure_ascii=False)
    print(json_str)



