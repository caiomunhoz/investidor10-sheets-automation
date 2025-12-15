from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)

    def get_url(self):
        self.driver.get(self.url)
    
    def url_to_be(self, new_url):
        return self.wait.until(EC.url_to_be(new_url))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text, clear=False):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        if clear:
            element.clear()
        
        element.send_keys(text)