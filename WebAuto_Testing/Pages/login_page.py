from WebAuto_Testing.Common.base_page import BasePage


class Login_Page(BasePage):
    # 定位登录元素
    user = ("By.ID", "account")
    pwd = ("By.NAME", "password")
    keeplogin = ("By.ID", "keepLoginon")
    submit = ("By.ID", "submit")

    # 封装每个元素的操作方法
    def input_user(self, account):
        # 输入用户名
        # *操作符用于解包参数列表。当你在函数调用时使用*，它会将列表、元组或任何可迭代对象中的元素“展开”，作为独立的参数传递给函数。
        # self.pwd 是一个元组，包含两个元素，分别是定位方法和定位值（例如，("By.NAME", "password")）
        self.element_input(*self.user, account)

    def input_pwd(self, password):
        # 输入密码
        self.element_input(*self.pwd, password)

    def keep_login(self, desired_state):
        # desired_state :True or False
        self.checkbox_select(*self.keeplogin, desired_state)

    def click_login(self):
        """点击登录"""
        self.element_click(*self.submit)
