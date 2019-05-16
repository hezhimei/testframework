import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome(
        executable_path='/Users/a123/Downloads/testframework-master/excise/driver/chromedriver')

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver
