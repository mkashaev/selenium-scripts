import os 
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_css_selector("[name=firstname]")
first_name.send_keys("Marat")

last_name = browser.find_element_by_css_selector("[name=lastname]")
last_name.send_keys("Taram")

email = browser.find_element_by_css_selector("[name=email]")
email.send_keys("123@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'article.txt')           # добавляем к этому пути имя файла 

element = browser.find_element_by_css_selector("[type=file]")
element.send_keys(file_path)

browser.find_element_by_tag_name("button").click()

