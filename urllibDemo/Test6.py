import requests

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)



