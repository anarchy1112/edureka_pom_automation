import time

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.confreader import confread
from utilities.datagetter import getdata


class TestsReg(BaseTest):

    @pytest.mark.happyflow
    @pytest.mark.parametrize('email, phoneno, password', getdata('TestDataPath','test_register_sheet'))
    def test_reg_pass(self, email, phoneno, password):
        page=HomePage(self.driver)
        page.reg_user(email, phoneno)
        page.wait_clickable('locators','signupWin_btn_XPATH')
        assert page.enabled_button()==True
        page.reg_user2(password)
        page.wait_visible('locators', 'HP_loggedin_edureka_XPATH')
        assert page.login_text()==confread('asserts', 'HP_loggedin_text')
        page.alluress('test_reg_pass')

    @pytest.mark.negativeinput
    @pytest.mark.xfail
    @pytest.mark.parametrize('email, phoneno, password', getdata('TestDataPath','test_register_sheet_fail'))
    def test_reg_fail(self, email, phoneno, password):
        page = HomePage(self.driver)
        page.reg_user(email, phoneno)
        page.wait_visible('locators', 'signupWin_btn_XPATH')
        assert page.enabled_button() == True
        page.alluress('test_reg_fail')
        page.reg_user2(password)
        page.alluress('test_reg_fail')
        assert page.element_present('HP_loggedin_edureka_XPATH')


