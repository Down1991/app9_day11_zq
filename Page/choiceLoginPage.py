import allure

from Base.Base import Base
from Page.pageElements import PageElements


class ChoicLoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title='点击已有账号去登录')
    def click_exits_account_btn(self):
        """点击已有账号去登录"""
        self.click_element(PageElements.choice_login_exits_account_id)
        allure.attach('点击已有账号去登录')
