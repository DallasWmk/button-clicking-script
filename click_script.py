from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://tryhackme.com/subscriptions')
time.sleep(5)
balance = browser.find_element_by_xpath("//span[@id='sub-no']")
button = browser.find_element_by_xpath("//button[@class='button-plus sub-colors']")

for i in range(10000000):
    button.click()
