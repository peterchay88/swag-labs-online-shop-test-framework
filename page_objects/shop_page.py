import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class ShopPage(BasePage):
    __url = "https://www.saucedemo.com/inventory.html"
    __cart_button = (By.ID, "shopping_cart_container")
    __nav_bar = (By.ID, "react-burger-menu-btn")
    __logout_button = (By.ID, "logout_sidebar_link")
    __backpack_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    __bike_light_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.__url
        self.backpack_add_to_cart = self.__backpack_add_to_cart_btn
        self.bike_light_add_to_cart = self.__bike_light_add_to_cart_btn
        super().__init__(driver)

    def get_current_url(self) -> str:
        """
        Returns current url
        :return:
        """
        return self.driver.current_url

    def check_current_url(self) -> bool:
        """
        Checks if current url matches shop page url
        :return:
        """
        if self.get_current_url() == self.__url:
            return True
        else:
            return False

    def is_cart_button_is_displayed(self) -> bool:
        """
        This method checks to see if the cart button is displayed on the shop page
        :return:
        """
        logger.info("Checking to see if cart button element is present on web page")
        return super()._is_displayed(element=self.__cart_button)

    def check_chart_count(self) -> str:
        """
        Returns the count in the cart icon
        :return:
        """
        if self.is_cart_button_is_displayed():
            logger.info(super()._find_element(element=self.__cart_button).text)
            return super()._find_element(element=self.__cart_button).text

    def click_cart_button(self):
        """
        This method is for clicking the cart button on the shop page
        :return:
        """
        self.is_cart_button_is_displayed()
        logger.info("Clicking cart button")
        super()._click_button(element=self.__cart_button)

    def is_nav_bar_present(self) -> bool:
        """
        This method checks to see if the nav bar on the shop page is present
        :return:
        """
        logger.info("Checking to see if nav bar is present")
        return super()._is_displayed(element=self.__nav_bar)

    def click_nav_bar(self):
        """
        This method clicks on the nav bar on the shop page
        :return:
        """
        self.is_nav_bar_present()
        logger.info("Clicking nav bar")
        super()._click_button(element=self.__nav_bar)

    def is_logout_button_present(self) -> bool:
        """
        This method checks to see if the logout button is present on the shop page
        :return:
        """
        logger.info("Checking to see if logout button is present")
        self.click_nav_bar()
        return super()._is_displayed(element=self.__logout_button)

    def click_logout_button(self):
        """
        This method clicks the logout button on the shop page
        :return:
        """
        # self.is_logout_button_present()
        super()._click_button(element=self.__logout_button)

    def click_add_to_cart_button(self, element: tuple):
        """
        This method clicks the add to cart button for the specified element
        :param element: Use self attribute to define which item to add to the cart
        :return:
        """
        logger.info(f"Clicking add to cart for web element located at {element}")
        super()._click_button(element)

    def click_specified_add_to_cart_buttons(self, number: int):
        """
        this method clicks the add to cart button for the specified number of items passed in the argument
        :param number: Number of items to add to the cart
        :return:
        """
        logger.info(f"Clicking add to cart for {number} items")
        list_of_buttons = [self.__bike_light_add_to_cart_btn, self.__backpack_add_to_cart_btn]
        count = 0
        while count < number:
            web_element = random.choice(list_of_buttons)
            self.click_add_to_cart_button(web_element)  # Pick a random element from the list
            list_of_buttons.pop(list_of_buttons.index(web_element))
            count += 1
        # TODO: Implement this in a test

