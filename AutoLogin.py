# Auto Login - Mikrotik Hotspot Authentication

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os, platform

print("Auto Login - Mikrotik Hotspot Authentication")

class AutoLogin:

    def __init__(self, username, password, ip):
        self.username = username
        self.password = password
        self.ip = ip
        self.driver = webdriver.Chrome() # select browser

    def CloseBrowser(self):
        self.driver.quit()
        print("[Status] : Close browser")

    def Login(self):
        driver = self.driver
        address = self.ip
        driver.get(address)
        time.sleep(1)
        username_element = driver.find_element_by_xpath("//input[@name='username'][@type='text']")
        username_element.clear()
        username_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password'][@type='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        try:
            driver.find_element_by_xpath("//input[@name='username'][@type='text']") or driver.find_element_by_xpath("//input[@name='password'][@type='password']");
            print("[Status] : Wrong username or password ")
        except:
            print("[Status] : Login successful")
        
    def LoginCheck(self):
        print("[Status] : Login Check")
        hostname = "8.8.8.8" # ip address to ping test 
        response = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ")+ "-W 0.1 " + hostname)
        if response == 0:
            pingstatus = True
        else:
            pingstatus = False
        return pingstatus
        
# Setting ("username", "password", "hotspot_ip-address")
Auto = AutoLogin("username", "password", "192.168.0.1")
print("[Status] : Running scripts")
if Auto.LoginCheck():
    print("[Status] : Already login")
    Auto.CloseBrowser()
else:
    print("[Status] : Not logged in")
    Auto.Login()
    Auto.CloseBrowser()
