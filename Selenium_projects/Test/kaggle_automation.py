# This script automates the query of the kaggle page in search of the pandas course
import time
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class KagglePandasTest(unittest.TestCase):

    def setUp(self):
        """Start the browser session before running the test"""
        self.driver = webdriver.Chrome(executable_path='/home/PycharmProjects/drivers/chromedriver')
        driver = self.driver
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get('https://www.kaggle.com/')

    # verify that the name of the search icon of kaggle exists
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, '#site-container > div > div.sc-pAwOa.sc-oUMOe.kuByUO > div.sc-qPVvu.Irslq > div.sc-pssnI.fGcBXN.sc-pCOPB.fefpln'))

    def test_search_course(self):
        driver = self.driver

        # search bar is identified to enter pandas
        item_search = driver.find_element_by_xpath('//*[@id="site-container"]/div/div[1]/div[2]/div[1]/p').click()
        search_field = driver.find_element_by_xpath('//*[@id="site-container"]/div/div[3]/div[1]/div/div[1]/form/input')
        search_field.clear()
        search_field.send_keys('pandas')
        search_field.submit()

        # the section of courses is identified and the course of pandas is selected
        courses = driver.find_element_by_xpath('//*[@id="site-container"]/div/div[3]/div[2]/div/div/div[1]/div/div[1]/div/button[8]/div/div/p')
        courses.click()
        pandas_course = driver.find_element_by_partial_link_text('Pandas')
        pandas_course.click()
        time.sleep(3)

    def is_element_present(self, how, what):
        """ Identify when an element is present according to the parameters: how=selector, what=value"""
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

    def tearDown(self):
        """Is used to cleanly exit it when the test has completed"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    #unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='reporte_kaggle_pandas'))