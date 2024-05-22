import allure
import pytest
import helpers
from data import Urls
from page_objects.order_page import OrderPage


class TestOrder:

    @allure.title('Нажать кнопку "Заказать" (header)')
    @allure.description('Проверка открытия формы заказа по нажатию на кнопку "Заказать" в хэдере')
    def test_click_order_header(self, driver):
        redirect_page = OrderPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.wait_until_element_is_visible_order()

        assert redirect_page.show_current_url() == Urls.ORDER_PAGE_URL

    @allure.title('Нажать кнопку "Заказать" (middle)')
    @allure.description('Проверка открытия формы заказа по нажатию на кнопку "Заказать" в середине страницы')
    def test_click_order_middle(self, driver):
        redirect_page = OrderPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.wait_until_element_is_visible_order()

        assert redirect_page.show_current_url() == Urls.ORDER_PAGE_URL

    @allure.title('Заполнение формы оформления заказа (positive)')
    @allure.description('Проверка создания заказа при вводе валидных данных в форме оформления заказа')
    @pytest.mark.parametrize(
        'first_name, surname, address, subway_station, mobile_number, comment',
        [
            [
                'Северус',
                'Снейп',
                '3-я Фрунзенская 26',
                'Спортивная',
                '+79990987654',
                'Комментарий',
            ],
            [
                'Альбус',
                'Дамблдор',
                'Свободная ул. 1',
                'Фрунзенская',
                helpers.random_telephone(),
                'Непонятное понятно',
            ],
        ],
    )
    def test_order_form(self, driver, first_name, surname, address, subway_station, mobile_number, comment):
        booking_page = OrderPage(driver)
        booking_page.open_base_url()
        booking_page.click_header_order_button()
        booking_page.click_cookie_consent()
        booking_page.fill_who_order_scooter(first_name, surname, address, subway_station, mobile_number)
        booking_page.click_next_button()
        booking_page.fill_about_order(comment)
        booking_page.click_finish_order_button()
        booking_page.wait_until_element_is_clickable_order()
        booking_page.click_are_you_sure_yes_button()

        assert booking_page.find_show_status_button().text == 'Посмотреть статус'
