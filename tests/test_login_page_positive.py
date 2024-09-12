import pytest
from page_objects.login_page import LoginPage
from page_objects.shop_page import ShopPage
import logging as logger

pytestmark = [pytest.mark.login, pytest.mark.positive]


class TestLoginPagePositive:

    @pytest.mark.parametrize("username, password, test_id", [
        pytest.param("standard_user", "secret_sauce", "1", marks=pytest.mark.tcid01),
        pytest.param("visual_user", "secret_sauce", "2", marks=pytest.mark.tcid02)
    ])
    def test_login(self, username, password, test_id, my_driver):
        """
        This test confirms that we can log into the swag labs online shop
        1. Enter Username, 2. Enter Password, 3. Click login, 4. Validate successful login
        :return:
        """
        logger.info(f"Running test {test_id}")
        login_page = LoginPage(driver=my_driver)
        login_page.open_login_page()
        login_page.enter_username(username=str(username))
        login_page.enter_password(password=str(password))
        login_page.click_login_button()
        shop_page = ShopPage(driver=my_driver)
        # Confirm that we land on the shop page, Verify some elements on the page
        assert shop_page.is_cart_button_is_displayed(), "Error. Cart button not found on page"
        assert shop_page.is_logout_button_present(), "Error. Logout button not found on page"

    @pytest.mark.parametrize("username, password, test_id", [
        pytest.param("standard_user", "secret_sauce", "6", marks=pytest.mark.tcid06),
        pytest.param("visual_user", "secret_sauce", "7", marks=pytest.mark.tcid07)
    ])
    def test_round_trip_login(self, username, password, test_id, my_driver):
        """
        This test confirms a user can successfully log in and log out of the online shop.
        1. Enter Username, 2. Enter Password, 3. Click login, 4. Validate successful login,
        5. Click Logout button, 6. Validate successful log out.
        :param username:
        :param password:
        :param test_id:
        :param my_driver:
        :return:
        """