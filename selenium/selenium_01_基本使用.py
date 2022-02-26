from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

time.sleep(5)

# 回收资源
driver.quit()

