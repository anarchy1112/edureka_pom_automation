import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.confreader import confread
from utilities.datagetter import getdata


class TestsLogin(BaseTest):

    @pytest.mark.parametrize('email, phoneno, password', getdata('TestDataPath','test_register_sheet'))
    def test_reg_pass(self, email, phoneno, password):
        page=HomePage(self.driver)
        page.reg_user(email, phoneno)
        assert page.enabled_button()==True
        page.reg_user2(password)
        assert page.login_text()==confread('locators', 'HP_loggedin_text')


    @pytest.mark.xfail
    @pytest.mark.parametrize('email, phoneno, password', getdata('TestDataPath','test_register_sheet_fail'))
    def test_reg_fail(self, email, phoneno, password):
        page = HomePage(self.driver)
        page.reg_user(email, phoneno)
        assert page.enabled_button() == True
        page.reg_user2(password)
        assert page.login_text() == confread('locators', 'HP_loggedin_text')