import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_login_nop_shop:

    @pytest.mark.login
    def test_login_with_valid_credentials(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("stone1234")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

    @pytest.mark.login
    def test_login_with_invalid_password(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("22222")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        error_msg = driver.find_element(By.XPATH, "(//div[@class='message-error validation-summary-errors'])[1]").text
        assert error_msg == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer account "
                             "found")

    @pytest.mark.login
    def test_login_with_invalid_email(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone11111@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("stone1234")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        error_msg = driver.find_element(By.XPATH, "(//div[@class='message-error validation-summary-errors'])[1]").text
        assert error_msg == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer account "
                             "found")

    @pytest.mark.login
    def test_login_forgot_password_link(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        link = driver.find_element(By.XPATH, "(//a[normalize-space()='Forgot password?'])[1]").click()
        confirmation = driver.find_element(By.XPATH, "(//p[@class='tooltip'])[1]").text
        assert confirmation == "Please enter your email address below. You will receive a link to reset your password."

    @pytest.mark.login
    def test_login_case_sensitivity(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("STONE@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("STONE1234")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        error_msg = driver.find_element(By.XPATH, "(//div[@class='message-error validation-summary-errors'])[1]").text
        assert error_msg == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer account "
                             "found")

    @pytest.mark.login
    def test_login_blank_email(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        password = driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("stone1234")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        email_error_msg = driver.find_element(By.XPATH, "(//span[@id='Email-error'])[1]").text
        assert email_error_msg == "Please enter your email"

    @pytest.mark.one
    @pytest.mark.login
    def test_login_blank_password(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        login = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]").click()
        email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("stone@gmail.com")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()
        error_msg = driver.find_element(By.XPATH, "(//div[@class='message-error validation-summary-errors'])[1]").text
        assert error_msg == ("Login was unsuccessful. Please correct the errors and try again.\nNo customer account "
                             "found")

        