import time
from selenium.webdriver.common.by import By


def test_homepage(driver):
    driver.get('https://www.great.gov.uk/')
    driver.find_element(By.LINK_TEXT, 'Accept all cookies').click()
    h1_element = driver.find_element(By.TAG_NAME, 'h1')
    assert 'MADE in the UK\nSOLD \nto\n the\n world' in h1_element.text
