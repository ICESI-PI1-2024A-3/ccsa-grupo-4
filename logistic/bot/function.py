import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import constants as const

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(const.BASE_URL)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("daron")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("daron123")
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

if __name__ == "__main__":
    unittest.main()
