# Missão 9: Calculando Dobro de um Número 🛠️

# Os alunos precisam de um programa que ajude em cálculos rápidos.
#  
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
#  Exemplo: dobro(5)
#  Saída: "O dobro de 5 é 10"

def dobro(numero):
    return 2 * numero

numero = float(input("Digite um número: "))
resultado = dobro(numero)

print(f"O dobro de {numero} é {resultado}")