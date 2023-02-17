from yl51_Sõnastik import inglise, itaalia
from yl53_Sõnastik import e_inglise, e_itaalia
"""
Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
"""
inglise["headaega"] = "goodbye"
inglise["pott"] = "pot"
inglise["sõnastik"] = "dictionary"

itaalia["headaega"] = "arrivederci"
itaalia["pott"] = "pentola"
itaalia["sõnastik"] = "dizionario"

e_inglise["goodbye"] = "headaega"
e_inglise["pot"] = "pott"
e_inglise["dictionary"] = "sõnastik"

e_itaalia["arrivederci"] = "headaega"
e_itaalia["pentola"] = "pott"
e_itaalia["dizionario"] = "sõnastik"

"""
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise
"""
print(f"üks -> itaalia - {itaalia['üks']}")
print(f"ciao -> eesti - {e_itaalia['ciao']}")
print(f"dog -> itaalia - {itaalia[e_inglise['dog']]}")
print(f"pentola -> inglise - {inglise[e_itaalia['pentola']]}")


