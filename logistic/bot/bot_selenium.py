# pragma: no cover
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import constants as const

class bot_selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(const.BASE_URL)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(const.USER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(const.PASSWORD)
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logístico")

    def test_create_delete_event(self):
        #primero hacemos login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(const.USER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(const.PASSWORD)
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()

        #Assert del login
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

        #Creaamos el evento
        burguer = self.driver.find_element(By.XPATH, "/html/body/section/nav/header/img")
        burguer.click()
        create_event = self.driver.find_element(By.XPATH, "/html/body/section/nav/div/div[1]/ul/div/li[2]/a/span")
        create_event.click()
        event_name = self.driver.find_element(By.NAME, "name")
        event_name.send_keys("Evento selenium web Driver")
        delta_time = self.driver.find_element(By.XPATH, "//*[@id='id_executionDate']")
        delta_time.send_keys("29042024\t1200a")
        event_place = self.driver.find_element(By.XPATH, "//*[@id='id_place']")
        event_place.send_keys("Hall de auditorios")
        event_progress = self.driver.find_element(By.XPATH, "//*[@id='id_progress']")
        event_progress.send_keys("0")
        delta_time_fin = self.driver.find_element(By.XPATH, "//*[@id='id_finishDate']")
        delta_time_fin.send_keys("30042024\t1200a")
        event_user = self.driver.find_element(By.XPATH, "//*[@id='id_user']")
        event_user.send_keys("da")
        save_button = self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/button")
        save_button.click()

        #Borramos el evento
       
        event_edit = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/754/')]")
        event_edit.click()
        delete_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/button[2]")
        delete_button.click()

        #Assert
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")


    def test_delete_and_check(self):
        #login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(const.USER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(const.PASSWORD)
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

        #Borramos el evento
        event_edit = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/30/')]")######
        event_edit.click()
        delete_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/button[2]")
        delete_button.click()

        #miramos el historial
        burguer = self.driver.find_element(By.XPATH, "/html/body/section/nav/header/img")
        burguer.click()
        history = self.driver.find_element(By.XPATH, "/html/body/section/nav/div/div[1]/ul/div/li[5]/a/span")
        history.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div/div/h1')
        self.assertEqual(text_expected.text, "Historial De Eventos Eliminados")

    def test_checklist(self):
        #login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(const.USER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(const.PASSWORD)
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logístico")

        event = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/checklist/17')]")
        event.click()
        text_expected = self.driver.find_element(By.XPATH, "/html/body/section/div/div/h1")
        self.assertEqual(text_expected.text, "Detalles del Evento")
    
    def test_Calendar(self):
        #login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(const.USER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(const.PASSWORD)
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logístico")

        burguer = self.driver.find_element(By.XPATH, "/html/body/section/nav/header/img")
        burguer.click()
        calendar = self.driver.find_element(By.XPATH, "/html/body/section/nav/div/div[1]/ul/div/li[4]/a/span")
        calendar.click()
        text_expected = self.driver.find_element(By.ID, "fc-dom-1")
        self.assertEqual(text_expected.text, "mayo de 2024")


if __name__ == "__main__":
    unittest.main()
