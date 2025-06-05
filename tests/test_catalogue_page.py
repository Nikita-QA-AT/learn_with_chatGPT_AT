import time
import pytest

from pages.catalogue_page import CataloguePage
from pages.product_page import ProductPage


CATALOG_LINK = "http://selenium1py.pythonanywhere.com/catalogue/"

@pytest.mark.skip(reason="Отлаживаю другие тк, и специально не запускаю этот")
def test_products_have_name_and_price(browser):
    page = CataloguePage(browser, CATALOG_LINK)
    page.open()
    page.should_all_products_have_name_and_price()

@pytest.mark.skip(reason="Отлаживаю другие тк, и специально не запускаю этот")
def test_product_name_matches_between_catalogue_and_detail(browser):
    page = CataloguePage(browser, CATALOG_LINK)
    page.open()
    product_name_from_catalog = page.get_product_name_from_card_in_catalog()
    page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    product_name_from_card = product_page.get_product_name()
    assert product_name_from_catalog == product_name_from_card, f"имя в каталоге {product_name_from_catalog}, имя в карточке {product_name_from_card}"
    print(f"ТК пройден успешно: имя продукта в каталоге и внутри карточки продукта совпадает")



@pytest.mark.skip(reason="Отлаживаю другие тк, и специально не запускаю этот")
def test_add_product_to_basket_from_catalog(browser):
    page = CataloguePage(browser, CATALOG_LINK)
    page.open()
    product_name_from_catalog = page.get_product_name_from_card_in_catalog()
    page.add_product_to_basket_from_catalog()
    product_name_from_success_message = page.get_product_name_from_success_message()
    assert product_name_from_catalog == product_name_from_success_message, f"ожидали, что имя в каталоге{product_name_from_catalog}, и имя в сообщении об успешном добавлении{product_name_from_success_message} будут одинаковыми"
    print(f"Тест успешно пройден: имя в каталоге совпадает с именем в сообщении об успешном добавлении")


def test_product_price_after_add_to_basket_equals_basket_total_in_success_message(browser):
    page = CataloguePage(browser, CATALOG_LINK)
    page.open()
    product_price = page.get_product_price_from_card_in_catalog()
    page.add_product_to_basket_from_catalog()
    product_price_from_success_message = page.get_basket_total_from_success_message()
    assert product_price == product_price_from_success_message, f"ожидали, что после добавления в корзину, итоговая цена в корзине {product_price_from_success_message}будет совпадать с ценой товара{product_price}"
    print(f"Тест успешно пройден: после добавления в корзину, итоговая цена в корзине {product_price_from_success_message} совпадает с ценой товара {product_price}, который был добавлен")



