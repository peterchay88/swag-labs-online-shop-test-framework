from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class ShopPage(BasePage):
    __cart_button = (By.ID, "shopping_cart_container")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def click_cart_button(self):
        """
        This method is for clicking the cart button on the shop page
        :return:
        """
        logger.info("Clicking cart button")
        super()._click_button(element=self.__cart_button)
