from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

time.sleep(5)

# 创建select对象——复选框的id为selectA，其中的option为
select = Select(driver.find_element_by_id("selectA"))
select.select_by_index(3)
select.select_by_value("bj")
select.select_by_visible_text("A广州")
# 回收资源
driver.quit()

