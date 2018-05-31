from datetime import datetime, timedelta, date

now_dt = datetime.now()

# import ipdb; ipdb.set_trace()
# print("現在日時は "+now_dt.strftime('%Y-%m-%d %H:%M:%S')+" です")

# d = input("進めたい時間を入力してください: ")

# while True:
#     if d.isdigit() or d[0]=="-" and d[1:].isdigit():
#         if int(d) <= 9999999 and int(d) >= -9999999:
#             tmr_dt = now_dt + timedelta(hours=int(d))
#             print(str(d)+"時間後の日時は "
#                 +tmr_dt.strftime('%Y-%m-%d %H:%M:%S')+" です")
#             break
#         else:
#             d = input("7桁以内で入力してください: ")
#     else:
#         d = input("plz input on number: ")

k = input("日付を入力してください(yyyy, mm, dd): ")
k_dt = date.strftime(str(k), "%Y, %m, %d")

count = k_dt - now_dt.date()

print(count)

# while True:
#     try:
#         tmr_dt = now_dt + timedelta(days=int(d))
#         print(tmr_dt.strftime('%Y-%m-%d %H:%M:%S'))
#         break
#     except ValueError:
#         d = input("plz input on number: ")

    
        
