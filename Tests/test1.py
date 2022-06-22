from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Crear una sesión de Firefox

driver = webdriver.Chrome() 
options = webdriver.ChromeOptions()

# Acceder a la aplicación web
driver.get('http://127.0.0.1:5003')

def validar_login():
    #assert "Login"in driver.title

    username = driver.find_element(By.ID,"username")
    print(username)
    username.clear()
    username.send_keys("dion")

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("0")

    driver.find_element(By.ID, "submit").click()

    assert "Welcome" in driver.page_source


def login_invalido():

    username = driver.find_element(By.ID,"username")
    username.clear()
    username.send_keys("Juan Diego")

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("0")
    driver.find_element(By.ID, "submit").click()
    
    assert "Didn't work" in driver.page_source


def black_login():
    user = driver.find_element(By.NAME, 'username')

    user.send_keys('hola')

    user.submit()

    driver.find_element(By.ID, "submit").click()

    assert "No llenado" in driver.page_source


#validar_login()
#login_invalido()
black_login()