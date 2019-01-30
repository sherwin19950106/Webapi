import requests
import time

time1 = time.time()
url = 'http://localhost/apijson/mgr/sq_mgr/'
payload = {
  "action": "add_course_json",
  "data": {
    "name": time1,
    "desc": "初中化学课程",
    "display_idx": "4"
  }
}
res = requests.post(url, json=payload)
if res.json()['retcode'] == 2:
    print('失败')
elif res.json()['retcode'] == 0:
    print('pass')