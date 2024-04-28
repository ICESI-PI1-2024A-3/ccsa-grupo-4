import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.implicitly_wait(3) #Para esperar 3 segundos implícitos
user = driver.find_element(By.NAME,"username")
user.send_keys("daron")
password = driver.find_element(By.NAME,"password")
password.send_keys("daron123")
loginButton = driver.find_element(By.CLASS_NAME,"btn-primary")
loginButton.click()
input("input de prueba para que no se cierra instantaneamete")