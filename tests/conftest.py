import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.confreader import confread
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup(request):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver=driver
    driver.get(confread('basic_info', 'HomePageURL'))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()