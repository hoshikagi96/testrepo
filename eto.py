born_y = input("生まれ年を西暦４桁で入力してね: ")

while True:
    if born_y.isdigit():
        if len(born_y) == 4:
            eto_num = (int(born_y) + 8) % 12
            break
        else:
            born_y = input("4桁で入力してね: ")
    else:
        born_y = input("数字のみで入力してね: ")

eto_tuple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
# []ではなく（）で囲むとタプル（不変のリスト）になるよ！
eto = eto_tuple[eto_num]
print("あなたは{}年です".format(eto))