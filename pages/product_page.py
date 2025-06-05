from .base_page import BasePage
from .locators import CataloguePageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        product_name = self.safe_get_text(ProductPageLocators.PRODUCT_NAME, description = "Название продукта со страницы продукта")
        return product_name
