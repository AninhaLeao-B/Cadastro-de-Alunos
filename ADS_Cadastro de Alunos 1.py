tabela = {}

print(tabela)

nome = input("Digite o nome do Aluno: ")
tabela['Nome:'] = nome

cont = 0
while cont < 4:
    nota = float(input(f"Digite a nota {cont+1}: "))
    tabela[f"Nota {cont+1}"] = nota
    cont+= 1

print(tabela)


