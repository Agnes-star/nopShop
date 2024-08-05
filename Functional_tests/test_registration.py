import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_registration_nop_shop:

    @pytest.mark.registration
    def test_registration_with_valid_credentials(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        register = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        female = driver.find_element(By.XPATH, "(//input[@id='gender-female'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthDay'])[1]")
        day = Select(dropdown_element)
        day.select_by_visible_text("5")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthMonth'])[1]")
        month = Select(dropdown_element)
        month.select_by_index(4)

        dropdown_element = driver.find_element(By.XPATH, "(// select[@ name='DateOfBirthYear'])[1]")
        year = Select(dropdown_element)
        year.select_by_value("2000")

        email = driver.find_element(By.XPATH, "(//input[@id='Email'])[1]").send_keys("test2222@gmail.com")
        password = driver.find_element(By.XPATH, "(//input[@id='Password'])[1]").send_keys("test3333")
        confirm_password = driver.find_element(By.XPATH, "(//input[@id='ConfirmPassword'])[1]").send_keys("test3333")
        register_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]").click()

    @pytest.mark.registration
    def test_negative_registration_with_missing_fields(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        registration = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        male = driver.find_element(By.XPATH, "(//input[@id='gender-female'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthDay'])[1]")
        day = Select(dropdown_element)
        day.select_by_visible_text("5")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthMonth'])[1]")
        month = Select(dropdown_element)
        month.select_by_index(4)

        dropdown_element = driver.find_element(By.XPATH, "(// select[@ name='DateOfBirthYear'])[1]")
        year = Select(dropdown_element)
        year.select_by_value("2000")
        register_btn = driver.find_element(By.CSS_SELECTOR, "#register-button").click()
        confirmation = driver.find_element(By.XPATH, "(//div[@class='result'])[1]").text
        assert confirmation == "Your registration completed"

    @pytest.mark.registration
    def test_negative_error_msg_when_registration_fails(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        registration = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        male = driver.find_element(By.XPATH, "(//input[@id='gender-female'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthDay'])[1]")
        day = Select(dropdown_element)
        day.select_by_visible_text("5")

        dropdown_element = driver.find_element(By.XPATH, "(//select[@name='DateOfBirthMonth'])[1]")
        month = Select(dropdown_element)
        month.select_by_index(4)

        dropdown_element = driver.find_element(By.XPATH, "(// select[@ name='DateOfBirthYear'])[1]")
        year = Select(dropdown_element)
        year.select_by_value("2000")
        register_btn = driver.find_element(By.CSS_SELECTOR, "#register-button").click()

        email_error_msg = driver.find_element(By.XPATH, "(//span[@id='Email-error'])[1]").text
        assert email_error_msg == "Email is required."

        password_error_msg = driver.find_element(By.XPATH, "(//span[@id='ConfirmPassword-error'])[1]").text
        assert password_error_msg == "Password is required."

    @pytest.mark.registration
    def test_registration_with_pre_existing_credentials(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        register = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        email = driver.find_element(By.XPATH, "(//input[@id='Email'])[1]").send_keys("test2222@gmail.com")
        password = driver.find_element(By.XPATH, "(//input[@id='Password'])[1]").send_keys("test3333")
        confirm_password = driver.find_element(By.XPATH, "(//input[@id='ConfirmPassword'])[1]").send_keys("test3333")
        register_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]").click()

        error_msg = driver.find_element(By.XPATH,
                                        "(//li[normalize-space()='The specified email already exists'])[1]").text
        assert error_msg == "The specified email already exists"

    @pytest.mark.registration
    def test_negative_incorrect_email(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        register = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        email = driver.find_element(By.XPATH, "(//input[@id='Email'])[1]").send_keys("test.com")
        password = driver.find_element(By.XPATH, "(//input[@id='Password'])[1]").send_keys("test3333")
        confirm_password = driver.find_element(By.XPATH, "(//input[@id='ConfirmPassword'])[1]").send_keys(
            "test3333")
        register_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]").click()
        error_msg = driver.find_element(By.XPATH, "(//span[@id='Email-error'])[1]").text
        assert error_msg == "Please enter a valid email address."

    @pytest.mark.current
    @pytest.mark.registration
    def test_redirection_after_successful_registration(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        register = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]").click()
        first_name = driver.find_element(By.XPATH, "(//input[@id='FirstName'])[1]").send_keys("Lilly")
        last_name = driver.find_element(By.XPATH, "(//input[@id='LastName'])[1]").send_keys("Blue")

        email = driver.find_element(By.XPATH, "(//input[@id='Email'])[1]").send_keys("testing888@gmail.com")
        password = driver.find_element(By.XPATH, "(//input[@id='Password'])[1]").send_keys("test3333")
        confirm_password = driver.find_element(By.XPATH, "(//input[@id='ConfirmPassword'])[1]").send_keys(
            "test3333")
        register_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]").click()
        confirmation = driver.find_element(By.XPATH, "(//div[@class='result'])[1]").text
        assert confirmation == "Your registration completed"

    # confirmation = driver.find_element(By.XPATH, "(//div[@class='result'])[1]").text
    # assert confirmation == "Your registration completed"
