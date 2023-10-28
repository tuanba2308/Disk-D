from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.get("https://korean.dict.naver.com/kovidict/#/search?query=%EA%B0%80%EB%8B%A4")
# time.sleep(2)
# mean=driver.find_elements(By.CLASS_NAME, "mean")[0].find_elements(By.CLASS_NAME, "word_class")[0].text
try:
    mean=driver.find_elements(By.CLASS_NAME, "mean")[0].get_attribute("innerText").split()[1] #it worked
    print(mean)
except:
    print("An exception occurred") 
driver.quit()

