from selenium.webdriver.common.by import By

class AlertsPage:
    ALERT = (By.CSS_SELECTOR, '[onclick="jsAlert()"]')
    CONFIRM = (By.CSS_SELECTOR, '[onclick="jsConfirm()"]')
    PROMPT = (By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    RESULT_TEXT = (By.ID, 'result')

    # URL
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def open_alert(self):
        self.browser.find_element(*self.ALERT).click()

    def open_confirm(self):
        self.browser.find_element(*self.CONFIRM).click()

    def open_promt(self):
        self.browser.find_element(*self.PROMPT).click()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def cancel_alert(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def insert_text_in_alert(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)

    def get_text_from_result(self):
        return self.browser.find_element(*self.RESULT_TEXT).text