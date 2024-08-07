from selenium.webdriver.common.by import By


class Login_page:
    # locators
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    button_login_xpath = "(//button[normalize-space()='Log in'])[1]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
