from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

driver.find_element_by_xpath("//*[@id='kw']").send_keys("美女")
driver.find_element_by_xpath("//*[@id='su']").click()

# 强制等待——不是最优解，因为根据网速不一样可能依旧会报错或者出现浪费时间
time.sleep(3)

# 显示等待——浏览器最多等待5s,直到查找出现元素定位ID为"content_right"才执行
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, '1')))

# 隐式等待——没有具体期待条件，所以是等所有元素
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='1']").click()
time.sleep(2)

# 回收资源
driver.quit()

