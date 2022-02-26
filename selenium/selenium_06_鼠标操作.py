from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

action = ActionChains(driver)
# 右键点击操作
action.context_click(driver.find_element_by_id("su"))
# 悬停操作
# action.move_to_element(driver.find_element_by_xpath("//*[@class='soutu-btn']"))
# 查看
# action.click_and_hold(driver.find_element_by_xpath("//*[@class='soutu-btn']"))
# 拖拽
# action.drag_and_drop(driver.find_element_by_id("div1"), driver.find_elements_by_id("div2"))
action.perform()

time.sleep(5)

# 回收资源
driver.quit()
