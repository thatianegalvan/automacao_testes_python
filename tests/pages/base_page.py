from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text
    
    def is_displayed(self, by, value):
        return self.find(by, value).is_displayed()

    def select_dropdown_by_visible_text(self, by, value, text):
        from selenium.webdriver.support.ui import Select
        select_element = self.find(by, value)
        select = Select(select_element)
        select.select_by_visible_text(text)


def Eelement_to_be_clickable(by, value):
    """Create a Selenium condition for an element that is ready to be clicked."""
    from selenium.webdriver.support import expected_conditions as EC

    return EC.element_to_be_clickable((by, value))