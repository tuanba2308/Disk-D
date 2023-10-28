from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# use selenium to get meaning of a word, in this example 가다 -> đi
# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://korean.dict.naver.com/kovidict/#/search?query=가")

#     title = driver.title
#     assert title == "Web form"

#     driver.implicitly_wait(0.5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
    
#     return value

# test_eight_components()

driver = webdriver.Chrome()
driver.get("https://korean.dict.naver.com/kovidict/#/search?query=가")
time.sleep(2)
# mean=driver.find_elements(By.CLASS_NAME, "mean")[0].find_elements(By.CLASS_NAME, "word_class")[0].text
# mean=driver.find_elements(By.CLASS_NAME, "mean")[0].get_attribute("innerText").split()[1:] #it worked
mean=driver.find_elements(By.CLASS_NAME, "highlight")[0].get_attribute("innerText") #it worked
print(' '.join(mean)),