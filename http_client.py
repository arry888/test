import requests

r = requests.get('https://www.baidu.com')
print(r.status_code)  # 状态码
# print(r.headers) # header
# for k in r.headers:
#     print(r.headers[k])
print(r.headers)  # header字段
# print(r.text)


# r1 = requests.get('https://api.github.com/events', auth=('user', 'pass'))
# print(r1.text)
# print(r1.status_code)


r2 = requests.post('http://httpbin.org/post', data={'key': 'value'})
# print(r2)
# print(r2.text)
# print(r2.json())
# print(r2.json()['form'])


payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.status_code)
print(r.headers)
print(r.url)
print(r.encoding)

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
