from selenium.webdriver.common.by import By
from .base import BasePage

class WalletPage(BasePage):
    ADD_ENTRIES_BUTTON = (By.XPATH, '//button[.//label[normalize-space()="Adicionar Lançamento"]]')

    def open_entry_form(self):
        self.click(self.ADD_ENTRIES_BUTTON)
