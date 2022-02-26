from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

driver.find_element_by_id("kw").send_keys("python")
time.sleep(3)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("周杰伦")
driver.find_element_by_id("kw").click()

print(driver.find_element_by_id("kw").size)  # 获取元素大小
print(driver.find_element_by_id("kw").text)  # 获取元素文本（因为没有文本所以是空的）
print(driver.find_element_by_xpath("//*[text()='新闻']").get_attribute("href"))  # 获取元素属性
print(driver.find_element_by_id("kw").is_enabled())  # 判断元素是否可用
print(driver.find_element_by_id("kw").is_displayed())  # 判断元素是否可见


time.sleep(5)

# 回收资源
driver.quit()

