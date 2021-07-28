from time import  sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
sleep(3)
driver.quit()


# 安装好，python后，按照该博主装没问题：https://blog.csdn.net/orange_xiang/article/details/82924296?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control