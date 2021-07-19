from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\annuk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.linkedin.com")
driver.maximize_window()


driver.find_element(By.ID,"session_key").clear()
driver.find_element(By.ID,"session_key").send_keys("annukumari3628@gmail.com")
driver.find_element(By.ID,"session_password").clear()
driver.find_element(By.ID,"session_password").send_keys("!@#$%^&*(")
driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()
time.sleep(1)


driver.find_element(By.CLASS_NAME,"btn__primary--large").click()

driver.get("https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit")
#assert feed in driver.current_url
driver.find_element(By.ID,"ember22").click()

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

acceptButton = []
while len(acceptButton)==0:
    acceptButton=driver.find_elements(By.XPATH,"//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")


for button in acceptButton:
    button.click()
    time.sleep(5)


driver.quit()