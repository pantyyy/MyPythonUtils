import json
import requests
from lxml import etree
import re
import os
from selenium import webdriver
import time

"""
    作用 :
        使用requests模块 ， 获取页面源码

    参数:
        target_url : 目标url
        cookie_dict : cookie信息
        headers : header信息
    返回值:
        字符串
"""
def get_html_by_request(target_url , cookie_dict=None , headers=None):

    if headers == None :
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
    response = requests.get(target_url, headers = headers, cookies = cookie_dict)
    # print(response.text)

    return response.text

"""
    作用 :
        使用requests模块 ， 获取页面response

    参数:
        target_url : 目标url
        cookie_dict : cookie信息
        headers : header信息
    返回值:
        字符串
"""
def get_response_by_request(target_url , cookie_dict=None , headers=None):

    if headers == None :
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
    response = requests.get(target_url, headers = headers, cookies = cookie_dict)

    return response


"""
    作用 :
        使用Xpath提取html字符串中的数据
        
    参数:
        html_str : html字符串数据
        xpath_str : 提取数据的规则 
"""
# 根据xpath获取html中的数据
def get_data_from_html_by_xpath(html_str , xpath_str):
    # 获取页面源码进行xpath解析
    xpath_data = etree.HTML(html_str)
    data = xpath_data.xpath(xpath_str)
    return data


"""
    作用 :
        根据url , 返回页面源码

    参数:
        driver : 浏览器对象
        target_url : 目标url
    返回值:
        字符串
"""
def get_html_by_selenium(driver , target_url):
    driver.get(target_url)
    return driver.page_source


"""
    作用 :
        初始化selenium浏览器
    返回值:
        browser对象
"""
def init_selenium(domain=None , cookie_dict=None):
    # 关闭显示通知
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    options.add_experimental_option('prefs', prefs)
    # 设置为无头浏览器
    # options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)



    browser.get("https://www.google.com/")
    browser.maximize_window()

    # 给浏览器添加cookie
    if domain != None :
        for key, value in cookie_dict.items():
            browser.add_cookie({'domain': domain , 'name': key, 'value': value})

    return browser

"""
    作用 :
        登陆Chrome
"""
def login_chrome(browser):
    browser.get("https://accounts.google.com")
    email_input = browser.find_element_by_xpath("//input[@type=\"email\"]")
    pwd_input = browser.find_element_by_xpath("//input[@type=\"password\"]")


    email_input.send_keys("pantyAstocking@gmail.com")

    next_btn = browser.find_element_by_xpath("//span[@class=\"CwaK9\"]")
    next_btn.click()


    time.sleep(2)

    try:
        pwd_input = browser.find_element_by_xpath("//input[@type=\"password\"]")
        print(pwd_input.get_attribute("type"))
        pwd_input.send_keys("Lck053258")

    except :
        print("重新获取元素password")
        pwd_input = browser.find_element_by_xpath("//input[@type=\"password\"]")
        pwd_input.send_keys("Lck053258")


    try:
        next_btn = browser.find_element_by_xpath("//span[@class=\"CwaK9\"]")
        next_btn.click()

    except:
        print("重新获取元素next_btn")
        next_btn = browser.find_element_by_xpath("//span[@class=\"CwaK9\"]")
        next_btn.click()



if __name__ == '__main__':
    browser = init_selenium()
    login_chrome(browser)



















