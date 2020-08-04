import sys
import requests
from requests.auth import HTTPBasicAuth


f_n,username,password = sys.argv
print("Got username", username)
print("Got Password", password)

url = 'http://10.114.4.99:8080/job/Barossa-Website-fullstack-UI-Regression-Entities/16/api/json'

sess = requests.Session()
sess.auth = (username, password)
res = sess.get(url)
print(res.status_code)

