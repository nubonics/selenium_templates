import getpass
import platform

from glob import glob
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

username = getpass.getuser()
if platform.system() == 'linux':
    gecko_driver_path = f'/home/{username}/webdrivers/firefox/geckodriver'
    profile_path = "/home/{username}/.mozilla/firefox/or2171cc.recaptcha"
if platform.system() == 'windows':
    gecko_driver_path = f'C:/Users/{username}/webdrivers/geckodriver/geckodriver.exe'
    profile_path = glob("%APPDATA%/Mozilla/Firefox/Profiles/*.recaptcha")[0]
else:
    raise Exception('Could not detect operating system')

options = Options()
options.add_argument("-profile")
options.add_argument(profile_path)
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

driver.get('about:profiles')