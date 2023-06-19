import requests
import json

URL = "http://127.0.0.1:8000/studentapi"

def get_data(id = None):
    print("id...",id)
    data = {}
    if id is not None:
        data = {'id': id}
        # print("data is",data)
    json_data = json.dumps(data)
    # print("data is",json_data)
    r = requests.get(url=URL,data = json_data)
    # print('this is R...............',data,r)
    data = r.json()
    print(data)

# get_data()


def post_data():
    data = {
        'name':'Gautam',
        'roll': 10,
        'city': 'amreli'
    }
    json_data = json.dumps(data)
    # print("json....",json_data)
    r = requests.post(url=URL,data = json_data)
    # print('this is R...............',data,r)
    data = r.json()
    print(data)
# post_data()


def update_data():
    data = {
        'id': 8,
        'name': 'Dhara',
        'city': 'abuabu'
    }
    json_data = json.dumps(data)
    # print("json....",json_data)
    r = requests.put(url=URL,data = json_data)
    # print('this is R...............',data,r)
    data = r.json()
    print(data)
# update_data()


def delete_data():
    data = {
        'id': 8
    }
    json_data = json.dumps(data)
    # print("json....",json_data)
    r = requests.delete(url=URL,data = json_data)
    # print('this is R...............',data,r)
    data = r.json()
    print(data)
delete_data()