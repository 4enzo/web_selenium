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

def attendance_info(br):
    '''获取考勤信息'''
    print('正在获取考勤信息')
    attendance_link = br.find_element_by_link_text('考勤信息')
    attendance_link.click()

    holiday_balance = br.find_element_by_xpath('//*[@id="ctl00_ContentMain_lblNXJYE"]').text
    extra_work_time = br.find_element_by_xpath('//*[@id="ctl00_ContentMain_lblYXGS"]').text
    abnormal_attendance = br.find_element_by_xpath('//*[@id="ctl00_ContentMain_lblKQYCS"]').text

    print('年休假余额：%s天'%holiday_balance)
    print('有效工时余额：%s小时'%extra_work_time)
    print('月度考勤异常：%s'%abnormal_attendance)


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
    attendance_info(br)
    logout(br)

    time.sleep(5)
    br.close()

if __name__ == '__main__':
    main()


