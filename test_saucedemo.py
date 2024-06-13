import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver_init")
class TestSauceDemo:
    @allure.step("Login with valid credentials")
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in self.driver.current_url

    @allure.step("Login with invalid credentials")
    def test_login_invalid(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login("invalid_user", "invalid_pass")
        assert "login" in self.driver.current_url

    @allure.step("Sort products from low to high and assert prices")
    def test_sort_and_assert_product_prices(self):
        products_page = ProductsPage(self.driver)
        products_page.sort_products_low_to_high()
        prices = products_page.get_product_prices()
        assert prices == sorted(prices)

    @allure.step("Add product to cart and assert button text")
    def test_add_to_cart(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(0)
        assert products_page.get_cart_button_text(0) == "REMOVE"

    @allure.step("Go to cart and assert product details")
    def test_go_to_cart_and_assert(self):
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        
        product_price = products_page.get_product_prices()[0]
        products_page.add_to_cart(0)
        products_page.go_to_cart()
        
        assert cart_page.get_item_price(0) == product_price
        assert cart_page.get_item_name(0) == "Sauce Labs Backpack"

    @allure.step("Proceed to checkout and verify error message")
    def test_checkout_and_verify_error(self):
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        cart_page.go_to_checkout()
        checkout_page.fill_details("", "Doe", "12345")
        assert "Error: First Name is required" in checkout_page.get_error_message()
