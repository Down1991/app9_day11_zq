import allure

from Base.Base import Base
from Page.pageElements import PageElements


class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title='获取我的收藏的文本信息')
    def get_shop_cart_text(self):
        """获取我的收藏文本信息"""
        result = self.get_element(PageElements.person_shopcart_id).text
        allure.attach('我的收藏的文本信息:{}'.format(result))
        return result


    @allure.step(title='点击设置按钮操作')
    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(PageElements.person_setting_btn_id)
        allure.attach('点击设置按钮')

