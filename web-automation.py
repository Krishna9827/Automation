from selenium import webdriver
import pyautogui
import time

time.sleep(3)

driver = webdriver.Chrome()

driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Vxol Gaming')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

time.sleep(5)
pyautogui.leftClick(945, 311, 2)


