from selenium.webdriver.common.by import By
from .base import BasePage

class WalletPage(BasePage):
    ADD_ENTRIES_BUTTON = (By.XPATH, '//button[.//label[normalize-space()="Adicionar Lançamento"]]')

    def open_entry_form(self):
        self.click(self.ADD_ENTRIES_BUTTON)

    def add_entry(self, entry):
        return self.driver.execute_script(
            '''
            const payload = arguments[0]
            
            return fetch ("/wallet/api/proxy/wallet-app/entry/store", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            })
            .then(async response => {
                return {
                    status: response.status,
                    ok: response.ok,
                    body: await response.text()
                };
            })
            .catch(error => {
                return {
                    status: -1,
                    error: error.toString()
                };
            });
            ''', entry)
