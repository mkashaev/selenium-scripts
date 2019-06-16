from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

img = browser.find_element_by_id("treasure")
x = img.get_attribute("valuex")

# x_element = browser.find_element_by_id("input_value")
# x = x_element.text
y = calc(x)

inputForm = browser.find_element(By.ID, "answer")
inputForm.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()

submitButton = browser.find_element_by_css_selector("[type='submit']")
submitButton.click()