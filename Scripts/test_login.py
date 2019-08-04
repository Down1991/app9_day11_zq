import sys, os, pytest

sys.path.append(os.getcwd())
from Page.Page import Page
from Base.getDriver import get_android_driver
from Base.getFileData import GetFileData
from selenium.common.exceptions import TimeoutException


def get_login_data():
    # 预期成功数据
    suc_list = []
    # 预期失败数据
    fail_list = []
    # 读取全部数据
    login_data = GetFileData().get_yml_data("login_data.yml")
    for i in login_data.keys():
        if login_data.get(i).get("toast"):
            # 预期失败
            fail_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd"),
                              login_data.get(i).get("toast"), login_data.get(i).get("expect_data")))
        else:
            # 预期成功
            suc_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}


class TestLogin:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        # 退出driver
        self.page_obj.driver.quit()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        """进入登录页面"""
        # 点击我
        self.page_obj.get_home_page().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_chocie_login_page().click_exits_account_btn()

    @pytest.mark.parametrize("case_num, username, passwd, expect_data", get_login_data().get("suc"))
    def test_login_suc(self, case_num, username, passwd, expect_data):
        """
        预期成功测试用例
        :param case_num: 用例编号
        :param username: 用户名
        :param passwd: 密码
        :param expect_data: 预期结果
        :return:
        """
        # 登录
        self.page_obj.get_login_page().login(username, passwd)
        try:
            # 获取收藏
            cart_text = self.page_obj.get_person_page().get_shop_cart_text()
            try:
                # 断言
                assert cart_text == expect_data
            except AssertionError: # 断言失败异常
                """个人中心"""
                # 截图
                self.page_obj.get_person_page().screen_shot()
                assert False
            finally:
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 退出操作
                self.page_obj.get_setting_page().logout()

        except TimeoutException:
            """停留在登录页面"""
            # 截图
            self.page_obj.get_setting_page().screen_shot()
            # 关闭页面
            self.page_obj.get_login_page().close_login_page()
            assert False

    @pytest.mark.parametrize("case_num, username, passwd,toast,expect_data", get_login_data().get("fail"))
    def test_login_fail(self, case_num, username, passwd, toast, expect_data):
        """
        预期失败测试用例
        :param case_num: 用例编号
        :param username: 用户名
        :param passwd: 密码
        :param toast: xpath拼接语句
        :param expect_data: 预期结果
        :return:
        """
        # 登录操作
        self.page_obj.get_login_page().login(username, passwd)
        try:
            """找到toast"""
            # 获取toast 消息
            message = self.page_obj.get_login_page().get_toast(toast)
            try:
                # 断言
                assert message == expect_data
            except AssertionError:
                # 截图
                self.page_obj.get_login_page().screen_shot()
                assert False
        except TimeoutException:
            """没找到toast 消息"""
            # 截图
            self.page_obj.get_login_page().screen_shot()
            assert False
        finally:
            try:
                """登录按钮存在"""
                # 判断登录按钮
                self.page_obj.get_login_page().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
            except TimeoutException:
                """登录按钮不存在"""
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 退出操作
                self.page_obj.get_setting_page().logout()
                # 找不到登录按钮 全失败
                assert False
