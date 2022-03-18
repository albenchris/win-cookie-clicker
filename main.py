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

count = 0


def buy_product():
    products = [
        driver.find_element(
            By.ID,
            "productPrice" + str(i)
        ) for i in range(1, -1, -1)
    ]
    for product in products:
        value = int(product.text)
        if value <= count:
            # print("products", products)
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(product)
            upgrade_actions.click()
            upgrade_actions.perform()


def buy_upgrade():
    if count > 100:
        upgrades = [
            driver.find_element(
                By.ID,
                "upgrade" + str(i)
            ) for i in range(1, -1, -1)
        ]

        for upgrade in upgrades:
            # print("upgrades", upgrades)
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(upgrade)
            upgrade_actions.click()
            upgrade_actions.perform()


def click_golden_cookie():
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
    finally:
        print("", end="")


while count < 500:
    actions.click(cookie)

    buy_product()
    buy_upgrade()
    # click_golden_cookie()

    actions.perform()
    count = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])

    # if keyboard.is_pressed("q"):
    #     driver.quit()

sleep(2)
driver.quit()
