"""
Kirjuta programm, mis analüüsib isikukoode ja väljastab võimalikult rohkem infot selle kohta (sünnikuupäev, sugu jne).
Isikukoodi käsitlege kui sümbolite kogumit ehk sõnet (kuigi see koosneb numbritest), analüüsimiseks kasutage sõneoperatsioone (vt. käsiraamat).
Kuna isikukoode on keeruline testimise ajal korduvalt sisestada, on alguses mõistlik sisestada erinevad isikukoodid ning kommenteerida vastavalt vajadusele ülearused välja.
"""


#isikukood = "60201302715"
isikukood = "48008082727"
#isikukood = "31212230156"

first_number = int(isikukood[0])
if first_number % 2 == 0:
    sex = "naine"
else:
    sex = "mees"

year_part = int(isikukood[1:3])
if first_number < 3:
    century = 1800
elif first_number < 5:
    century = 1900
else:
    century = 2000
year = century + year_part
import datetime    
month_number = int(isikukood[3:5])
    
day = int(isikukood[5:7])
birthday = datetime.datetime(year,month_number,day).strftime("%A %d %B %Y")

print(f"""Oled {sex}
Sünniaasta on {year}
Oled sündinud aasta {month_number}. kuul {day}. päeval
Sünnipäev on {birthday}
""")
    