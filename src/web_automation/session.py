from .browser import create_browser

class WebSession:
    def __enter__(self):
        self.driver = create_browser()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()
        return