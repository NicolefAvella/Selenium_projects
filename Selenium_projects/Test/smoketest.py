# Test suit file, main file to run test files
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from kaggle_automation import KagglePandasTest
from navigation_datasets import NavigationTest
from register_new_user import LoginUserTest

# load test cases
kaggle_automation = TestLoader().loadTestsFromTestCase(KagglePandasTest)
navigation_datasets = TestLoader().loadTestsFromTestCase(NavigationTest)
register_new_user = TestLoader().loadTestsFromTestCase(LoginUserTest)

# build the test suit
smoke_test = TestSuite([navigation_datasets, register_new_user, kaggle_automation])

kwargs = {
    "output": 'reports2'
}

# generate report and run
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

