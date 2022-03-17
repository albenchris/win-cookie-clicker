
# Created by Alex Christopherson on March 17, 2022

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")


sleep(2)

driver.quit()


