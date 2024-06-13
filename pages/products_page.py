from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_select = (By.CLASS_NAME, "product_sort_container")
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        
    def sort_products_low_to_high(self):
        select = Select(self.driver.find_element(*self.sort_select))
        select.select_by_value("lohi")
        
    def get_product_prices(self):
        return [float(price.text[1:]) for price in self.driver.find_elements(*self.product_prices)]
        
    def add_to_cart(self, index):
        self.driver.find_elements(*self.add_to_cart_buttons)[index].click()
        
    def get_cart_button_text(self, index):
        return self.driver.find_elements(*self.add_to_cart_buttons)[index].text
        
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
