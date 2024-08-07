import pytest
from selenium import webdriver
from login_page_object import Login_page


class Test_login_nop_shop:

    @pytest.mark.login
    def test_login_with_valid_credentials(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setEmail("stone@gmail.com")
        self.loginPage.setPassword("stone1234")
        self.loginPage.loginButton()
        self.driver.quit()

        # MY OLD CODE:
        # driver.get("https://demo.nopcommerce.com/")
        # login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        # email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone@gmail.com")
        # password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("stone1234")
        # login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

    @pytest.mark.login
    def test_login_with_invalid_password(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setEmail("stone@gmail.com")
        self.loginPage.setPassword("22222")
        self.loginPage.loginButton()

        self.actual_message = self.loginPage.errorMessage()
        assert self.actual_message == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer "
                                       "account found")
        self.driver.quit()

        # MY OLD CODE:
        # driver.get("https://demo.nopcommerce.com/")
        # login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        # email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone@gmail.com")
        # password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("22222")
        # login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        # error_msg = driver.find_element(By.XPATH, "(//div[@class='message-error validation-summary-errors'])[1]").text
        # assert error_msg == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer account "
        #                      "found")

    @pytest.mark.login
    def test_login_with_invalid_email(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setEmail("stone.com")
        self.loginPage.setPassword("stone1234")
        self.loginPage.loginButton()

        self.actual_message = self.loginPage.emailErrorMessage()
        assert self.actual_message == "Please enter a valid email address."
        self.driver.quit()

    @pytest.mark.login
    def test_login_forgot_password_link(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.forgotPasswordLink()

        self.password_recovery = self.loginPage.passwordRecovery()
        assert self.password_recovery == ("Please enter your email address below. You will receive a link to reset "
                                          "your password.")
        self.driver.quit()

    @pytest.mark.login
    def test_login_case_sensitivity(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setEmail("STONE@gmail.com")
        self.loginPage.setPassword("STONE1234")
        self.loginPage.loginButton()

        self.actual_message = self.loginPage.errorMessage()
        assert self.actual_message == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer "
                                       "account found")
        self.driver.quit()

    @pytest.mark.login
    def test_login_blank_email(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setPassword("STONE1234")
        self.loginPage.loginButton()

        self.actual_message = self.loginPage.emailErrorMessage()
        assert self.actual_message == "Please enter your email"
        self.driver.quit()

    @pytest.mark.login
    def test_login_blank_password(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = Login_page(self.driver)
        self.loginPage.clickLogin()
        self.loginPage.setEmail("stone@gmail.com")
        self.loginPage.loginButton()

        self.actual_message = self.loginPage.errorMessage()
        assert self.actual_message == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer "
                                       "account found")
        self.driver.quit()
