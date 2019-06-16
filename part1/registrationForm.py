from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link1)

# Ваш код, который заполняет обязательные поля
inputFirstName = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
inputFirstName.send_keys("Ivan")

inputLastName = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
inputLastName.send_keys("Nav")

inputEmail = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
inputEmail.send_keys("mail@mail.ru")


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


# input1 = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
# input3.send_keys("fake@fake.fake")