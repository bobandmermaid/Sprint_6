import allure
from data import Urls
from page_objects.main_page import MainPage
from locators.base_page_locators import BasePageLocators


class TestUrls:
    @allure.title('Клик на логотип Самоката')
    @allure.description(
        'Проверка редиректа на главную по нажатию на логотип Самоката'
    )
    def test_redirect_scooter(self, driver):
        redirect_page = MainPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.click_scooter_logo()
        redirect_page.wait_until_element_is_visible(BasePageLocators.middle_order_button)
        assert redirect_page.show_current_url() == Urls.BASE_URL

    @allure.title('Клик на логотип Яндекса')
    @allure.description(
        'Проверка редиректа на Дзен по нажатию на логотип Яндекса'
    )
    def test_redirect_yandex(self, driver):
        redirect_page = MainPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        assert len(driver.window_handles) == 1
        redirect_page.click_yandex_logo()
        redirect_page.check_window()
        redirect_page.wait_until_element_is_clickable(BasePageLocators.dzen_button)
        assert redirect_page.show_current_url() == Urls.REDIRECT_URL
