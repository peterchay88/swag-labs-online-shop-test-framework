import pytest
from page_objects.shop_page import ShopPage
from page_objects.login_page import LoginPage
import logging as logger

pytestmark = [pytest.mark.shop_page]


class TestShopPage:

    @pytest.mark.parametrize("number_of_items_to_add", [
        pytest.param(1, marks=pytest.mark.tcid09),
        pytest.param(2, marks=pytest.mark.tcid10),
        pytest.param(3, marks=pytest.mark.tcid11),
        pytest.param(4, marks=pytest.mark.tcid12),
        pytest.param(5, marks=pytest.mark.tcid13),
        pytest.param(6, marks=pytest.mark.tcid14)
    ])
    def test_add_items_to_cart_from_main_page(self, number_of_items_to_add, my_driver):
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
        shop_page.click_specified_add_to_cart_buttons(number=number_of_items_to_add)
        assert shop_page.check_chart_count() == number_of_items_to_add, \
            f"Error. Unexpected value. Expected {number_of_items_to_add}. Actual {shop_page.check_chart_count()}."

    @pytest.mark.tcid15
    def test_validate_add_cart_button(self, my_driver):
        """
        This test confirms that when clicking the add to cart button from the main shop page, the add to cart button
        changes to a remove from cart button
        :param my_driver:
        :return:
        """
        pass


