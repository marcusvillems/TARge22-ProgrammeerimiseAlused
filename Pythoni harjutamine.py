#Kirjuta programm, mis sind tervitab.

#print("Tere sina!")

#Kas oskad Pythoni abil öelda tehte 3 + 8 / (4 - 2) * 4 vastuse?

#print(3 + 8 / (4 - 2) * 4)

""" Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:

kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll
kill-koll kill-koll kill-koll kill-koll


first_kk = "kill-koll"
second_kk = "killadi-koll"
third_kk = (f"{first_kk} {first_kk} ") 
first_var_of_kk = (f"{first_kk}  {first_kk}  {second_kk} ")
second_var_of_kk = (f"{third_kk} {third_kk} ")
sum_of_kk = first_var_of_kk + first_var_of_kk + second_var_of_kk + second_var_of_kk


print(sum_of_kk)
"""


"""
Ruudu sees asub ring. Ringi raadius on 3.
Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
"""
"""
import math

r = 3

ringi_pindala = round((math.pi * r ** 2), 2)
ringi_ümbermõõt = round((2 * math.pi * r), 2)

a = (r * 2)

ruudu_pindala = (a ** 2)
ruudu_ümbermõõt = (4 * a)

print(f"Ruudu pindala: {ruudu_pindala}\n Ruudu ümbermõõt: {ruudu_ümbermõõt}\n Ringi pindala: {ringi_pindala}\n Ringi ümbermõõt: {ringi_ümbermõõt}")
"""
"""
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused
ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
""" 
"""
import math

def kujundi_arvutaja():
    
    print("Tere, mina olen ristküliku kalkulaator!\nPalun sisesta ristküliku lähisküljed.")
    
    a = float(input("Lähiskülg a: "))
    b = float(input("Lähiskülg b: "))
    
    if a <= 0 and b <= 0 or a > 0 and b <= 0 or a <= 0 and b > 0:
        print("Sellist ristkülikut pole olemas ")

    elif a and b > 0:
        S = round((a * b), 2)
        P = round((2 * (a + b)), 2)
        print(f"Ümbermõõt: {P}\nPindala: {S}")
        
kujundi_arvutaja()
"""
"""
Koosta vähemalt kümnest elemendist koosnev järjend arvudest.
Koosta programm, mis küsib kasutajalt tegurit ja korrutab kõik algses järjendis olnud arvud sellega läbi ning väljastab tulemuse ekraanile.
"""
"""
import math

def järjendi_korrutaja():
    
    num_list = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]
    x = int(input("Sisesta tegur:"))
    
    for num in num_list:
        print(num * x, end=" ")
        
järjendi_korrutaja()
"""
"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil.
"""
"""
def Euroopa_pealinnad():
    
    linnad1 = sorted(["Tallinn", "Riia", "Helsinki", "Brüssel", "Madrid", "Amsterdam", "Zagreb", "Reykjavik", "Ateena", "Rooma"])
    print(*linnad1, sep="\n" )
    
    uus_linn1 = input("Sisesta esimene pealinn: ")
    uus_linn2 = input("Sisesta teine pealinn: ")
    
    linnad1.append(uus_linn1)    
    linnad1.append(uus_linn2)
    
    linnad2 = sorted(linnad1.copy(), key=str.lower)
    
    print(*linnad2, sep="\n")

Euroopa_pealinnad()
"""


