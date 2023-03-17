"""BMI calculator"""
from Erindid import *

try:
    age,height,weight = ask_values()
except AgeInvalid:
    print("Sisestasid oma vanuse valesti.")
    
except HeightInvalid:
    print("Sisestasid pikkuse valesti.")
    
except WeightInvalid:
    print("Sisestasid oma kehakaalu valesti.")

else:
    print(f"Sinu kehamassiindeks on {CalculateBMI(height,weight)}")


