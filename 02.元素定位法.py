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
