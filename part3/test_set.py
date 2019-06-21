import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test(unittest.TestCase):
    def test_1(self):
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

        self.assertEqual(
            welcome_text, 
            "Поздравляем! Вы успешно зарегистировались!", 
            f"{welcome_text} should be 'Поздравляем! Вы успешно зарегистировались!'")

    def test_2(self):
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

        self.assertEqual(
            welcome_text, 
            "Поздравляем! Вы успешно зарегистировались!", 
            f"{welcome_text} should be 'Поздравляем! Вы успешно зарегистировались!'")
      



if __name__ == '__main__':
  unittest.main()