
def järjendi_korrutaja():
    
    num_list = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]
    x = int(input("Sisesta tegur:"))
    
    for num in num_list:
        print(num * x, end="\n")
        
järjendi_korrutaja()

def Euroopa_pealinnad():
    linnad1 = sorted(["Tallinn", "Riia", "Helsinki", "Brüssel", "Madrid", "Amsterdam", "Zagreb", "Reykjavik", "Ateena", "Rooma"])
    print(*linnad1, sep="\n" )
    print("Palun sisesta kask uut Euroopa pealinna.")
    
    uus_linn1 = input("Sisesta esimene pealinn:")
    uus_linn2 = input("Sisesta teine pealinn:")
    
    linnad1.append(uus_linn1)    
    linnad1.append(uus_linn2)
    
    linnad2 = sorted(linnad1.copy(), key=str.lower)
    linnade_num = len(linnad2)
    
    print(*linnad2, sep="\n")
    print(f"Meie järjendis on {linnade_num} Euroopa pealinna.")
Euroopa_pealinnad()


def sõnaraamat():
    arv = [1, 2, 3, 4]
    eesti = ['üks', 'kaks', 'kolm', 'neli']
    inglise = ['one', 'two', 'three', 'four']
    itaalia = ['uno', 'due', 'tre', 'quattro']
    
    abiarv = 0
    
    arv.append(5)
    eesti.append('viis')
    arv.append(6)
    eesti.append("kuus")
    
    for i in range(len(arv)):
        print(f"{arv[i]}-{eesti[i]}-{inglise[abiarv]}-{itaalia[abiarv]}")
        if abiarv <= 2:
            abiarv += 1
sõnaraamat()

import random

def ennustaja():
    print(f"Tere, ma oskan ennustada.\nPalun küsi minu käest jah/ei küsimusi.")
    vastused = ["Jah, kindlasti!", "Kahtlemata.", "Võite sellele loota.", "Tõenäoliselt.", "Jah", "Võib-olla!", "Vastus on udune, proovi uuesti.", "Küsi hiljem uuesti", "Keskenduge ja küsige uuesti.", "Ei oska praegu öelda.", "Ei!", "Ärge lootke sellele!", "Minu vastus on eitav!", "Minu allikad ütlevad ei!"]
    input("Mida sa soovid teada?:")
    
    juhu_vastus = random.choice(vastused)
    print(juhu_vastus)
    replay()
    
    
def replay():
    print("Kas sa soovid veel midagi küsida? [J/E]")
    reply = input()
    if reply == "J":
        ennustaja()
    elif reply == "E":
        exit()
    else:
        print("Vabandust, ma ei saanud aru. Palun vasta uuesti.")
        replay()
    
ennustaja()


def sõnaotsing():
    otsitav = input("Millist sõna otsite?:")
    sõna = ["auto", "kass", "koer", "ahv", "lamp", "tool"]
    if otsitav in sõna:
        print("Jah, see sõna on olemas")
    else:
        print("Sellist sõna ei ole.")
        sõnaotsing()
sõnaotsing()






