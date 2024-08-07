from selenium.webdriver.common.by import By


class Login_page:
    # locators
    login_click_xpath = "(//a[normalize-space()='Log in'])[1]"
    txtbox_email_css = "#Email"
    txtbox_password_xpath = "(//input[@id='Password'])[1]"
    button_login_xpath = "(//button[normalize-space()='Log in'])[1]"
    error_msg_xpath = "//div[@class='message-error validation-summary-errors']"
    email_error_msg_xpath = "(//span[@id='Email-error'])[1]"
    error_password_recovery = "(//p[@class='tooltip'])[1]"
    forgot_password_link = "(//a[normalize-space()='Forgot password?'])[1]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_click_xpath).click()

    def setEmail(self, email):
        emailtxt = self.driver.find_element(By.CSS_SELECTOR, self.txtbox_email_css)
        emailtxt.clear()
        emailtxt.send_keys(email)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.XPATH, self.txtbox_password_xpath)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def loginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def errorMessage(self):
        return self.driver.find_element(By.XPATH, self.error_msg_xpath).text

    def emailErrorMessage(self):
        return self.driver.find_element(By.XPATH, self.email_error_msg_xpath).text

    def forgotPasswordLink(self):
        self.driver.find_element(By.XPATH, self.forgot_password_link).click()

    def passwordRecovery(self):
        return self.driver.find_element(By.XPATH, self.error_password_recovery).text
