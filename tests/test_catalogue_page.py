from pages.catalogue_page import CataloguePage

def test_products_have_name_and_price(browser):
    catalog_link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = CataloguePage(browser, catalog_link)
    page.open()
    page.should_all_products_have_name_and_price()
