print("\t\t* Sistema Acadêmico *\n")

print("\t\t\t- Menu -")
print("[ 1 ] - Adicionar um novo aluno\n"
      "[ 2 ] - Editar informações já existentes\n"
      "[ 3 ] - Remover aluno existente\n"
      "[ 4 ] - Adicionar notas em aluno existente\n"
      "[ 5 ] - Adicionar a frequencia do aluno\n"
      "[ 6 ] - Mostrar todos os alunos cadastrados\n"
      "[ 7 ] - Buscar por aluno especifico\n")

op = int(input("Digite sua opção: "))
alunos = {}

if op == 1:
    cont = 0
    num = int(input("Digite a quantidade de alunos a ser incluida: "))
    while cont < num:
        nome = input(f"Digite o nome do aluno {cont+1}: ")
        alunos[f"Nome {cont+1}:"] = nome
        cont+= 1
    print(alunos)
elif op == 2:
    print("Opção 2")
elif op == 3:
    print("Opção 3")
elif op == 4:
    print("Opcão 4")
elif op == 5:
    print("Opção 5")
elif op == 6:
    print("Opcão 6")
elif op == 7:
    print("Opção 7")
else:
    print("Opção inválida")
