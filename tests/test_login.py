import allure
import pytest
from allure_commons.types import AttachmentType

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.confreader import confread
from utilities.datagetter import getdata


class TestsLogin(BaseTest):

    @pytest.mark.happyflow
    @pytest.mark.parametrize('email, password', getdata('TestDataPath','test_login_sheet'))
    def test_login_pass(self, email, password):
        page=HomePage(self.driver)
        page.dologin(email, password)
        page.wait_visible('locators','HP_loggedin_edureka_XPATH')
        page.alluress("test_login")
        assert page.login_text()==confread('asserts', 'HP_loggedin_text')


    @pytest.mark.negativeinput
    @pytest.mark.xfail
    @pytest.mark.parametrize('email, password', getdata('TestDataPath','test_login_sheet_fail'))
    def test_login_fail(self, email, password):
        page = HomePage(self.driver)
        page.dologin(email, password)
        page.alluress("test_login_fail")
        assert page.element_present('HP_loggedin_edureka_XPATH')
