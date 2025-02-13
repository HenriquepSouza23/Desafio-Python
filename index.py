#Missão 1: Restaurando as Regras Escolares 📝 
#O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

# Solicita a nota do aluno
nota_aluno = float(input("Digite a nota do aluno: "))

# Verifica se o aluno foi aprovado, está em recuperação ou foi reprovado
if nota_aluno >= 6:
    print("O aluno foi Aprovado.")
else:  # Nota menor que 6
    if nota_aluno > 5:  # Verifica se está em recuperação
        print("O aluno está em Recuperação.")
    else:  # Nota menor ou igual a 5
        print("O aluno foi Reprovado.")