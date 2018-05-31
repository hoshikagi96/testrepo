import re

def nengou(command):
    if re.search(r"\d{4}", command):
        year_sr = re.search(r"\d{4}", command)
        year = int(year_sr.group())
        if year >=1989 and year <= 2018:
            hs = year - 1988
            response = "平成{}年でしょー？".format(hs) 
        elif year >=1926:
            sw = year - 1925
            response = "昭和{}年のことー？".format(sw)   
        elif year > 2018:
            response = "未来の話だね～"   
        else:
            response = "昔の話はわからないなー"
    else:
        response = "なになに？いつの話？"
    return response

def heisei(command):
    if re.search(r"\d+", command):
        year_hs = re.search(r"\d+", command)
        year_h = int(year_hs.group())
        if year_h <=30:
            sr = year_h + 1988
            response = "西暦{}年のことだね！".format(sr)
        else:
            response = "平成終わっちゃってるよ～" 
    else:
        response = "平成何年の話ー？"
    return response

def showa(command):
    if re.search(r"\d+", command):
        year_sw = re.search(r"\d+", command)
        year_s = int(year_sw.group())
        if year_s <=64:
            sr = year_s + 1925
            response = "西暦{}年のことですね～！".format(sr)
        else:
            response = "昭和は64年までだよねー？" 
    else:
        response = "昭和って昔だね～"
    return response

def eto(command):
    eto_tuple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
    eto_msg = ("チュー","モーモー","がおー","うさこ年！","ふぁいやー","ぱいそん？",
               "ぱからっ","メェ～","かとうです！ウキー","こけこっこ～","めぐっちょわんっ","みゃーことおそろい！")
    if re.search(r"\d{4}", command):
        year_eto = re.search(r"\d{4}", command)
        year_e = int(year_eto.group())
        eto_num = (int(year_e) + 8) % 12
        eto = eto_tuple[eto_num]
        eto_m = eto_msg[eto_num]
        response = "{}年生まれの干支は{}だね～ {}".format(year_e, eto, eto_m)
    else:
        response = "みゃーこは亥年だよー"
    return response

