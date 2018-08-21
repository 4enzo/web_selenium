# -*- coding: utf-8 -*-
'''
Created on 2018-08-19

@author: Enzo
'''

from selenium import webdriver
import time


# 存放账号/密码
import account

def login(br):
    '''登录hrss'''
    if '用户认证中心' in br.title:
        print('开始认证登录')
        username = br.find_element_by_xpath('//*[@id="tbxUserName"]')
        passwd = br.find_element_by_xpath('//*[@id="tbxPassword"]')
        login_btn = br.find_element_by_xpath('//*[@id="btnLogin"]')
        username.send_keys(account.username)
        passwd.send_keys(account.passwd)
        login_btn.click()
        if 'HRSS | 首页' in br.title:
            print('登录成功')
            return br
        else:
            print('登录失败')
    else:
        print('未打开登录界面')



def logout(br):
    '''注销登录'''
    logout_link = br.find_element_by_xpath('//*[@id="ctl00_LinkButton1"]')
    logout_link.click()
    # 接受弹窗,并点击确认
    br.switch_to_alert().accept()
    print('注销成功')



def main():
    url = 'http://hrss.h3c.com'
    # a = webdriver.Firefox()
    br = webdriver.Chrome()
    br.get(url)
    time.sleep(3)
    login(br)
    logout(br)

    time.sleep(5)
    br.close()

if __name__ == '__main__':
    main()


