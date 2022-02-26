from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://www.douyu.com/directory/all"
driver.get(url)
driver.maximize_window()
# 绝对滚动，滚动到最下方，先编写js代码
js_str = "window.scrollTo(0,10000)"
driver.execute_script(js_str)


# time.sleep(2)
# driver.find_element_by_xpath("//*[@title='下一页']").click()

time.sleep(5)

# 回收资源
driver.quit()

