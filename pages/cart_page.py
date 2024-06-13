from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        
    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)
        
    def get_item_price(self, index):
        return float(self.driver.find_elements(*self.cart_items)[index].find_element(By.CLASS_NAME, "inventory_item_price").text[1:])
        
    def get_item_name(self, index):
        return self.driver.find_elements(*self.cart_items)[index].find_element(By.CLASS_NAME, "inventory_item_name").text
        
    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
