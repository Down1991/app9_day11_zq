from selenium.webdriver.common.by import By

from Base.getDriver import get_android_driver

from Page.Page import Page

# 实例化统一入口类
page_obj = Page(get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

# 点击我
page_obj.get_home_page().click_my_btn()
# 点击已有账号去登录
page_obj.get_chocie_login_page().click_exits_account_btn()
# 登录操作
page_obj.get_login_page().login("13488834010", "159357")

# # 获取提示消息

print(page_obj.get_setting_page().get_toast("错误"))
# mess_path = (By.XPATH, "//*[contains(@text,'密码错误')]")
# print(page_obj.get_login_page().get_element(mess_path, timeout=5, poll_frequency=0.5).text)


# # 个人中心 -获取我的收藏
# print(page_obj.get_person_page().get_shop_cart_text())
# # 个人中心 -点击设置
# page_obj.get_person_page().click_setting_btn()
# # 设置页面点击 -退出
# page_obj.get_setting_page().logout()
# # 退出driver
# page_obj.driver.quit()
