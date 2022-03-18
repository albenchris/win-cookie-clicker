# Created by Alex Christopherson on March 17, 2022
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import keyboard

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

actions = ActionChains(driver)

cookie = driver.find_element(By.ID, "bigCookie")


# Created by Alex Christopherson on March 17, 2022
# Modified by Alex Christopherson on March 18, 2022
def buy_upgrade():
    driver.implicitly_wait(0)
    
    try:
        upgrades = driver.find_elements(By.CLASS_NAME, "upgrade")
        for u in upgrades:
            if u.get_attribute("class").__contains__("enabled"):
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(u)
                upgrade_actions.click()
                upgrade_actions.perform()
    except Exception as e:
        print("", end="")

    products = driver.find_elements(By.CLASS_NAME, "product")
    for p in products:
        if p.get_attribute("class").__contains__("enabled"):
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(p)
            upgrade_actions.click()
            upgrade_actions.perform()


# Created by Alex Christopherson on March 17, 2022
# Modified by Alex Christopherson on March 18, 2022
def click_golden_cookie():
    driver.implicitly_wait(0)
    try:
        golden_cookie = driver.find_element(By.CLASS_NAME, "shimmer")
        if golden_cookie.is_displayed():
            print("found golden cookie")
            golden_actions = ActionChains(driver)
            golden_actions.move_to_element(golden_cookie)
            golden_actions.click()
            golden_actions.perform()
    except Exception as e:
        print("", end="")


playing = True

while playing:
    actions.click(cookie)
    actions.double_click(cookie)

    click_golden_cookie()

    buy_upgrade()

    actions.perform()

    if keyboard.is_pressed("q"):
        playing = False

sleep(2)
driver.quit()
