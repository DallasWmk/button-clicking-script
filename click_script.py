from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

#browser selected is Chrome
browser = webdriver.Chrome(ChromeDriverManager().install())

#initalize webpage 
browser.get('REPLACE WITH WEBSITE URL')

#wait for webpage to fully load 
time.sleep(5)

#initialize the button xpath based on the website HTML
button = browser.find_element_by_xpath("REPLACE WITH BUTTON XPATH FROM WEBPAGE")

#click button 10 mil times
for i in range(10000000):
    button.click()
