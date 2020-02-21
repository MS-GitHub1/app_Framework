#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 16:13
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from Common.logger_handler import logger
from appium.webdriver.common.multi_action import MultiAction
from Common.dir_config import picture_path
from appium.webdriver.common.touch_action import TouchAction
import datetime
import time

class Base:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.Maximum = driver.get_window_size()
        # 截图方法
    def save_page_screenshot(self,img_doc):
        """
        :param img_doc:
        :return:
        """
        # 路径配置文件中引入图片保存路径  + 年月日-时分秒
        #  # 截图 - 命名。 页面名称_行为名称_当前的时间.png
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = picture_path + "/{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logger.exception("当前网页截图失败")
        else:
            logger.info("截取当前网页成功并存储在: {}".format(screenshot_path))

    # 等待元素可见
    def wait_ele(self,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info("{} : 等待 {} 元素可见".format(img_doc,loc))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(loc))
        except AssertionError as e:
            logger.exception("等待元素可见失败：")
            self.save_page_screenshot(img_doc)
            raise e
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logger.info("等待结束.开始时间为{},结束时间为:{},一共等待耗时为:{}".format(start, end, end - start))

    # 查找单个元素
    def get_ele(self,loc,img_doc):
        logger.info("{} : 查找 {} 元素.".format(img_doc,loc))
        try:
            ele = self.driver.find_element(*loc)
        except AssertionError as e:
            logger.exception("查找元素失败：")
            raise e
        else:
            return ele
        # 点击
    def click_ele(self,loc,img_doc,timeout=30,poll_fre=0.5):
        # 等待元素可见
        self.wait_ele(loc,img_doc,timeout,poll_fre)
        ele = self.get_ele(loc,img_doc)
        logger.info("{}: 点击 {} 元素 ".format(img_doc, loc))
        try:
            ele.click()
        except AssertionError as e:
            logger.info("{}点击 {} 元素失败".format(img_doc,loc))
            raise e
        # 输入

    def send_text(self, locator, value, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素可见；2）查找元素；3）输入动作
        self.wait_ele(locator, img_doc, timeout, poll_fre)
        ele = self.get_ele(locator, img_doc)
        logger.info("{}: 对 {} 元素输入文本 {}".format(img_doc, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 异常信息写入日志
            logger.exception("输入文本失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

        # 获取动作
    def get_attr(self,locator,name,img_doc, timeout=30, poll_fre=0.5):
        self.wait_ele(locator, img_doc, timeout, poll_fre)
        ele = self.get_ele(locator, img_doc)
        logger.info("{}: 获取 {}  元素的文本内容.".format(img_doc, locator))
        try:
            tel = ele.get_attribute(name)
        except:
            logger.exception(("获取元素文本值失败{}").format(locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            logger.info("获取的文本值为: {}".format(tel))
            return tel
        #获取值
    def  get_element_text(self, locator,img_doc, timeout=30, poll_fre=0.5):
        self.wait_ele(locator, img_doc, timeout, poll_fre)
        ele = self.get_ele(locator, img_doc)
        logger.info("{}: 获取 {}  元素的文本内容.".format(img_doc,locator))
        try:
            te = ele.text
        except:
            logger.exception(("获取元素文本值失败{}").format(locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            logger.info("获取的文本值为: {}".format(te))
            return te
        # 获取toast值
    def get_toast(self, locator,img_doc, timeout=30, poll_fre=0.5):
        WebDriverWait(self.driver,timeout,poll_fre).until(EC.presence_of_element_located(locator))
        ele = self.get_ele(locator, img_doc)
        logger.info("{}: 获取 {}  元素的文本内容.".format(img_doc, locator))
        try:
            te = ele.text
        except:
            logger.exception(("获取元素文本值失败{}").format(locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            logger.info("获取的文本值为: {}".format(te))
            return te

     # 画对应的九宫格的方法
    def nine_squared(self,loc,img_doc,timeout=30,poll_fre=0.5):
        # 整个高和宽
        self.driver.get_window_size()
        self.wait_ele(loc,img_doc,timeout,poll_fre)
        # 使用TouchAction获取起点
        ta = TouchAction(self.driver)
        ele = self.get_ele(loc,img_doc)
        qidian = ele.location
        size = ele.size
        step = size["width"] / 6
        p1 = (qidian["x"] + step, qidian["y"] + step)
        p2 = (p1[0] + 2 * step, p1[1])
        p3 = (p2[0] + 2 * step, p2[1])
        p4 = (p3[0], p3[1] + 2 * step)
        p5 = (p4[0], p4[1] + 2 * step)
        p6 = (p5[0] - 2 * step, p5[1])
        ta.press(x=p1[0], y=p1[1]).wait(200). \
            move_to(x=p2[0], y=p2[1]).wait(200). \
            move_to(x=p3[0], y=p3[1]).wait(200). \
            move_to(x=p4[0], y=p4[1]).wait(200). \
            move_to(x=p5[0], y=p5[1]).wait(200). \
            move_to(x=p6[0], y=p6[1]).wait(200). \
            release().perform()


    #滑动操作（四个滑动）
    def slide(self,loc,img_doc,timeout=30,poll_fre=0.5):
        # 整个的宽和高度
        WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_all_elements_located(loc))

    # 由下向上滑动操作
    def Up_and_down(self,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info("由下向上滑动:")
        self.slide(loc,img_doc,timeout,poll_fre)
        self.driver.swipe(self.Maximum["width"]*0.3,self.Maximum["height"]*0.70,self.Maximum["width"]*0.3,self.Maximum["height"]*0.30,200)

    # 由下向上滑动操作
    def down_and_up(self,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info("由下向上滑动:")
        self.slide(loc,img_doc,timeout,poll_fre)
        self.driver.swipe(self.Maximum["width"]*0.3,self.Maximum["height"]*0.15,self.Maximum["width"]*0.3,self.Maximum["height"]*0.85,200)

    # 由左向右滑动操作
    def Left_and_right(self,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info("由左向右滑动:")
        self.slide(loc,img_doc,timeout,poll_fre)
        self.driver.swipe(self.Maximum["width"]*0.10,self.Maximum["height"]*0.40,self.Maximum["width"]*0.80,self.Maximum["height"]*0.40,200)

    # 由右向左滑动操作
    def right_and_Left(self,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info("由右向左滑动:")
        self.slide(loc,img_doc,timeout,poll_fre)
        self.driver.swipe(self.Maximum["width"]*0.80,self.Maximum["height"]*0.40,self.Maximum["width"]*0.10,self.Maximum["height"]*0.40,200)

    # 多点触控
    def Multipoint(self,loc,img_doc,timeout=30,poll_fre=0.5):
        self.wait_ele(loc,img_doc, timeout, poll_fre)
        time.sleep(20)
        # 从中间划到左下
        logger.info(" 从中间划到左下:")
        t1 = TouchAction(self.driver).press(x=self.Maximum["width"]*0.5,y=self.Maximum["height"]*0.5).wait(200)\
            .move_to(x=self.Maximum["width"]*0.1,y=self.Maximum["height"]*0.9).release()
        # 从中间划到右上
        logger.info(" 从中间划到右上:")
        t2 = TouchAction(self.driver).press(x=self.Maximum["width"] * 0.5, y=self.Maximum["height"] * 0.5).wait(200) \
            .move_to(x=self.Maximum["width"] * 0.9, y=self.Maximum["height"] * 0.1).release()
        mm = MultiAction(self.driver)
        mm.add(t1,t2)
        mm.perform()

    # 列表滑动
    def get_lb_slide(self,lo,loc,img_doc,timeout=30,poll_fre=0.5):
        logger.info(" 列表滑动:")
        self.wait_ele(lo,img_doc,timeout,poll_fre)
        # 新的页面与old页面进行循环，不相等就行循环
        old = None
        new = self.driver.page_source
        while old != new:
            try:
                self.slide(lo,img_doc)
                ele = self.get_ele(loc,"查找元素")
                ele.click()
            except:
                self.Up_and_down(lo,img_doc)
                old = new
                new = self.driver.page_source
            else:
                break

    def get_blend(self):
        time.sleep(2)
        con = self.driver.contexts
        print(con)
        self.driver.switch_to.context(con[1])





