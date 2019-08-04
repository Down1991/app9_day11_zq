import allure

from Base.Base import Base
from Page.pageElements import PageElements


class LoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step('点击登录的操作')
    def login(self, user, passwd):
        """
        登录
        :param user: 登录用户名
        :param passwd: 登录密码
        :return:
        """
        # 用户名
        self.send_element(PageElements.login_name_id, user)
        # 密码
        self.send_element(PageElements.login_passwd_id, passwd)
        # 登录
        self.click_element(PageElements.login_btn_id)
        allure.attach('登录用户名:{},登录密码{}'.format(user,passwd),'')
    @allure.step(title='关闭页面的操作')
    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_page_btn_id)
        allure.attach('关闭页面','')
    @allure.step(title='判断登录按钮是否存在的操作')
    def if_login_btn(self):
        # 登录
        self.get_element(PageElements.login_btn_id)

