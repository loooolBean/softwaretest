from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

element = driver.find_element_by_id("kw")
# 需求：输入python，然后全选，回退输入，再输入“美女”,点击百度一下
element.send_keys("pyhton")
element.send_keys(Keys.CONTROL, "a")  # 键盘的control + a
element.send_keys(Keys.BACK_SPACE)    # 键盘的backspace键
element.send_keys("美女")
driver.find_element_by_id("su").click()

# 回收资源
driver.quit()

