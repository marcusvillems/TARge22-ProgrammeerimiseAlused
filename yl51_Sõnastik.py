"""
Loo kaks sõnastikku (inglise, itaalia) ja anna neile väärtused (nagu järjendite ülesandes).
Miks on seekord ainult kaks sõnastikku?

Lisa sõnastikku järgmised sõnad:

eesti - auto, itaalia - auto, inglise - car
eesti - koer, itaalia - cane, inglise - dog
eesti - kass, itaalia - gatto, inglise - cat
eesti - tere, itaalia - ciao, inglise - hello
"""

inglise = {"üks" : "one","kaks":"two","kolm":"three","neli":"four"}
itaalia = {"üks" : "uno","kaks":"due","kolm":"tre","neli":"quattro"}
inglise["auto"] = "car"
itaalia["auto"] = "auto"
inglise.update({"koer":"dog"})
itaalia.update({"koer":"cane"})
inglise.setdefault("kass","cat")
itaalia.setdefault("kass","gatto")
inglise["tere"] = "hello"
itaalia["tere"] = "ciao"

if __name__ == "__main__":
    print(inglise, "\n",itaalia)
    
    

    
    
    
    
    