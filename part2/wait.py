from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

browser.find_element_by_id("book").click()

button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

input_value = browser.find_element_by_id("input_value").text
input_filed = browser.find_element_by_id("answer")
input_filed.send_keys(calc(input_value))

button.click()