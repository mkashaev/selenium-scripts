from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

input_value = browser.find_element_by_id("input_value").text
input_filed = browser.find_element_by_id("answer")
input_filed.send_keys(calc(input_value))

checkbox = browser.find_element_by_id("robotCheckbox").click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

radio = browser.find_element_by_id("robotsRule").click()
button.click()

