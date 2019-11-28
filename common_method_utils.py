import json
import requests
from lxml import etree
import re
import os
import xlrd
import xlwt
import random
import string






"""
    作用 :
        使用正则表达式提取需要的数据
    返回值:
        字符串
"""
def use_regex():
    # 待匹配字符串
    target_str = "https://images.unsplash.com/photo-1531563154281-041ebe947157?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max"
    # 编译匹配规则
    patter = re.compile('(.*?)photo-(.*?)\?ixlib=(.*)')
    # 获取想要的数据(方式一)
    result = patter.match(target_str)
    print(result.group())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))

"""
    作用 :
        生成指定长度的字符串 ， UUID
        
    返回值:
        字符串
"""
def generate_random_str(randomlength):
    '''
    string.digits = 0123456789
    string.ascii_letters = 26个小写,26个大写
    '''
    str_list = random.sample(string.digits + string.ascii_letters,randomlength)
    random_str = ''.join(str_list)
    return random_str


"""
    作用 :
        生成随机字符串

    返回值:
        字符串
"""
def generate_random_str_2():
    for i in range(5):
        user_email = ''.join(random.sample('0123456789adbcdefg' , 5))
        print(user_email)



"""
    作用 :
        字符串是否包含

    返回值:
        true或者false
"""
def is_contain(this_str , result_str):
    result = this_str in result_str
    return result


"""
    作用 :
        遍历list对象
"""
def traver_list():
    list = ["lck" , "zzt" , "cxk"];
    for str in list :
        print(str)


# 解析json数据
# get_json_data("https://unsplash.com/napi/landing_pages/images/people/girls?page=1&per_page=20")
def get_json_data(json_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    response = requests.get(json_url, headers = headers)
    json_data = json.loads(response.content)
    print(json_data)
    print(type(json_data))
    print(json_data["photos"])
    print(type(json_data["photos"]))

"""
    作用 :
        使用字符串切割
"""
def use_split():
    target_str = "https://res.cloudinary.com/twenty20/private_images/t_standard-fit/v1521838663/photosp/5cf5908b-c3b6-4b78-aabc-01684e7835e2/5cf5908b-c3b6-4b78-aabc-01684e7835e2.jpg"
    print(target_str.split("/")[len(target_str.split("/")) - 1])



def test():
    print("Helloworld")




def read_excel_by_cols(col_num , file_path , sheet_name):
    # 打开excel文件
    wb = xlrd.open_workbook(filename=file_path)

    # 获取所有表格名字
    # print(wb.sheet_names())
    # 通过表格名获取表格
    sheet1 = wb.sheet_by_name(sheet_name)
    # 获取第col_num列的数据
    cols = sheet1.col_values(col_num)
    return cols

"""
    作用 :
        根据指定列 ， 向excel表格中写入数据

    参数:
        col_num：指定在哪列写入数据
        file_path：文件路径
        sheet_name：表格名称
        data_list：需要写入的数据
"""
def write_excel_by_cols(col_num , file_path , sheet_name , data_list):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(sheet_name,cell_overwrite_ok=True)

    for i in range(0 , len(data_list)):
        sheet1.write(i , col_num , data_list[i])

    f.save(file_path)