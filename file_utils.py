#coding=utf-8
import configparser
import json
import os
import random
import string



"""
    作用 :
        根据路径创建文件夹
    参数:
        dir_path : 指定文件夹的路径
"""
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print("创建" + dir_path + "成功！！！")


"""
    作用 :
        向指定文件中写入数据
    参数:
        file_path : 指定文件的路径
        data : 需要写入的数据
"""
# write_data_2_file("G://test//test.txt" , "I love you")
def write_data_2_file(file_path , data):
    #with open(file_path, "wb") as f:
    with open(file_path , "w" , encoding="utf-8") as f:
        f.write(data)


"""
    作用 :
        根据.ini文件路径读取文件
    参数:
        file_path : 文件路径
    返回值:
        .ini文件对象
"""
def get_ini_file(file_path):
    cf_file = configparser.ConfigParser()
    cf_file.read(file_path)
    return cf_file


"""
    作用 :
        根据节点名 ， 键名 ， 获取获取.ini文件对应的值
    参数:
        cf : 配置文件对象
        node_name : 节点的名字
        key : 键名
    返回值:
        字符串
"""
def get_ini_file_value_by_key(cf , node_name , key):
    data = cf.get(node_name , key)
    return data


"""
    作用 :
        根据文件路径读取json字符串格式的文件
    参数:
        file_path : json文件路径
    返回值:
        字典对象
"""
def read_json_file(file_path):
    load_file = open(file_path , encoding='utf-8')
    json_data = json.load(load_file)
    return json_data


"""
    作用 :
        字典对象写入文件中
        
    参数:
        file_path : 写入文件的位置
        data_dict : 字典对象

"""
def write_dict_to_file(file_path , data_dict) :
    jsObj = json.dumps(data_dict)
    fileObject = open(file_path , 'w' , encoding="utf-8")
    fileObject.write(jsObj)
    fileObject.close()



if __name__ == '__main__':
    file_path = r'D:/PythonProject/SeleniumCode/config/LocalElement.ini'
    cf_file = get_ini_file(file_path)


    node_name = "RegisterElement"
    key = "user_name_error"

    data = get_value_by_key(cf_file , node_name , key)
    print(data)