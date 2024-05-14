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

    def test_checklist(self):
        #login
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("daron")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("daron12345")
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logístico")

        event = self.driver.find_element(By.XPATH, "//a[contains(@href, '/event/checklist/17')]")
        event.click()
        text_expected = self.driver.find_element(By.XPATH, "/html/body/section/div/div/h1")
        self.assertEqual(text_expected.text, "Detalles del Evento")

if __name__ == "__main__":
    unittest.main()