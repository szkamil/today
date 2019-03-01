import json
import os
import requests
import sqlite3
from requests.auth import HTTPBasicAuth
from jsondiff import diff
import hashlib


# import json
# # test url site
# # auth = () - use env variables
# payload = {}
# url = 'https://jsonplaceholder.typicode.com/posts'
# url_json = requests.get(url, payload).json()
# print(type(url_json))
# print(url_json)
# print(url_json[1])


# ===================COMPARE
with open('json1') as j1:
    json1 = json.load(j1)

with open('json2') as j2:
    json2 = json.load(j2)
x = diff(json1, json2)
print(type(x))
print(diff(json1, json2))

# requests.put('url', )


# print(type(json))
#
# x = json.json
# print(type(x))


#    conn = sqlite3.connect(':memory:')
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS test(
#                 postId integer primary key,
#                 id integer,
#                 name text,
#                 email text,
#                 body text
#                 )""")
#
#
#     for i in range(len(url_json)):
#         c.execute("INSERT INTO test VALUES (?, ?, ?, ?,?)",( url_json[i]['postId'], url_json[i]['id'],
#                                                              url_json[i]['name'], url_json[i]['email'], url_json[i]['body']))
# except:
#     pass
#     # add error handling
# finally:
#     conn.commit()
