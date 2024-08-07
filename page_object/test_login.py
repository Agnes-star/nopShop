from selenium import webdriver
from login_page_objects import Login_page


class Test_login:
    def test_login(self,driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()

        self.lp = Login_page(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()

        self.act_title = self.driver.title
        self.driver.close()
        assert self.act_title == "Dashboard / nopCommerce administration"


