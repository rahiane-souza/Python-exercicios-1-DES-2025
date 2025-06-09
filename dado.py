import random

input("pressione o enter para lançar o dado")

resultado = random.randint(1,6)

print (f"0 dado roulou: {resultado}");
if resultado > 6:
    print("você é fara!")
    elif resultado <