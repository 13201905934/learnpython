# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="应用中心").click()
# 睡眠2秒
sleep(2)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child(
    "android.widget.FrameLayout").offspring("应用").click()
# 睡眠2秒
sleep(2)
# 点击网易云
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child(
    "android.widget.FrameLayout").offspring("com.mumu.store:id/main_pager").offspring(
    "androidx.recyclerview.widget.RecyclerView").child("android.view.ViewGroup")[0].child(
    "com.mumu.store:id/iv_icon").click()
if poco("com.mumu.store:id/tv_tab").exists():
    # 点击返回
    poco("com.mumu.store:id/btn_go_back").click()
