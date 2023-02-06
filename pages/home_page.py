from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def reg_user(self, email, phoneno):
        self.click('HP_signup_btn_XPATH')
        self.type('signupWin_email_XPATH', email)
        self.type('signupWin_phone_XPATH', phoneno)
        self.click('signupWin_chkbx_XPATH')

    def enabled_button(self):
        return self.enable_check('signupWin_btn_XPATH')

    def reg_user2(self,password):
        self.click('signupWin_btn_XPATH')
        self.type('signupWin2_passw_XPATH', password)
        self.click('signupWin2_btn_XPATH')


    def dologin(self, email, password):
        self.click('HP_login_btn_XPATH')
        self.erase('login_win_email_XPATH')
        self.erase('login_win_pass_XPATH')
        self.type('login_win_email_XPATH', email)
        self.type('login_win_pass_XPATH', password)
        self.click('login_win_btn_XPATH')

    def login_text(self):
        return self.text_extract('HP_loggedin_edureka_XPATH')
