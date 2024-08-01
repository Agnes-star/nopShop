import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_Functional_nop_shop:

    @pytest.mark.home_page
    def test_home_page_loading_succesfully(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        title = driver.title
        assert title == "nopCommerce demo store"

    @pytest.mark.home_page
    def test_sign_in_works(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        sign_in = driver.find_element(By.XPATH, "(//a[normalize-space()='Log in'])[1]")
        sign_in.click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Welcome, Please Sign In!'])[1]").text
        assert confirmation == "Welcome, Please Sign In!"

    @pytest.mark.home_page
    def test_sign_up_works(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        sign_up = driver.find_element(By.XPATH, "(//a[normalize-space()='Register'])[1]")
        sign_up.click()
        confirmation = driver.find_element(By.CSS_SELECTOR, "div[class='page-title'] h1").text
        assert confirmation == "Register"

    @pytest.mark.home_page
    def test_product_category_display(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        computers_category = driver.find_element(By.XPATH, "(//a[normalize-space()='Computers'])[1]")
        assert computers_category.is_displayed()

    @pytest.mark.home_page
    def test_product_details_open_after_click(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        search_input = driver.find_element(By.XPATH, "(//input[@id='small-searchterms'])[1]")
        search_input.send_keys("Lenovo IdeaCentre 600 All-in-One PC")
        driver.find_element(By.XPATH, "(//button[@class='button-1 search-box-button'])[1]").click()
        computers_lenovo = driver.find_element(By.CSS_SELECTOR, "h2[class='product-title'] a").click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Lenovo IdeaCentre 600 All-in-One "
                                                     "PC'])[1]").text
        assert confirmation == "Lenovo IdeaCentre 600 All-in-One PC"

    @pytest.mark.home_page
    def test_product_added_to_cart(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        search_input = driver.find_element(By.XPATH, "(//input[@id='small-searchterms'])[1]")
        search_input.send_keys("Lenovo IdeaCentre 600 All-in-One PC")
        driver.find_element(By.XPATH, "(//button[@class='button-1 search-box-button'])[1]").click()
        computers_lenovo = driver.find_element(By.CSS_SELECTOR, "h2[class='product-title'] a").click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Lenovo IdeaCentre 600 All-in-One "
                                                     "PC'])[1]").text
        assert confirmation == "Lenovo IdeaCentre 600 All-in-One PC"
        add_to_cart = driver.find_element(By.XPATH, "(//button[normalize-space()='Add to cart'])[1]")
        add_to_cart.click()
        add_cart_confirmation = driver.find_element(By.CSS_SELECTOR, ".bar-notification.success").text
        assert add_cart_confirmation == "The product has been added to your shopping cart"

    @pytest.mark.home_page
    def test_shopping_cart_icon_works(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        shopping_cart_element = driver.find_element(By.CSS_SELECTOR, ".cart-label")
        shopping_cart_element.click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Shopping cart'])[1]").text
        assert confirmation == "Shopping cart"

    @pytest.mark.home_page
    def test_remove_from_cart_btn(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        search_input = driver.find_element(By.XPATH, "(//input[@id='small-searchterms'])[1]")
        search_input.send_keys("Lenovo IdeaCentre 600 All-in-One PC")
        driver.find_element(By.XPATH, "(//button[@class='button-1 search-box-button'])[1]").click()
        computers_lenovo = driver.find_element(By.CSS_SELECTOR, "h2[class='product-title'] a").click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Lenovo IdeaCentre 600 All-in-One "
                                                     "PC'])[1]").text
        assert confirmation == "Lenovo IdeaCentre 600 All-in-One PC"
        add_to_cart = driver.find_element(By.XPATH, "(//button[normalize-space()='Add to cart'])[1]")
        add_to_cart.click()
        driver.find_element(By.XPATH, "(//span[@class='cart-label'])[1]").click()
        remove_from_cart_btn = driver.find_element(By.XPATH, "(//button[@class='remove-btn'])[1]")
        remove_from_cart_btn.click()
        remove_btn_confirmation = driver.find_element(By.XPATH, "(//div[@class='no-data'])[1]").text
        assert remove_btn_confirmation == "Your Shopping Cart is empty!"

    @pytest.mark.actual
    @pytest.mark.home_page
    def test_product_display_reviews(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        search_input = driver.find_element(By.XPATH, "(//input[@id='small-searchterms'])[1]")
        search_input.send_keys("Build your own computer")
        driver.find_element(By.XPATH, "(//button[@class='button-1 search-box-button'])[1]").click()
        computer = driver.find_element(By.CSS_SELECTOR, "h2[class='product-title'] a").click()
        reviews = driver.find_element(By.XPATH, "(//a[normalize-space()='1 review(s)'])[1]").click()
        confirmation = driver.find_element(By.XPATH, "(//strong[normalize-space()='Existing reviews'])[1]").text
        assert confirmation == "Existing reviews"
