"""
Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles,
kui morse koodina ja lubab seejärel kasutajal sisestada sõnu ning
teisendab need sümbolhaaval morsetähestikku (lisades iga sümboli järele tühiku).
Sõnastik ei pruugi sisaldada kõikvõimalikke märke,
seega tuleb iga sümboli puhul kontrollida, kas see üldse esineb sõnastikus.
Tähe registrit ehk suur- ja väiketähti ei eristata.
Samuti tuleb otsustada, mida ette võtta nende tähtedega,
mida inglise tähestikus pole (näiteks "õ", "ä" jne):
ignoreerida või mõned neist teisendada (näiteks "õ" -> "o" vms).

Programm võiks küsida kasutajalt sõnu kas mingi arv kordi või töötada lõpmatult,
kuni kasutaja sõna ei sisesta, vaid vajutab lihtsalt sisestusklahvile.
"""


alphabet = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
m_alphabet = {v:k for k, v in alphabet.items()}
def text_to_morse(text):
    morse = []
    for symbol in text.lower():
        if symbol in alphabet:
            morse.append(alphabet[symbol])
        else:
            morse.append("X")
    return " ".join(morse)


def morse_to_text(morse):
    message = []
    morse_list = morse.split(" ")
    for character in morse_list:
        if character in m_alphabet:
            message.append(m_alphabet[character])
        else:
            morse.append(" ")
        return " ".join(message)



print("Tere: ",end="")
print(text_to_morse("Tere")) #  - . .-. .


while True:
    message = input("Sisesta oma sõnum, mida morse koodi teisendada: ")
    if message == "":
        break
    print(text_to_morse(message))
    print("Sisesta kontrolliks morse kood: ")
    print(morse_to_text(input()))