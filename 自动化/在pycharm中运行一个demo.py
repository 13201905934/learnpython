# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()


# 写一个返回主页的函数
def back_main():
    for i in range(2):
        poco("btn_back").click()
    if poco("btn_start").exists():
        print("已经返回主界面")


# 主界面开始start函数
def start():
    poco("btn_start").click()
    sleep(1)
    value_name = poco("basic").attr("name")
    assert_equal(value_name, "basic", "已经进入开始页面.")


# 点击操作
start()

poco("basic").click()
sleep(1)
if poco("star_single").exists():
    print("已经进入Basic Test页面")

# 点击星星
poco("star_single").click()
sleep(1)

# 长点击星星
poco("star_single").long_click()
sleep(1)
# 点击文本框
poco("Placeholder").click()
sleep()
# 激活输入光标
poco("pos_input").click()
sleep(2)
# 输入文本
poco("pos_input").set_text("译文晚上好！")
sleep(1)
# 返回开始主界面
back_main()

# 测试滑动
# 点击操作
start()
sleep(1)
poco("list_view").click()
if poco("title").exists():
    print("进入listView页面")
sleep(1)
# 滑轮向下滑动0.2个单位
poco("Handle").swipe([0, 0.2])
sleep(1)

# 滑轮向上滑动0.2个单位
poco("Handle").swipe([0, -0.2])
sleep(1)

# 滑轮向下滑动0.1个单位
poco("Handle").swipe("down")
sleep(1)

# 滑轮向上滑动0.1个单位
poco("Handle").swipe("up")
sleep(1)
back_main()

# 点击操作
start()
poco("drag_and_drop").click()
sleep(2)
# 拖拽星星
poco("playDragAndDrop").child("star")[0].drag_to(poco("shell"))
sleep(1)

poco("playDragAndDrop").child("star")[2].drag_to([0.504, 0.705])
sleep(1)
back_main()
sleep(1)
# 内部偏移练习
poco("btn_start").click()
sleep(1)
value_name = poco("basic").attr("name")
assert_equal(value_name, "basic", "已经进入开始页面.")

# 使用focus
poco("local_positioning").click()
sleep(1)
paer = poco(texture="icon")
paer.focus("center").long_click()
sleep(1)
# 左部中间
paer.focus([0.25, 0.25]).long_click()
sleep(1)
# 右下中间
paer.focus([0.9, 0.9]).long_click()
sleep(1)

amd = poco(text="pearl")
# 在peal上方点击，此时y为负数
amd.focus([0.5, -3]).long_click()
sleep(1)
# 返回主页
back_main()

sleep(1)

# 测试wait等待事件，等待10s,鸡蛋的控件出现后进行长按,没有出现也不会报错
start()
poco("local_positioning").click()
sleep(1)
poco(texture="icon").wait(timeout=10).long_click()
back_main()

# 测试wait_for_appearance()和wait_for_disappearance()， 不满足则报错,默认时间为120秒
start()
poco("wait_ui").click()
sleep(1)
# 等待炸弹出现
poco("jump_end").wait_for_appearance(timeout=20)

# 等待计分板消失
# poco(text="Count:").wait_for_disappearance(timeout=3) 计分板不会消失，会报错
# 返回主页
back_main()

# wait_for_any()和wait_for_all()。与上述等待事件不同的是，wait_for_any() 和 wait_for_all() 可以给定多个UI对象让其等待
start()
poco("wait_ui").click()
sleep(1)

yellow = poco("yellow")
blue = poco("blue")
black = poco("black")
# 在超时时长结束之前，需要 等待所有给定的UI对象都显示出来
# poco.wait_for_all([yellow,blue,black])
poco.wait_for_all([yellow])

# 返回主页
back_main()

