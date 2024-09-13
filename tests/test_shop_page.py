import pytest
from page_objects.shop_page import ShopPage
from page_objects.login_page import LoginPage
import logging as logger


class TestShopPage:

    @pytest.mark.tcid09
    def test_add_items_to_cart_from_main_page(self, my_driver):
        """
        This test confirms that we are able to add items to the cart from the main shop page
        1. Users can click add to cart for the items
        2. Add to cart button turns into remove button
        3. Cart Icon updates with the number of items added
        :return:
        """
        login_page = LoginPage(my_driver)
        login_page.execute_login(username="standard_user", password="secret_sauce")
        shop_page = ShopPage(my_driver)
        shop_page.click_add_to_cart_button(shop_page.backpack_add_to_cart)
        shop_page.click_add_to_cart_button(shop_page.bike_light_add_to_cart)
        shop_page.check_chart_count()
        # TODO: figure out how to compare the count on the cart icon to the number of items clicked.




