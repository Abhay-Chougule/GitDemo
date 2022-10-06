from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_Name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\abhay.chougule\\Documents\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("C:\\Users\\abhay.chougule\\Documents\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    else:
        service_obj = Service("C:\\Users\\abhay.chougule\\Documents\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the Pytest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace(":", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height=228px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# "C:/Users/abhay.chougule/PycharmProjects/PythonSelfFramework"