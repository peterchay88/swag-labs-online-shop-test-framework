from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class ShopPage(BasePage):
    __cart_button = (By.ID, "shopping_cart_container")
    __nav_bar = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def check_if_cart_button_is_displayed(self) -> bool:
        """
        This method checks to see if the cart button is displayed on the shop page
        :return:
        """
        logger.info("Checking to see if cart button element is present on web page")
        return super()._is_displayed(element=self.__cart_button)

    def click_cart_button(self):
        """
        This method is for clicking the cart button on the shop page
        :return:
        """
        self.check_if_cart_button_is_displayed()
        logger.info("Clicking cart button")
        super()._click_button(element=self.__cart_button)

    def is_logout_button_present(self):
        pass

    def click_logout_button(self):
        pass

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