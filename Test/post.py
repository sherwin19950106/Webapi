import requests
import Test.get
import time
time1 = time.time()
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'action': 'add_course', 'data': '''{
                                              "name":%s,
                                              "desc":"初中化学课程",
                                              "display_idx":"4"
                                            }'''%  (time1)
}
requests.post(Test.get.url, data=payload)