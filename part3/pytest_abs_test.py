
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


success_output = "Поздравляем! Вы успешно зарегистировались!"

def test_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    inputFirstName = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
    inputFirstName.send_keys("Ivan")

    inputLastName = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
    inputLastName.send_keys("Nav")

    inputEmail = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
    inputEmail.send_keys("mail@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text

    assert welcome_text == success_output, f"{welcome_text} should be '{success_output}'"

def test_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    inputFirstName = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
    inputFirstName.send_keys("Ivan")

    inputLastName = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
    inputLastName.send_keys("Nav")

    inputEmail = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
    inputEmail.send_keys("mail@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text

    assert welcome_text == success_output, f"{welcome_text} should be '{success_output}'"


if __name__ == '__main__':
    test_1()
    test_2()