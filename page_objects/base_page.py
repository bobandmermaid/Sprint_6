import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from data import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_base_url(self):
        return self.driver.get(Urls.BASE_URL)

    @allure.step('Вернуть адрес текущей страницы')
    def show_current_url(self):
        return self.driver.current_url

    @allure.step('Найти страницу или элемент')
    def find_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Нажать на страницу или элемент')
    def click_page(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Открыть блок "Вопросы о важном"')
    def open_important_questions_section(self):
        element = self.find_page(BasePageLocators.important_question_section)
        return self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликаем кнопку "Заказать" в хэдере')
    def click_header_order_button(self):
        return self.driver.find_element(*BasePageLocators.header_order_button).click()

    @allure.step('Дождаться загрузки элемента')
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 6).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step('Дождаться загрузки элемента при проверке заказа')
    def wait_until_element_is_visible_order(self):
        return WebDriverWait(self.driver, 6).until(
            expected_conditions.presence_of_element_located(BasePageLocators.next_button)
        )

    @allure.step('Дождаться, чтобы на элемент можно было нажать при проверке заказа')
    def wait_until_element_is_clickable_order(self):
        return WebDriverWait(self.driver, 6).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.confidence_yes_button)
        )

    @allure.step('Принять cookies')
    def click_cookie_consent(self):
        return self.driver.find_element(*BasePageLocators.cookie_button).click()

    @allure.step("Ожидание открытия второго окна")
    def wait_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url == Urls.REDIRECT_URL)
