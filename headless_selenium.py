from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


my_chromedriver_path = r"C:\webdrivers\chromedriver\chromedriver.exe"
my_chromedriver_path = '/home/nubonix/webdrivers/chrome/chromedriver'

options = Options()
#options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument('--start-maximized')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path=my_chromedriver_path )

url = "https://www.google.com"

driver.get(url)

my_variable0 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "my whatever xpath")))

my_variable1 = WebDriverWait(driver, 10)\
    .until(EC.presence_of_element_located((By.LINK_TEXT,
                                           "what a person sees as as the href, or the actual text of the link")))

my_variable2 = WebDriverWait(driver, 10)\
    .until(EC.presence_of_element_located((By.CSS_SELECTOR, "my whatever css_selector")))


my_variable3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "my whatever partial text")))
