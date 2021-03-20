import requests

uri = 'http://localhost:8080'

r = requests.get(uri)

# To see the status code, print r
# print(r)
#
# To see the return data, or error message, print r.text
# print(r.text)

if r:
    print(r.json())
else:
    print(r)

