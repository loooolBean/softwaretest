from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.baidu.com/"
driver.get(url)
driver.maximize_window()

time.sleep(2)

# 所有页面
print(driver.window_handles)
# 当前页面
print(driver.current_window_handle)

driver.find_element_by_id("kw").send_keys("美女")
driver.find_element_by_id("su").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='1']").click()
driver.implicitly_wait(2)

print(driver.current_window_handle)
# 切换页面
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//*[@id='currentImg']").click()
time.sleep(1)
driver.get_screenshot_as_file("img.png")

time.sleep(5)

# 回收资源
driver.quit()

