import requests
import random


def find_course():
    list = []
    url = 'http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
    res = requests.get(url)
    if res.json()['retcode'] == 0:
        for i in res.json()['retlist']:
            list.append(i['name'])
        print('现有课程名：', list)
        choose = random.sample(list, 1)[0]
        print('随机选取一个name：', choose)
        return choose
    else:
        print('查询失败')


def add_json_course(choose):
    url = 'http://localhost/apijson/mgr/sq_mgr/'
    jsons = {
      "action" : "add_course_json",
      "data"	 : {
        "name": choose,
        "desc": choose,
        "display_idx": "4"
      }
    }
    print('-----准备插入-----')
    res = requests.post(url, json=jsons)

    if res.json()['retcode'] == 2:
        print(res.json())
        print('ok')
    else:
        print('error')
        print(res.json())

if __name__ == '__main__':
    add_json_course(find_course())
