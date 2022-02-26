from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url——非此地址
url = "https://www.baidu.com/"

driver.get(url)

time.sleep(5)
driver.find_element_by_id("alerts").click()

# 要切到警告框才能操作警告框
alert = driver.switch_to.alert()
print(alert.text)
# 关闭警告框
alert.dismiss()

# 回收资源
driver.quit()

