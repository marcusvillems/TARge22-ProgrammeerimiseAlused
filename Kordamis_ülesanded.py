"""Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda
ja lisab ka tervituse järjekorranumber."""


"""name = input("Palun sisesta oma nimi:")
for i in range(5):
    print(f"Ole tervitatud, {name}, {i+1}. korda.") """

"""Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
Proovige seda ülesannet lahendada nii while- kui for-tsükliga."""



"""total = 0
for i in range(10):
    number = int(input(f"Sisesta {i+1}. täisarv: "))
    total += number
print(f" Sisestatud arvude summa on {total}")"""

"""count = 0
total = 0
while count < 10:
    num = int(input("Sisesta 10 täisarvu: "))
    num = int(num)
    total += num
    count += 1
    print(total)"""


"""total = 0
print("Küsin ja summeerin täisarve kuni tühja sisestuseni")
count = 1
while True:
    number_text = input(f"Sisesta {count}. täisarv: ")
    if number_text == "":
        break
    total += int(number_text)
    count += 1
print(f"Sisestatud arvude summa on {total}")"""



"""Koosta programm, mis aitab lastel treenida liitmist.
Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte.
Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).
Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse.

from random import randint
from Operations import Operation
correct_answers = 0
operations = int(input("Mitu korda soovid harjutada?"))
operand_min = int(input("Milline peaks olema tehtes kasutatav väikseim arv?"))
operand_max = int(input("Milline peaks olema tehtes kasutatav suurim arv?"))
precision = 0.1
print(f"Tere! Õpime arvutama. Esitan {operations} liitmistehet, püüa vastata õigesti.")
for i in range(operations):
    first_operand = randint(operand_min,operand_max)
    second_operand = randint(operand_min,operand_max)
    operator = 1 #randint(1,4)
    if operator == Operation.ADDITION: #addition
        answer = int(input(f"{first_operand} + {second_operand} = "))
        total = first_operand + second_operand
    elif operator == Operation.SUBTRACTION: #subtraction
        answer = int(input(f"{first_operand} - {second_operand} = "))
        total = first_operand - second_operand
    elif operator == Operation.MULTIPLICATION:
        answer = int(input(f"{first_operand} * {second_operand} = "))
        total = first_operand * second_operand
    elif operator == Operation.DIVISION:
        answer = float(input(f"{first_operand} / {second_operand} = "))
        total = first_operand / second_operand
    if (total - precision) < answer and answer < (total + precision):
        print("Tubli, õige vastus!")
        correct_answers += 1
    else:
        print(f"Sinu vastus polnud õige. Õige vastus on {total}.")
print(f"See oli viimane ülesanne. Kogusid {operations}-st punktist {correct_answers}.")        
   """   








              