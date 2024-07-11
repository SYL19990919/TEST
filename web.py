import time

from selenium import webdriver

from selenium.webdriver.common.by import By


driver=webdriver.Edge() #选择edge这个浏览器，初始化driver===可以浏览器进行沟通，建立会话=session
driver.implicitly_wait(10)
#1、 打开一个网址
driver.get("https://ids.cqupt.edu.cn/authserver/login?service=https%3A%2F%2Fi.cqupt.edu.cn%2Flogin%23%2F")
#2、 浏览器最大化
driver.maximize_window()

#driver.switch_to.frame()
#driver.find_element(By.ID,"switcher_plogin").click()
# driver.find_element(By.XPATH,"//input[@id="u"]").send_keys("1325078415")
#
#
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("3119117")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("SYL194087")
driver.find_element(By.XPATH,"//a[@id='login_submit']").click()
time.sleep(10)

#driver.get("https://www.jianshu.com/p/5c1f846e8dc1")

# time.sleep(2)
#
# driver.back()
#
# time.sleep(2)
#
# driver.forward()
#
#
# time.sleep(2)
