import random

frutas = ["maçã", "banana", "laranja", "uva", "manga"]
    
print("lista de fruta:")
for i in range(len(frutas)):
    print(f"{i + 1} -{frutas[i]}")

posicao_sorteada = random.randint(1,5)

palpite = input ("qual fruta você acha que está na aposição sorteada?")

fruta_certa = frutas[posicao_sorteada-1]

if palpite.capitalize() == fruta_certa:
    print("parabéns! você acertou!")
    print(f"afruta n aposição {posicao_sorteada} era realmente {fruta_certa}.")

else:
    print("x que pena, você errou.")
    print(f"a fruta na posição {posicao_sorteada} era {fruta_certa}.")