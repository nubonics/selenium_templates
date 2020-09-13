import getpass

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import DesiredCapabilities

username = getpass.getuser()
gecko_driver_path = '/home/nubonix/webdrivers/firefox/geckodriver'
options = Options()
options.add_argument("-profile")
options.add_argument(f"/home/{username}/.mozilla/firefox/or2171cc.recaptcha")
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
# driver = webdriver.Firefox(executable_path=gecko_driver_path, capabilities=firefox_capabilities, options=options)
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

driver.get('about:profiles')