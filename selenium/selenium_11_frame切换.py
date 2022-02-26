# https://mail.qq.com/
from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://mail.qq.com/"
driver.get(url)

time.sleep(2)
# 定位到输入账号和密码——因为输入账号密码的是frame框架是另一个网页，所以直接使用driver会报错，所以需要切换到frame界面
# 方法类似警告框
driver.switch_to.frame(driver.find_element_by_id("login_frame"))
driver.find_element_by_id("u").send_keys("1410679979@qq.com")
# 切换回最原始的frame，因为不退回原始的frame，只能用当前切换frame框架的内容
driver.switch_to.default_content()

time.sleep(5)

# 回收资源
driver.quit()

