import allure
from data import Urls
from page_objects.main_page import MainPage


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
        assert redirect_page.show_current_url() == Urls.BASE_URL

    @allure.title('Клик на логотип Яндекса')
    @allure.description(
        'Проверка редиректа на Дзен по нажатию на логотип Яндекса'
    )
    def test_redirect_yandex(self, driver):
        redirect_page = MainPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.click_yandex_logo()
        redirect_page.wait_window()
        assert redirect_page.show_current_url() == Urls.REDIRECT_URL
