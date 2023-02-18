import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot():
#     return driver.get_screenshot_as_base64()
#

@pytest.fixture
def browser():
#     before tests
#     global driver
    options = Options()
#pt rulare fara sa se deschida comanda de chrome
    # options.add_argument('--headless')
    # driver = selenium.webdriver.Chrome(service=Service(Geko().install()), chrome_options=options)
#pt rulare firefox
    driver = selenium.webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver = selenium.webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
#     quit driver ; after tests
    driver.quit()
    return driver