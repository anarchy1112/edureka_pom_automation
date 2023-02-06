import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.confreader import confread
from utilities.datagetter import getdata


class TestsLogin(BaseTest):

    @pytest.mark.parametrize('email, password', getdata('TestDataPath','test_register_sheet'))
    def test_login_pass(self, email, password):
        page=HomePage(self.driver)
        page.dologin(email, password)
        assert page.login_text()==confread('locators', 'HP_loggedin_text')


    @pytest.mark.xfail
    @pytest.mark.parametrize('email, password', getdata('TestDataPath','test_register_sheet_fail'))
    def test_login_fail(self, email, password):
        page = HomePage(self.driver)
        page.dologin(email, password)
        assert page.login_text() == confread('locators', 'HP_loggedin_text')