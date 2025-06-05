from selenium.webdriver.common.by import By

class CataloguePageLocators:
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product_pod")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h3 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-block")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")



class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
