from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

first_elem = browser.find_element_by_id("num1").text
second_elem = browser.find_element_by_id("num2").text


sum_elem = int(first_elem) + int(second_elem)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum_elem))

browser.find_element_by_tag_name("button").click()

