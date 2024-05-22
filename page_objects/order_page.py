import allure
from page_objects.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Заполнение полей "Для кого самокат"')
    def fill_who_order_scooter(self, first_name, surname, address, subway_station, mobile_number):
        self.find_page(OrderPageLocators.first_name_field).send_keys(first_name)
        self.find_page(OrderPageLocators.surname_field).send_keys(surname)
        self.find_page(OrderPageLocators.address_field).send_keys(address)
        self.click_page(OrderPageLocators.subway_station_field)
        self.find_page(OrderPageLocators.subway_station_field).send_keys(subway_station)
        self.wait_until_element_is_visible(OrderPageLocators.subway_station_choice)
        self.click_page(OrderPageLocators.subway_station_choice)
        self.find_page(OrderPageLocators.phone_field).send_keys(mobile_number)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        return self.click_page(BasePageLocators.next_button)

    @allure.step('Заполнение полей "Про аренду"')
    def fill_about_order(self, comment):
        self.click_page(OrderPageLocators.date_selection_field)
        self.click_page(OrderPageLocators.date_selection)
        self.click_page(OrderPageLocators.time_of_lease_field)
        self.click_page(OrderPageLocators.time_of_lease_choice_six_day)
        self.click_page(OrderPageLocators.color_grey_field)
        self.find_page(OrderPageLocators.comment_field).send_keys(comment)

    @allure.step('Нажать кнопку Заказать')
    def click_finish_order_button(self):
        return self.click_page(OrderPageLocators.order_button)

    @allure.step('Нажать кнопку "Вы уверены? - Да"')
    def click_are_you_sure_yes_button(self):
        return self.click_page(OrderPageLocators.confidence_yes_button)

    @allure.step('Найти кнопку Посмотреть статус')
    def find_show_status_button(self):
        return self.find_page(OrderPageLocators.show_status_button)
