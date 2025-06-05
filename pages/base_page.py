from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout  # сохраним для использования в явных ожиданиях

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def safe_click(self, locator, timeout=10, description="элемент"):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            print(f"✅ Клик по элементу: {description}")
        except TimeoutException:
            raise AssertionError(
                f"❌ Не удалось кликнуть по элементу: {description}. Возможно, он неактивен или селектор неверный: {locator}")

    def safe_click_inside(self, parent_element, locator, timeout=10, description="элемент"):
        try:
            element = parent_element.find_element(*locator)
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((locator[0], locator[1]))
            )
            element.click()
            print(f"✅ Клик по {description}")
        except Exception as e:
            raise AssertionError(f"❌ Не удалось кликнуть по {description}. Ошибка: {e}")

    def safe_find(self, locator, timeout=10, description="элемент"):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"❌ Не найден {description} за {timeout} секунд. Локатор: {locator}"
            )
            print(f"✅ Найден элемент: {description}")
            return element
        except TimeoutException as e:
            raise AssertionError(
                f"❌ Ошибка: {description} не найден за {timeout} секунд. Проверь локатор: {locator}"
            ) from e

    def safe_find_all(self, locator, timeout=10, description="элементы"):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            elements = self.browser.find_elements(*locator)
            if not elements:
                raise AssertionError(f"❌ {description} найдены, но список пуст. Локатор: {locator}")
            print(f"✅ Найдено {len(elements)} {description}")
            return elements
        except TimeoutException:
            raise AssertionError(f"❌ {description} не найдены за {timeout} сек. Локатор: {locator}")


    def safe_get_text(self, locator, timeout=10, description="элемент"):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"❌ Не найден {description} за {timeout} секунд. Локатор: {locator}"
            )
            text = element.text  # важный момент — после явного ожидания
            print(f"✅ Получен текст '{text}' из: {description}")
            return text
        except StaleElementReferenceException:
            # попробуем повторно найти и взять текст (1 раз)
            try:
                element = WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                return element.text
            except Exception as e:
                raise AssertionError(f"❌ {description} стал недоступен из-за перерисовки. Локатор: {locator}") from e

    def safe_get_text_inside(self, parent_element, locator, description="элемент"):
        try:
            element = parent_element.find_element(*locator)
            text = element.text
            print(f"✅ Получен текст '{text}' из {description}")
            return text
        except Exception as e:
            raise AssertionError(f"❌ Не удалось получить текст из {description}. Ошибка: {e}")

    def safe_get_attribute(self, element, attribute_name, description="элемент"):
        try:
            value = element.get_attribute(attribute_name)
            print(f"✅ Получен атрибут '{attribute_name}' со значением '{value}' из: {description}")
            return value
        except Exception as e:
            raise AssertionError(f"❌ Не удалось получить атрибут '{attribute_name}' из {description}") from e

    def safe_fill_input(self, locator, text, description="поле ввода"):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            print(f"✅ Ввели текст '{text}' в {description}")
        except TimeoutException:
            assert False, f"❌ {description} не найдено на странице"