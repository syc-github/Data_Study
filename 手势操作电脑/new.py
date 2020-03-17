#!/usr/bin/env python
#@Time:2019/8/13 19:31
#@Author:老杨
#@File:new.py
#@Software:PyCharm
"""
课题分享：python骚操作之：手势智能机器人
主讲老师：老杨老师
1  2
开发环境：pycharm + python3
温馨提示：
学习没有太多捷径，但是学习有方式和方法
科学的学习方式和方法可以帮助你更快的学好知识
为了帮助同学们有最大的收获，希望同学们能遵守下面的规则：
第一：不要拘泥于代码  思维远比代码更重要，紧跟老师思维
第二：积极和老师互动，便于老师了解同学们的吸收情况
第三：不懂得问题及时发出来，知道答案的同学主动帮助
（这是对你的知识的巩固，同时说不定你的答案是错的，老师就会帮你纠正）
"""
# 直男思维  -》编程思维
# 666
# 第一：明确你的需求
# 听过我的手势就可以进行我想要的操作 -》控制电脑
# 1   2
# 思路分析  -》选择我们的技术架构
# 第一：怎么观察到我的手势
# 第二：怎么通过手势进行对应的操作
# 代码实现
# 库
# 标准库  第三方库
# 不要重复造轮子  懒
# pip install opencv-python
# pip install baidu-aip
# pip install pillow
import cv2
from aip import AipBodyAnalysis
from PIL import ImageGrab
import Control
# 主程序的入口
# 方便我们代码的调试
# 第一初级版本的第一小步
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def index(fileName):
    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''
    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(fileName)
    """ 调用手势识别 """
    res = client.gesture(image)
    if 'error_code' in res:
        print(res['error_msg'])
    try:
        classname = res['result'][0]['classname']
        print(classname)
        return classname
    except Exception as err:
        print('手势识别失败')
    # 告诉了我们手势到底是什么？
def screen():
    im = ImageGrab.grab()
    im.save('screen.png')
def test(classname):
    if classname=='One':
        screen()
    elif classname=='Five':
        print(5)
    else:
        print('其他')
def control():
    # 1  2
    className = index('start.jpg')
    if className=='One':
        control = Control.Order()
        control.run('打开微信')
    if className == 'Five':
        screen()
def main():
    # 程序中断
    # 出现的效果和预期不一致
    # 第一个：
    # 调用电脑第一个摄像头
    cap = cv2.VideoCapture(0)
    # 读取摄像头的资源
    # 是否读取成功
    # 读取到的数据资源
    ret,frame = cap.read()

    if ret:
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame',frame)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break
            if k == ord('a'):
                cv2.imwrite('start.jpg',frame)
                control()
        # # 程序的健壮性
        # cv2.imwrite('laoyang.jpg',frame)
        # className = index()
        # test(className)
    # 释放摄像头
    cap.release()
    # 删除建立的全部窗口
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
    # index()
# 更骚气
# 999  666
# 222
# 888
# Python
# 简洁高效
# 人工智能  -》 Python
# 1991
# 2015年底
# web  爬虫 自动化运维 数据分析 数据挖掘
# 。。。。。。
# 尽量不要汉化
# 自学  耽误
# 不知道学什么
# 不知道怎么学
# Python
# 人工智能 （门槛高 ）
# web全栈开发
# 高工资 低门槛 岗位多
# 47%  10K
# 一点的一点
# 具备独自开发企业级项目的能力
# 可直接
# 学好Python  你是否掌握了就业的技能点
# web
# Python的开发技巧
# # # 数据库
# # # 前端
# # # web框架
# # # Linux
# # # *******
# # # 项目实战能力
# 5个月的时间
# 项目
# 小班
# 53期
# 3个名额
# 晚上 视频直播互动的方式
# 高清视频录播
# 1
# 每堂课  课后作业
# 每一个阶段  阶段性的考核
# 免费重修
# 53
# 52期
# 500
# 7880元* 0.85  3个
# 最多支持到12期的分期
# 5个月
# 截止今晚老师下课之前最后3个名额
# 53
# Python
# C  几千  Java  几百  Python 几十
# 语言 适应性
# 2 就业
# Python前景更好  适应范围更广
# 就业
# 2015年底  2017年底
# 40万 目前
# 1000   500  低门槛
# 1000  2000,3000
# 666
# 情况有些特殊
#