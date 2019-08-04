import allure

from Base.Base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step(title='选择弹窗退出按钮点击退出')
    def logout(self, tag=1):
        """
        退出
        :param tag: 1:退出 0：取消
        :return:
        """
        # 滑动页面
        self.scroll_screen()
        # 点击退出按钮
        self.click_element(PageElements.setting_logout_btn_id)
        if tag == 1:
            # 点击确定按钮
            self.click_element(PageElements.setting_acc_logout_btn_id)
        if tag == 0:
            # 取消退出按钮
            self.click_element(PageElements.setting_dis_logout_btn_id)
