import requests
import datetime
import pprint


def add_json_course():
    time1 = str(datetime.datetime.now()).split('.')[0]
    url = 'http://localhost/apijson/mgr/sq_mgr/'
    jsons = {
      "action" : "add_course_json",
      "data"	 : {
        "name": "课程"+time1,
        "desc": "课程"+time1,
        "display_idx": "4"
      }
    }
    res = requests.post(url, json=jsons)

    if res.json()['retcode'] == 0:
        print('插入成功')
        return res.json()['id']
    else:
        print('失败')


def find_id_course(id):
    url = 'http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
    res = requests.get(url)
    if res.json()['retcode'] == 0:
        for i in res.json()['retlist']:
            if i['id'] == id:
                print('-----插入内容-----')
                pprint.pprint(i)
    else:
        print('查询失败')


if __name__ == '__main__':
    find_id_course(add_json_course())

