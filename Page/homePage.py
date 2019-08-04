import allure

from Base.Base import Base
from Page.pageElements import PageElements


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title='点击首页我的操作')
    def click_my_btn(self):
        """点击首页我按钮"""
        self.click_element(PageElements.home_my_btn_id)
        allure.attach('点击进入我的首页的操作','')
