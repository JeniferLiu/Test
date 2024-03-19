"""页面基类，在这个类中实现对webdriver常用API的二次封装"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ch
from selenium.webdriver.edge.service import Service as eg
from selenium.webdriver.firefox.service import Service as ff
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __ini__(self, driver=None):  # 构造方法，构造函数。在 Python 中，构造函数用于初始化新创建的对象。当创建一个类的实例时，Python 会自动调用这个构造函数。
        self.driver = webdriver

    def open(self, browser, url):
        """打开指定浏览器并访问指定页面"""
        if browser.lower() == "edge":
            self.driver = webdriver.Edge(service=eg())
        elif browser.lower() == "chrome":
            self.driver = webdriver.Chrome(service=ch())
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox(service=ff())

    def sleep(self, t):
        """强制等待"""
        time.sleep(t)

    def wait(self, t, how, what):
        """显式等待，定位元素的值直到出现"""
        obj = WebDriverWait(driver=self.driver,
                            timeout=t,
                            poll_frequency=0.5)
        return obj.until(lambda ele: self.driver.find_element(how), what)

    def get_element(self, how, what):
        """根据定位策略和值查找元素。"""
        try:
            return self.driver.find_element(how, what)
        except Exception as e:
            print(f"查找元素时发生错误：{e}")
            return None

    def element_input(self, how, what, value):
        """在指定元素中输入指定内容"""
        ele = self.get_element(how, what)
        if ele:
            ele.clear()
            ele.send_keys(value)

    def element_click(self, how, what):
        """点击"""
        ele = self.get_element(how, what)
        if ele:
            ele.click()

    def select_option(self, how, what, mode, value=None):
        """在下拉框中选择指定选项
        mode: 选取方式，
            0-获取所有，
            1-通过索引选取，
            2-通过value属性值选取，
            3-通过文本值选取
        """
        ele = self.get_element(how, what)
        if ele:
            obj = Select(ele)
            if mode == 0:
                return obj.options
            elif mode == 1:
                obj.select_by_index(value)
            elif mode == 2:
                obj.select_by_value(value)
            else:
                obj.select_by_visible_text(value)

    def switch_frame(self, how=None, what=None):
        """切换到指定框架。如果未指定how和what，则切换回主内容框架。"""
        try:
            if not how and not what:
                # 没有提供定位参数，切换回主内容框架
                self.driver.switch_to.default_content()
                print("已切换回主内容框架。")
            else:
                # 使用提供的定位参数查找框架元素
                frame = self.get_element(how, what)
                if frame:
                    # 如果找到了框架元素，切换到该框架
                    self.driver.switch_to.frame(frame)
                    print(f"已切换到框架：{what}。")
                else:
                    # 如果未找到框架元素，打印错误信息
                    print(f"未找到指定的框架：{what}。")
        except Exception as e:
            # 捕获并打印异常信息
            print(f"切换框架时发生错误：{e}")

    def opt_alert(self, action, value=None):
        """处理警告框
        action:
            0-获取文本；
            1-点击确定；
            2-点击取消；
            3-输入"""
        if action == 0:
            return self.driver.switch_to.alert.text
        elif action == 1:
            self.driver.switch_to.alert.accept()
        elif action == 2:
            self.driver.switch_to.alert.dismiss()
        else:
            self.driver.switch_to.alert.send_keys(value)

    def execute_js(self, js, param=None):
        """执行js代码"""
        self.driver.execute_script(js)

    def get_title(self):
        """获取页面标题"""
        return self.driver.title

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def get_element_att(self, how, what, att):
        """获取元素的指定属性值"""
        ele = self.get_element(how, what)
        if ele:
            return ele.get_attribute(att)

    def get_element_text(self, how, what):
        """获取元素的文本值"""
        ele = self.get_element(how, what)
        if ele:
            return ele.text

    def get_element_image(self, how, what, file):
        """对指定元素截图"""
        ele = self.get_element(how, what)
        if ele:
            ele.screenshot(file)

    def checkbox_select(self, how, what, desired_state):
        """根据desired_state对checkbox进行勾选或取消勾选"""
        checkbox = self.driver.find_element(how, what)

        # 如果desired_state为True且checkbox未被选中，则点击checkbox选中它
        if desired_state and not checkbox.is_selected():
            checkbox.click()
        # 如果desired_state为False且checkbox被选中，则点击checkbox取消选中它
        elif not desired_state and checkbox.is_selected():
            checkbox.click()

    def close_window(self):
        """关闭当前标签页"""
        self.driver.close()

    def close_broswer(self):
        """关闭浏览器"""
        self.driver.quit()

    def reload(self):
        """刷新页面"""
        self.driver.refresh()
