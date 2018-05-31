born_y = input("生まれ年を西暦４桁で入力してね")

if born_y.digit():
    if born_y.len == 4:
        print("おっけー")
    else:
        print("4桁で入力してね")
else:
    print("数字のみで入力してね")