# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("com.mumu.store")
sleep(1.0)
sleep(2)
real_value = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
    "android:id/content").child("android.widget.FrameLayout").offspring("推荐").child("android.widget.TextView").attr(
    "text")
print(real_value)
assert_equal(real_value, "推荐", "已经进入应用市场页面")
sleep(2)
poco(text="游戏").click()
sleep(2)
# swipe(Template(r"tpl1672937316665.png", record_pos=(-0.247, -0.148), resolution=(1600, 900)), vector=[-0.1295, 0.27])
keyevent("BACK")
sleep(1)
keyevent("BACK")
