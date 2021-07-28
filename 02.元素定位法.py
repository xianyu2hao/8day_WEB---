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

# 导包
from selenium import  webdriver
from time import  sleep
# 获取浏览器对象
driver = webdriver.Chrome()
#打开url
url = ""
driver.get(url)
# 查找电话 输入186111111111
driver.find_element_by_class_name("tellA").send_keys("186111111111")
# 查找邮箱 123456@qq.com
driver.find_element_by_class_name("emailA").send_keys("123456@qq.com")
# 前体需要由class属性，同样其他元素需要id属性和name属性
# 暂停3s
sleep(3)