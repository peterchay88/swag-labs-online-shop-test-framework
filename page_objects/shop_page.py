import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class ShopPage(BasePage):
    __url = "https://www.saucedemo.com/inventory.html"
    __cart_button = (By.ID, "shopping_cart_container")
    __nav_bar = (By.ID, "react-burger-menu-btn")
    __logout_button = (By.ID, "logout_sidebar_link")

    # Add to cart buttons for specified items
    __backpack_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    __bike_light_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")
    __black_shirt_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    __fleece_jacket_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    __onesie_add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
    __red_shirt_add_to_cart_btn = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    # Remove from cart buttons for specified items
    __backpack = {"add": (By.ID, "add-to-cart-sauce-labs-backpack"),
                  "remove": (By.ID, "remove-sauce-labs-backpack")}

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.__url
        self.backpack = self.__backpack
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

    def check_chart_count(self) -> int:
        """
        Returns the count in the cart icon
        :return:
        """
        if self.is_cart_button_is_displayed():
            logger.info(super()._find_element(element=self.__cart_button).text)
            return int(super()._find_element(element=self.__cart_button).text)

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
        if self.is_logout_button_present():
            super()._click_button(element=self.__logout_button)
        else:
            raise NoSuchElementException

    def click_add_to_cart_button(self, element: dict):
        """
        This method clicks the add to cart button for the specified element
        :param element: Use self attribute to define which item to add to the cart
        :return:
        """
        web_element = element['add']
        logger.info(f"Clicking add to cart for web element located at {web_element}")
        super()._click_button(web_element)

    def is_remove_from_cart_btn_visible(self, element: dict) -> bool:
        """
        This method checks to see if the remove from cart button is visible for a specified
        web element.
        :param element: Web element locator
        :return:
        """
        web_element = element['remove']
        logger.info(f"Checking to see if the remove from cart button is present for {web_element}")
        return super()._is_displayed(element=web_element)

    def click_remove_from_cart_button(self, element: dict):
        """
        This method clicks remove from cart for a specified web element.
        :param element: Web element locator
        :return:
        """
        web_element = element['remove']
        if self.is_remove_from_cart_btn_visible(web_element):
            logger.info(f"Clicking remove from cart button for {web_element}")
            super()._click_button(element=web_element)  # TODO: Test this
        else:
            pass


    def click_specified_add_to_cart_buttons(self, number: int):
        """
        this method clicks the add to cart button for the specified number of items passed in the argument
        :param number: Number of items to add to the cart
        :return:
        """
        logger.info(f"Clicking add to cart for {number} items")
        # list_of_buttons = [self.__bike_light_add_to_cart_btn, self.__backpack_add_to_cart_btn,
        #                    self.__black_shirt_add_to_cart_btn, self.__fleece_jacket_add_to_cart_btn,
        #                    self.__onesie_add_to_cart_btn, self.__red_shirt_add_to_cart_btn]
        list_of_buttons = [self.__backpack]  # TODO: Regression test this function w/ new element changes
        count = 0
        while count < number:
            web_element = random.choice(list_of_buttons)
            self.click_add_to_cart_button(web_element)  # Pick a random element from the list
            # Remove web element from list, so it cannot be picked again
            list_of_buttons.pop(list_of_buttons.index(web_element))
            count += 1
