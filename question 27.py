totalAlunos = 0
turmas = int(input("Quantidade de turmas: "))

for i in range(turmas):
    alunos = int(input(f"Alunos na turma {i+1}: "))
    while alunos > 40:
        print("A turma não pode ter mais de 40 alunos.")
        alunos = int(input(f"Alunos na turma {i+1}: "))
    totalAlunos += alunos

media = totalAlunos / turmas
print( f"Média de alunos por turma: {media}")
