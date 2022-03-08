#coding=utf-8;
import os
from xlrd import open_workbook
import openpyxl
import pandas

path = "C:\Program Files (x86)\PICT\\"

def pandas_read(file_name):
    data = pandas.DataFrame(pandas.read_excel(file_name))

    return data


def read_file(file_name):
    """
    读取本地的接口请求参数（使用pict工具生成数据）
    :param pict_params:  本地路径
    :return: list
    """
    with open(path+file_name, 'r') as f:
        dataline = f.readlines()
    f.close()
    data = []
    for i in dataline:
        a = i.split()
        data.append(a)
    l_result = []
    if data:
        for info in range(len(data)):
            if info != 0:
                d_t = {}
                for item in range(len(data[info])):
                    a = data[info][item].replace("：", ":")
                    t_result = a.split(":")
                    t = {}
                    t[t_result[1]] = t_result[2]
                    t[t_result[3]] = t_result[4]
                    d_t[t_result[0]] = t
                l_result.append(d_t)
    return l_result

def read_simple(filename):
    with open(path+filename, 'r') as f:
        dataline = f.readlines()
    f.close()
    data = []
    for i in dataline:
        a = i.split()
        data.append(a)
    if data:
        new_data = []
        for info in range(len(data)):
            if info != 0:
                d_t = {}
                print(data[info])
                for j in range(len(data[info])):
                    d_t[data[0][j]] = data[info][j]
                new_data.append(d_t)

    return True


if __name__ == "__main__":
    # t = read_pict_param()
    # t = pandas_read(path + 'test1.xlsx')
    t = read_simple('test3.txt')
    print(t)
    print(type(t))
    # print(type(t))