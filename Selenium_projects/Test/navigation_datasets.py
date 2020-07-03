# The script automates the navigation of a website
import time
import unittest
from selenium import webdriver


class NavigationTest(unittest.TestCase):

    def setUp(self):
        """Start the browser session before running the test"""

        self.driver = webdriver.Chrome(executable_path='/home/PycharmProjects/drivers/chromedriver')
        driver = self.driver
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_navigation(self):
        driver = self.driver

        # a dataset search is performed in the google browser
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('datasets machine learning')
        search_field.submit()
        time.sleep(2)

        # page navigation and refresh the browser window
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.refresh()

    def tearDown(self):
        """Is used to cleanly exit it when the test has completed"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)