# -*- encoding=utf8 -*-
__author__ = "admin"

import time

from airtest.core.api import *
# 取消脚本执行中打印大量log信息
import logging
# 导入报告模块
from airtest.report.report import simple_report

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
# 日志级别有 DEBUG INFO WARNING ERROR

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app("com.mumu.store")
sleep(3)
# 进入游戏界面
poco(text="游戏").click()
sleep(1)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child(
    "android.widget.FrameLayout").offspring("com.mumu.store:id/main_pager").offspring(
    "com.mumu.store:id/rv_app_list").child("android.view.ViewGroup")[0].child("com.mumu.store:id/iv_icon").click()
sleep(2)
# 返回
poco("com.mumu.store:id/btn_go_back").click()

# 生成报告
simple_report(__file__, logpath=True)

# 获取系统当前时间
# time.strftime("%d", time.localtime(time.time()))
