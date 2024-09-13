import pytest
import logging as logger
from page_objects.login_page import LoginPage

pytestmark = [pytest.mark.login, pytest.mark.negative]


class TestLoginPageNegative:

    @pytest.mark.parametrize("username, password, error_msg, test_id", [
        pytest.param("incorrect_user", "secret_sauce",
                     "Epic sadface: Username and password do not match any user in this service",
                     "3", marks=pytest.mark.tcid03),
        pytest.param("standard_user", "incorrect_password",
                     "Epic sadface: Username and password do not match any user in this service",
                     "4", marks=pytest.mark.tcid04),
        pytest.param("incorrect_user", "incorrect_password",
                     "Epic sadface: Username and password do not match any user in this service",
                     "5", marks=pytest.mark.tcid05,),
        pytest.param("locked_out_user", "secret_sauce",
                     "Epic sadface: Sorry, this user has been locked out.",
                     "8", marks=pytest.mark.tcid08,)
    ])
    def test_bad_login(self, username, password, error_msg, test_id, my_driver):
        """
        This tests confirms we met the expected error when entering the incorrect credentials on the login page
        1. Open webpage, 2. Enter in incorrect username + Password combo, 3. Click login,
        4. Verify that the correct error message is displayed on the webpage
        :return:
        """
        logger.info(f"Running test {test_id}")
        login_page = LoginPage(my_driver)
        login_page.open_login_page()
        login_page.enter_username(username=str(username))
        login_page.enter_password(password=str(password))
        login_page.click_login_button()
        # Confirm login error is correct
        assert login_page.check_login_error_message() == error_msg, \
            f"Error, unexpected error message. Expected {error_msg}. Actual {login_page.check_login_error_message()}"
        
