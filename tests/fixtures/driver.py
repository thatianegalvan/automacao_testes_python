from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()
    yield driver

    driver.quit()