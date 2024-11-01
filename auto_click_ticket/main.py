from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login_in():
    # username
    username_input_xpath = "//div[@id='LoginForm']//div[@id='NormalLogin']//input[@id='UserNameText']"
    username_input = browser.find_element(By.XPATH, username_input_xpath)
    username_input.send_keys('gg777')

    # passwd
    passwd_input_xpath = "//div[@id='LoginForm']//div[@id='NormalLogin']//input[@id='PasswordText']"
    passwd_input = browser.find_element(By.XPATH, passwd_input_xpath)
    passwd_input.send_keys('kzjjg123456!')

    # login in button
    login_in_button_xpath = "//div[@id='LoginForm']//a[@id='LoginButton']"
    login_in_button = browser.find_element(By.XPATH, login_in_button_xpath)
    login_in_button.click()

    # ok button only if already login in other devices
    ok_button_xpath = "//div[@id='confirmBox']/form[@class='login-confirm-form']//button[@class='btn-sure']"
    ok_button = browser.find_element(By.XPATH, ok_button_xpath)
    if ok_button : ok_button.click()
    


browser = webdriver.Chrome()
browser.implicitly_wait(5)  # 隐式等待5s

# 登录url
url = 'https://mp.sh-cm.com:8090/i6/web/'
browser.get(url)

time.sleep(1)

# if in login in page
login_div_xpath = "//div[@id='LoginForm']//div[@id='NormalLogin']"
login_div = browser.find_element(By.XPATH, login_div_xpath)
if login_div : login_in()

time.sleep(1)

# 小票签收url
ticket_url = 'https://mp.sh-cm.com:8090/SCM/Common/SCM3ScgTicket/SCM3ScgTicketList'
browser.get(ticket_url)
input()





input()

browser.quit()
