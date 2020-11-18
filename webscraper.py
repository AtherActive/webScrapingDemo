from selenium import webdriver
from time import sleep

url = 'https://www.youtube.com/c/KalleHallden/videos'
browser = webdriver.Chrome()
browser.get(url)
sleep(5)
browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
