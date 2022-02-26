from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome()

# 输入url
url = "https://www.baidu.com/"
driver.get(url)

# 元素定位——普通方式
driver.find_element_by_id("kw").send_keys("周杰伦")
# driver.find_element_by_id("su").click()
# driver.find_element_by_class_name("s_ipt").send_keys("周杰伦")
# driver.find_element_by_link_text("新闻")
# driver.find_element_by_partial_link_text("新")

# 元素定位——css选择器方式
# driver.find_element_by_css_selector("#kw").send_keys("周杰伦")
# driver.find_element_by_css_selector(".s_ipt").send_keys("周杰伦")
# driver.find_element_by_css_selector("[name=wd]").send_keys("周杰伦")
# driver.find_element_by_css_selector("#su").click()
# driver.find_element_by_css_selector("[value=百度一下]").click()


# 元素定位——xpath方式
driver.find_element_by_xpath("//*[@id='kw']").send_keys("周杰伦")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(5)
# 回收资源
driver.quit()

