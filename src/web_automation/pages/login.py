from selenium.webdriver.common.by import By
from config.variables import INVESTIDOR10_EMAIL, INVESTIDOR10_PASSWORD
from .base import BasePage

class LoginPage(BasePage):
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div[4]/main/section/div/div/div/div/form[1]/div[3]/input')
    
    def authenticate(self):
        self.type(self.EMAIL, INVESTIDOR10_EMAIL)
        self.type(self.PASSWORD, INVESTIDOR10_PASSWORD)
        self.click(self.SUBMIT_BUTTON)
        self.url_to_be('https://investidor10.com.br/')