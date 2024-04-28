from types import TracebackType
from typing import Type
import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    
    def open_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(15)
        self.maximize_window()