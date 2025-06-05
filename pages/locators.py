from selenium.webdriver.common.by import By

class CataloguePageLocators:
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product_pod")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h3 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")