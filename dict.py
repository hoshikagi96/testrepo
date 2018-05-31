point_dict = {
    "001" : (100, 65, 89),
    "002" : (96, 71, 78),
    "003" : (88, 79, 67),
    "004" : (60, 100, 76)
}

for stu_id in point_dict:
    points = point_dict[stu_id]
    subject = len(points)
    # 教科数を取得
    japanese, engrish, mathmatics = points 
    # pointsはタプル型。順番に代入するよ！
    total = japanese + engrish +mathmatics

    if total >= subject * 100 * 0.8:
        evalu = "Excellent!!!"
    elif total >= subject * 100 * 0.65:
        evalu = "Good!"
    else:
        evalu = "Bad"

    print("学籍番号{}の合計点は{}、評価は{}です。".format(stu_id, total, evalu))


