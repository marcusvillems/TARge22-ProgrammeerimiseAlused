from yl51_Sõnastik import inglise,itaalia
"""
Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia),
mille võti ei ole mitte eesti keeles,
vaid vastavalt kas inglise või itaalia keeles.
Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad.

e_inglise[inglise["auto"]] = "auto".
"""



e_inglise = {}
e_itaalia = {}

for key,value in inglise.items():
    e_inglise[value] = key
    
for key,value in itaalia.items():
    e_itaalia[value] = key

if __name__ == "__main__":
    print(e_inglise,"\n",e_itaalia)

    




