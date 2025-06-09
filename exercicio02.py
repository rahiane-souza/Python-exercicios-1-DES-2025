#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
tempo1 = int(input("digite o tempo nessesário para a tividade1"))
tempo2 = int(input("digite o tempo nessesário para a tividade2"))
tempo3 = int(input("digite o tempo nessesário para a tividade3"))

soma = tempo1 + tempo2 + tempo3
if tempo1 < 0 or tempo2 < 0 or tempo3 < 0:
    print ("erro número negativo.")
else:
    soma = tempo1 + tempo2 + tempo3
print(f"tempo total do projeto:{soma} dias")
