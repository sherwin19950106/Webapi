import requests
url = 'http://localhost/api/mgr/sq_mgr/'
dict1 ={'action': 'list_course', 'pagenum':1, 'pagesize':20}
requests.get(url, params=dict1)