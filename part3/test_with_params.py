
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


list_of_links = [
  "https://stepik.org/lesson/236895/step/1",
  "https://stepik.org/lesson/236896/step/1",
  "https://stepik.org/lesson/236897/step/1",
  "https://stepik.org/lesson/236898/step/1",
  "https://stepik.org/lesson/236899/step/1",
  "https://stepik.org/lesson/236903/step/1",
  "https://stepik.org/lesson/236904/step/1",
  "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', list_of_links)
def test_feedback(link):
  browser = webdriver.Chrome()
  browser.get(link)

  # WebDriverWait(browser, 10).until(EC.visibility_of_element(By.ID, "ember1625"))

  time.sleep(3)

  form = browser.find_element_by_xpath('//div[@data-type="string-quiz"]/textarea')
  answer = math.log(int(time.time()))
  form.send_keys(str(answer))

  button = browser.find_element_by_xpath('//div[@class="attempt__actions"]/button').click()

  time.sleep(2) 

  feedback = browser.find_element_by_xpath('//pre[@class="smart-hints__hint"]').text

  assert feedback == "Correct!", f"Error, {feedback}"
  print("Passed")

