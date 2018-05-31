import re
import random
from datetime import date, time, datetime, timedelta

from calc import nengou, eto, heisei, showa

print("こんにちは、みゃーこだよ！お名前教えて～")
name = input("名前を入力してね> ")
print("{}ちゃんだねー！お話しよー".format(name))

command_file = open("pybot.txt", encoding="utf-8")
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(",")
    message = word_list[0]
    response = word_list[1]
    bot_dict[message] = response


# 曜日を定義するタプルだよ
yobi = ("月", "火", "水", "木", "金", "土", "日")

# 会話自体のループ
while True: 
    try:
        command = input("myako> ")
        response = ""
        for message in bot_dict:
            if message in command:
                response = bot_dict[message]
                break
        if "干支" in command or "なにどし" in command:
            response = eto(command)
        if "西暦" in command or "せいれき" in command:
            response = nengou(command)
        if "平成" in command:
            response = heisei(command)
        if "昭和" in command:
            response = showa(command)
        if "今日" in command:
            td = date.today()
            response = "今日は{}年の{}月{}日だよー？".format(td.year, td.month, td.day)
        if "曜日" in command:
            response = "今日は{}曜日だったはず～".format(yobi[td.weekday()])
        if "何時" in command or "時間" in command:
            nt = datetime.now()
            response = "現在時刻は{}時{}分じゃないー？".format(nt.hour, nt.minute)
        if name in command:
            response = "{}ちゃんがどうかしたのー？".format(name)
        if not response:
            response = "{}ってなに？".format(command)
        if not command:
            response = random.choice(["何か言ってよー",
                                    "終わるときはさようならしてねー",
                                    "無言なのー？"])
        print(response.format(name))

        if "さようなら" in command or "さよなら" in command or "ばいばい" in command:
            break
    except:
        response = "ごめん～なんかエラーがでたみたいー"


                         
