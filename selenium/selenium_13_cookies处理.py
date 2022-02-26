from selenium import webdriver
import time

# 获取浏览器的对象
path = "../chromedriver.exe"  # 设置环境变量
driver = webdriver.Chrome(path)

# 输入url
url = "https://mail.qq.com/cgi-bin/frame_html?sid=bsUmRADPsKUGVABh&r=d81f5ec47ab43984de4358725505fcf2"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(2)
driver.add_cookie({"name": "skey", "value": "@CIqpRbPjc"})
time.sleep(5)

# 回收资源
driver.quit()

