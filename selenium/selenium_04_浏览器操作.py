from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

# 浏览器最大化
driver.maximize_window()
# 设置浏览器大小 800*600
# driver.set_window_size(800, 600)
# 设置浏览器的位置
# driver.set_window_position(300, 100)

driver.find_element_by_id("kw").send_keys("周杰伦")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.back()  # 后退
time.sleep(3)
# driver.forward()  # 前进
driver.refresh()  # 刷新浏览器
driver.find_element_by_xpath("//*[text()='新闻']").click()
time.sleep(3)
driver.close()  # 关闭当前页面


time.sleep(5)

# 回收资源
driver.quit()

