from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name("button").click()

browser.switch_to.window(browser.window_handles[1])

input_value = browser.find_element_by_id("input_value").text
input_filed = browser.find_element_by_id("answer")
input_filed.send_keys(calc(input_value))

browser.find_element_by_tag_name("button").click()