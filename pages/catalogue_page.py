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


    def get_product_name_from_card_in_catalog(self, index=3):
        cards = self.safe_find_all(CataloguePageLocators.PRODUCT_CARD, description="Карточки всех товаров")
        card = cards[index]
        name_element = card.find_element(*CataloguePageLocators.PRODUCT_NAME)
        product_name = self.safe_get_attribute(name_element, "title", description=f"название товара под индексом {index}")
        return product_name



    def get_product_price_from_card_in_catalog(self, index=3):
        cards = self.safe_find_all(CataloguePageLocators.PRODUCT_CARD, description="Карточки всех товаров")
        card = cards[index]
        product_price = self.safe_get_text_inside(card, CataloguePageLocators.PRODUCT_PRICE, description=f"цена товара под индексом {index}")
        return product_price






    def go_to_product_page(self, index=3):
        cards = self.safe_find_all(CataloguePageLocators.PRODUCT_CARD, description="Карточки всех товаров")
        card = cards[index]
        self.safe_click_inside(card, CataloguePageLocators.PRODUCT_NAME, description=f"Карточка товара с индексом {index} для перехода внутрь карточки товара")


    def add_product_to_basket_from_catalog(self, index=3):
        cards = self.safe_find_all(CataloguePageLocators.PRODUCT_CARD, description="Карточки всех товаров")
        card = cards[index]
        self.safe_click_inside(card, CataloguePageLocators.ADD_TO_BASKET_BUTTON, description=f"кнопке 'Добавить в корзину' для товара с index =  {index}")

    def get_product_name_from_success_message(self):
        return self.safe_get_text(CataloguePageLocators.SUCCESS_MESSAGE_PRODUCT_NAME, description="имя товара в сообщении об успешном добавлении")

    def get_basket_total_from_success_message(self):
        return self.safe_get_text(CataloguePageLocators.BASKET_TOTAL, description="итоговая сумма в корзине после добавления")





