import json

def menu():
    print("\n\t\t* Sistema Acadêmico *\n")

    print("\t\t\t- Menu -")
    print("[ 1 ] - Adicionar um novo aluno\n"
          "[ 2 ] - Editar informações já existentes\n"
          "[ 3 ] - Remover aluno existente\n"
          "[ 4 ] - Adicionar notas em aluno existente\n"
          "[ 5 ] - Adicionar a frequencia do aluno\n"
          "[ 6 ] - Mostrar todos os alunos cadastrados\n"
          "[ 7 ] - Buscar por aluno especifico\n"
          "[ 8 ] - Sai do programa\n")
    return input("Escolha uma opção: ")

def adicionar_aluno():
    nome = input("Digite o nome do usuário: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    with open("alunos.txt", "a") as file:
        file.write(f"{nome}, {nota1}, {nota2}, {nota3}, {nota4}\n")
    print("Aluno cadastrado com sucesso!")

def editar_aluno():
    try:
        with open("alunos.txt", "r") as file:
            alunos = file.readlines()
        if not alunos:
            print("Nenhum aluno cadastrado")
            return

        print("\n === Lista da Alunos Cadastrados ===")
        for i, linha in enumerate (alunos):
            nome, nota1, nota2, nota3, nota4 = linha.strip().split(",")
            print(f"{i + 1}. Nome:{nome}, Nota 1: {nota1}, Nota 2: {nota2}, Nota 3: {nota3}, Nota 4: {nota4}")

        indice = int(input("\nDigite o Numero do aluno que deseja editar: ")) - 1

        if indice < 0 or indice >= len(alunos):
            print("Número inválido")
            return

        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o mesmo): ")
        nova_nota1 = float(input("Digite a nova nota 1 (ou pressione Enter para manter a mesma): "))
        nova_nota2 = float(input("Digite a nova nota 2 (ou pressione Enter para manter a mesma): "))
        nova_nota3 = float(input("Digite a nova nota 3 (ou pressione Enter para manter a mesma): "))
        nova_nota4 = float(input("Digite a nova nota 4 (ou pressione Enter para manter a mesma): "))

        nome_antigo, nota1, nota2, nota3, nota4 = alunos[indice].strip().split(",")
        novo_nome = novo_nome if novo_nome else nome_antigo
        nota_nota1 = nova_nota1 if nova_nota1 else nota1
        nova_nota2 = nova_nota2 if nova_nota2 else nota2
        nova_nota3 = nova_nota3 if nova_nota3 else nota3
        nova_nota4 = nova_nota4 if nova_nota4 else nota4

        alunos[indice] = f"{novo_nome}, {nova_nota1}, {nova_nota2}, {nova_nota3}, {nova_nota4}\n"

        with open ("alunos.txt", "w") as file:
            file.writelines(alunos)

        print("Aluno atualizado com sucesso!")

    except FileNotFoundError:
        print("Nenhum aluno cadastrado")
    except ValueError:
        print("Entrada inválida. Tente novamente")

def remover_aluno():
    try:
        with open("alunos.txt", "r") as file:
            alunos = file.readlines()

            if not alunos:
                print("Nenhum aluno cadastrado")
                return

            if alunos:
                print("\n=== Lista de Alunos Cadastrados ===")
                for i, linha in enumerate(alunos):
                    dados = linha.strip().split(",")
                    nome = dados[0]
                    notas = ", ".join(dados[1:])
                    print(f"{i+1}. {nome}, Notas: {notas}")

                indice = int(input("\nDigite o Nº do aluno que deseja remover: ")) - 1

                if indice < 0 or indice >= len(alunos):
                    print("Número inválido")
                    return

                alunos.pop(indice)

        with open("alunos.txt", "w") as file:
            file.writelines(alunos)

        print("Aluno removido com sucesso!")

    except FileNotFoundError:
        print("Nenhum aluno foi cadastrado ainda")
    except ValueError:
        print("Entrada inválida. Tente novamente...")

def visualizar_alunos():
    try:
        with open ("alunos.txt", "r") as file:
            alunos = file.readlines()
            if alunos:
                print("\n\t\t=== Lista de Alunos ===\n")
                for linha in alunos:
                    dados = linha.strip().split(",")
                    nome = dados[0]
                    notas = ", ".join(dados[1:])
                    print(f"Nome: {nome}, Notas:{notas}")
            else:
                print("Nenhum aluno cadastrado")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado ainda")

def main():
    while True:
        opcao = menu()
        if opcao == "1":            # Adicionar alunos
            adicionar_aluno()
        elif opcao == "2":          # Editar informações já existentes
            editar_aluno()
        elif opcao == "3":          # Remove aluno existente
            remover_aluno()
        elif opcao == "4":          # Adiciona notas
            print("Opcão 4")
        elif opcao == "5":          # Adiciona a frequência
            print("Opção 5")
        elif opcao == "6":          # Mostra a situação dos alunos cadastrados
            visualizar_alunos()
        elif opcao == "7":          # Busca por um aluno
            print("Opção 7")
        elif opcao == "8":          # Sai do programa
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
