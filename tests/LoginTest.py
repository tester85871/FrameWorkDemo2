import unittest
from selenium import webdriver
import time
import sys
import os
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from pages.LoginPage import LoginPageProp
from pages.HomePage import HomePageProp
from pages.CreateUserPage import CreateUserProp

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()

    def test_a_login(self):
        loginProp=LoginPageProp()
        self.driver.find_element_by_id(loginProp.username_text_field_id).send_keys("chaitusarma99@gmail.com")
        self.driver.find_element_by_id(loginProp.password_text_field_id).send_keys("NewPass@123")
        self.driver.find_element_by_id(loginProp.login_button_id).click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:/Users/Srujan/PycharmProjects/FrameWorkDemo2/screenshots/LoginSuccess.png")


    # def test_b_createUser(self):
    #     homePage=HomePageProp()
    #     self.driver.find_element_by_xpath(homePage.create_button_xpath).click()
    #     self.driver.find_element_by_xpath(homePage.create_user_xpath).click()
    #     time.sleep(8)
    #     createUser=CreateUserProp()
    #     frame1 = self.driver.find_element_by_xpath(createUser.create_user_new_frame_xpath)
    #     self.driver.switch_to.frame(frame1)
    #     self.driver.find_element_by_id(createUser.firstname_id).send_keys("surendra firstname")
    #

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Srujan/PycharmProjects/FrameWorkDemo2/reports'),verbosity=2)
