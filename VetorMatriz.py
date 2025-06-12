alunos = ["Alice", "bruno", "carla"]

dias = ["seg", "ter", "quar", "qui"]

reservas = [["ausente" for _ in dias] for _ in alunos]
      print("preencha com 's'para presença e 'x'para ausência:")

for i, aluno in enumerate(alunos):
      print(f"\nAluno: {aluno}")
    
