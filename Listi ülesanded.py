"""
words = ["ahv", "kass", "auto", "koer"]
search_string = input("Sisesta otsitav sõna: ")

for element in words:
    if search_string.lower() in element.lower():
        print(f"Sinu otsitav sõna on järgmistes elementides:\n{element}")
"""


"""
Loo järjend, milles on ülikooli vastuvõetud õpilaste arvud aastatel 2011-2022.
Küsige kasutajalt aastaarv, mis teda huvitab ja
väljastage sellel aastal vastuvõetud õpilaste arv.
"""
"""
accepted = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
year = int(input("Sisesta aastaarv, mis sind huvitab (2011-2022): "))
index = year - 2011
if index >= 0 and index < len(accepted):
    print(f"Aastal {year} võeti vastu {accepted[index]} õpilast.")
else:
    print("Antud aasta kohta andmed puuduvad.")
"""
"""
num_of_laps = int(input("Mitu ringi jooksid: "))
carrots = 0
for laps in range(2, num_of_laps + 1, 2):
        carrots += laps
print(f"Preemiaks saad {carrots} porgandit")
"""

"""
Küsi kasutajalt arve kuni tühja sisestuni.
loo järjend, kus on arvud väiksemaist arvust suurimani.
Kuva ekraanile iga kolmas arv järjendis.

Näiteks: sisendid -7, 5, 9, 12
järjend [5,6,7,8,9,10,11,12]
print 5,8,11
"""
"""
numbers = []
while True:
    answer = input("Sisesta arv: ")
    if answer == "":
        break
    
    numbers += [int(answer)]
smallest = min(numbers)
largest = max(numbers)
num_list = list(range(smallest,largest+1))
for i in range(len(num_list)):
        if i % 3 == 0:
            print(num_list[i])
"""
"""
Küsi looma nimesid kuni tühja sisestuni.
Kuva sama tähega algavate loomade kõige pikemad nimed.

Näiteks:
Sisend -< Karu, kass, koaala, siil, saarmas, rebane

Tulem ->
K - Koaala
S - Saarmas
R - Rebane
"""

animals = []
while True:
    answer = input("Sisesta loom: ")
    if answer == "":
        break
    






























