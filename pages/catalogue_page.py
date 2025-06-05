from .base_page import BasePage
from .locators import CataloguePageLocators

class CataloguePage(BasePage):
    def should_all_products_have_name_and_price(self):
        product_cards = self.browser.find_elements(*CataloguePageLocators.PRODUCT_CARD)

        assert len(product_cards) > 0, "❌ Не найдено ни одной карточки товара"

        for i, card in enumerate(product_cards, 1):
            name = card.find_element(*CataloguePageLocators.PRODUCT_NAME).text
            price = card.find_element(*CataloguePageLocators.PRODUCT_PRICE).text

            assert name != "", f"❌ У товара №{i} не указано название"
            assert price != "", f"❌ У товара №{i} не указана цена"
            print(f"✅ Товар №{i}: Название — '{name}', Цена — {price}")
