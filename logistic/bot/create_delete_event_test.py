import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import constants as const

class create_delete_event(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(const.BASE_URL)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_create_delete_event(self):
        #primero hacemos login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("daron")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("daron123")
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()

        #Assert del login
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

        #Creaamos el evento
        create_event = self.driver.find_element(By.XPATH, "/html/body/section/nav/div/div[1]/ul/li[2]/a/img")
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
        event_edit = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/31/')]")
        event_edit.click()
        delete_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/button[2]")
        delete_button.click()

        #Assert
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")


    def test_delete_and_check(self):
        #login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("daron")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("daron123")
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

        #Borramos el evento
        event_edit = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/30/')]")
        event_edit.click()
        delete_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/button[2]")
        delete_button.click()

        #miramos el historial
        history = self.driver.find_element(By.XPATH, "/html/body/section/nav/div/div[1]/ul/li[5]/a/img")
        history.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/div/div/h1')
        self.assertEqual(text_expected.text, "Historic Deleted Events")

if __name__ == "__main__":
    unittest.main()
