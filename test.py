from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://lms.uibk.ac.at/Shibboleth.sso/Login?SAMLDS=1&target=https://lms.uibk.ac.at/shib/&entityID=https%3A%2F%2Fidp.uibk.ac.at%2Fidp%2Fshibboleth")
username = driver.find_element("name", "j_username")
username.clear()
username.send_keys("csba3598")
password = driver.find_element("name", "j_password")
password.clear()
password.send_keys("tuberi25")
driver.find_element("name", "_eventId_proceed").click()

driver.find_element(By.LINK_TEXT, "Kurse").click()
tbody = driver.find_element(By.TAG_NAME, "tbody")
print(tbody.text)

driver.quit()
