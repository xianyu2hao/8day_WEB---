"""
# id定位法
from  selenium import  webdriver
from time import  sleep
driver = webdriver.Chrome
# python中的\是转义字符，如果使用需在总体前面加上r，例如url = r"E:\python\soft\data\AI.html"
# 还可以使用双反斜杠（\\）进行转义操作，例如，url = "E:\\python\\soft\\data\\AI.html"
# 使用本地浏览模式，前置加上：file:///，例如 url = "file:///E:/python/soft/data/AI.html"
url = "" # 这里需要填写
driver.get("")  # 这里需要填写
# 查找用户名元素
username = driver.find_element_by_id("userA")
# 查找密码元素
password = driver.find_element_by_id("passworA")
# 用户名输入admin ,send_keys
username.send_keys("admin")
# 密码输入123456
password.send_keys("123456")
# 延迟时间
sleep(3)
#关闭
driver.quit()
"""

"""
# name定位法
# 导包
from selenium import  webdriver
from time import  sleep
# 获取浏览器对象
driver = webdriver.Chrome()
#打开url
url = ""
driver.get(url)
# 查找用户名 admin
driver.find_element_by_name("userA").send_keys("admin")
# 查找密码 123456
driver.find_element_by_name("passwordA").send_keys("123456")

# 暂停3s
sleep(3)
"""
# class_name()定位法
"""
# 导包
from selenium import  webdriver
from time import sleep
# 获取浏览器对象
driver = webdriver.Chrome()
#打开url
url = ""
driver.get(url)
# 查找电话 输入186111111111
driver.find_element_by_class_name("tellA").send_keys("186111111111")
# 查找邮箱 123456@qq.com
driver.find_element_by_class_name("emailA").send_keys("123456@qq.com")
# 前提需要由class属性，同样其他元素需要id属性和name属性
# 暂停3s
sleep(3)
"""
'''
# tag_name定位
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器
driver = webdriver.Chrome()

# 打开html页面
url = ""
driver.get(url)
# tag_name定位用户名并输入admin
# 页面存在多个标签，默认选择第一个标签
driver.find_element_by_tag_name("imput").send_keys("admin")
# 暂停3秒
sleep(3)
# 退出
driver.quit()
'''
"""
# link_text定位，使用html页面，访问 新浪 链接
# 方法：diver.find_element_link_text() 定位元素
#      click
# 模糊定位的方法：partial_link_text # 智能定位a标签，且定位只能唯一，否则出问题
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器
driver = webdriver.Chrome()
# 打开html页面
url = ""
driver.get(url)
# 注意这个链接的全程需要匹配，不能省略例如“新浪”,非“新”
driver.find_element_by_link_text("新浪").click()
    # # 使用精准或模糊定位，模糊定位最好能代表唯一标签，多个值，默认返回第一个。
    # driver.find_element_by_partial_link_text("新").click()
# 暂停3秒
sleep(3)
# 退出
driver.quit()
"""
'''
# Xpath定位：其为xml path的简称,XML也是一种标记语言，html显示元素，css控制元素，xml为存储和传递数据，一般做软件配置。
# 定位策略：1.路径；2.元素属性；3.属性和逻辑；4.层级与属性
# 使用绝对路径定位 用户名 输入admin;暂停2秒钟；使用相对路径定位 密码 输入123456
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器
driver = webdriver.Chrome()
# 打开html页面
url = ""
driver.get(url)
# 绝对路径
driver.find_element_by_xpath("/html/body/form/div/p[1]/input").send_keys("admin")
# 相对路径
driver.find_element_by_xpath("//input[ @id ='password']").send_keys("123456")
# 逻辑结合
driver.find_element_by_xpath("//input[ @id ='password' and @placehold = '密码A']").send_keys("123456")
#层级结合
driver.find_element_by_xpath("//input[@ id = 'p1']/input").send_keys("123456")
# 暂停3秒
sleep(2)
# 停止
driver.quit()
'''

# css的元素定位
