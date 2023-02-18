from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

class ContextMenuPage:
    #locators
    BOX = (By.CSS_SELECTOR, '[oncontextmenu="displayMessage()"]')


    # URL
    URL = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def open_menu(self):
        actions = ActionChains(self.browser)
        actions.context_click(self.browser.find_element(*self.BOX)).perform()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()