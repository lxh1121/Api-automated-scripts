#coding=utf-8
import json
from getpathInfo import get_Path


def read_json(file_name=None):
    if file_name == None:
        file_path = get_Path() + "/Config/user_data.json"
    else:
        file_path = get_Path() + file_name
    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)


def write_value(data, fileUrl):
    data_value = json.dumps(data)
    with open(get_Path() + fileUrl, "w") as f:
        f.write(data_value)

def empty_fileData(file_name):
    file_path = get_Path() + file_name
    with open(file_path, 'r+', encoding='UTF-8') as f:
        f.truncate()

if __name__ == "__main__":
    data = {
        "aaaa":"bbbbbb"
    }
    # write_value(data)
    # print(base_path)