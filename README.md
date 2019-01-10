# AutoLogin - Mikrotik Hotspot Authentication
 ### Requirement
 - Python 3.4+
 - Selenium - Module
 - Selenium Webdriver
 #### Webdriver - Download Link
 |Browser|Link|
 |:-:|:-:|
 |Chrome:|https://sites.google.com/a/chromium.org/chromedriver/downloads|
 |Edge:|https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/|
 |Firefox:|https://github.com/mozilla/geckodriver/releases|
 |Safari:|https://webkit.org/blog/6900/webdriver-support-in-safari-10/|
 ### How to use
 1. Edit username, password and hotspot-ip in "AutoLogin.py"
  _line(51) : Auto = AutoLogin("username", "password", "xxx.xxx.xxx.xxx")
 2. Set Browser to use auto-login (Default : Chrome)
 Ex. Firefox
 _line(16) : "self.driver = webdriver.Chrome()" Edit as "self.driver = webdriver.Firefox()"
 3. Run "AutoLogin.py" Python File
### Reference
 - https://pypi.org/project/selenium/
