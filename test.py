from configparser import ConfigParser
from datetime import date, datetime
from time import localtime, sleep, time
import pyautogui
import pyperclip
import schedule

week = {
    "Monday": "星期一",
    "Tuesday": "星期二",
    "Webnesday": "星期三",
    "Thursday": "星期四",
    "Friday": "星期五",
    "Saturday": "星期六",
    "Sunday": "星期天",
}

beds = {
    1: "李宇航",
    2: "吴志锋",
    3: "文件传输助手",
    4: "张建宇",
    5: "杨金辉",
}


cfg = ConfigParser()
cfg.read("./test.cfg", encoding="utf-8")


def log(msg: str) -> None:
    with open("./log.txt", encoding="utf8", mode="a") as log:
        log.write(msg)


def getWeek() -> str:
    return week[datetime.now().strftime("%A")]


def getTodayMsg() -> tuple:
    today = 0
    msg = ""
    last_seq = int(cfg.get("test", "last_seq"))
    today = last_seq % 5 + 1
    msg = f"今天是{getWeek()}，上一次是{last_seq}号床，所以这次轮到{today}号床"
    cfg.set("test", "last_seq", str(today))

    return (today, msg)


def 吴学钊不在的世界():
    # 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    sleep(3)

    # 打开搜索栏
    pyautogui.hotkey('ctrl', 'f')
    sleep(3)

    # 搜索名字
    todayMsg = getTodayMsg()
    pyperclip.copy(beds[todayMsg[0]])
    pyautogui.hotkey('ctrl', 'v')
    sleep(3)

    # 选择用户
    pyautogui.hotkey('Enter')
    sleep(5)

    # 粘贴消息
    pyperclip.copy(
        todayMsg[1] + "\n【来自107宿舍倒垃圾提醒小助手，该消息由脚本自动生成，具体代码在https://www.github.com/esgloamp/TheWorldWithoutWXZ】")
    pyautogui.hotkey('ctrl', 'v')

    # 发送消息
    pyautogui.hotkey('Enter')

    with open("./test.cfg", "w", encoding="utf-8") as file:
        cfg.write(file)

    log(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S %a')} -> {todayMsg[1]}\n")


schedule.every().day.at("21:30").do(吴学钊不在的世界)

while True:
    schedule.run_pending()
    sleep(1)

###########################test##############################
# last_3 = 4
# last_seq = 1
# day = 2
# for i in range(10):
#     for day in range(1, 8, 1):
#         if day == 3:
#             last_3 = last_3 % 5 + 1
#             print("wed", last_3)
#         else:
#             last_seq = last_seq % 5 + 1
#             print("last_seq", last_seq)
#     print("end of week")
############################################################
