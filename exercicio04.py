# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).
distancia = int(input("digite a distancia"))
                   
tempo = float(input("digite o tempo"))
              
velocidade = distancia/tempo

if velocidade < 5:
   print (" voce foi lento")
elif velocidade == 5 and velocidade == 10:
   print("voce foi moderado")

