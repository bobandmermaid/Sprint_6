import allure
from page_objects.base_page import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Нажать на стрелочку у вопроса из списка')
    def click_dropdown_menu_button(self, *locator):
        return self.click_page(*locator)

    @allure.step('Кликнуть лого Яндекса')
    def click_yandex_logo(self):
        return self.click_page(BasePageLocators.yandex_logo)

    @allure.step('Кликнуть лого Самоката')
    def click_scooter_logo(self):
        return self.click_page(BasePageLocators.scooter_logo)

