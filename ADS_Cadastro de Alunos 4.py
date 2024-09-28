import json

def carregar_dados():
    try:
        with open ("alunos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvar_dados(alunos):
    with open("alunos.json", "w") as file:
        json.dump(alunos, file, indent=4)

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    if nome in alunos:
        print("aluno já cadastrado")
        return
    alunos[nome] = {"notas": [], "Frequencia": 0}
    salvar_dados(alunos)
    print("Aluno adicionado com sucesso")

def editar_aluno():
    nome = input("Digite o nome do aluno a ser editado: ").strip()
    if nome not in alunos:
        print("Aluno não encontrado")
        return

    elif nome in alunos:
        novo_nome = input("Digite o novo nome do aluno: ").strip()
        alunos[novo_nome] = alunos.pop(nome)
        salvar_dados(alunos)
        print("Aluno editado com sucesso!")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ").strip()
    if nome in alunos:
        del alunos[nome]
        salvar_dados(alunos)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado")

def adicionar_notas():
    nome = input("Digite o nome do aluno: ").strip()
    if nome not in alunos:
        print("Aluno não encontrado")
        return
    try:
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome]["notas"].append(nota)
        salvar_dados(alunos)
        print("Nota adicionada com sucesso!")
    except ValueError:
        print("NOta inválida. Tente novamente...")

def editar_notas():
    nome = input("Digite o nome do aluno: ").strip()
    if nome not in alunos:
        print("Aluno não encontrado")
        return
    try:
        notas = alunos[nome]["notas"]
        if not notas:
            print("Não existem notas cadastradas nesse aluno")
            return
        print("Notas existentes:", notas)
        indice = int(input("Digite o número da nota que você deseja editar(começando em 1): "))
        if indice < 0 or indice >= len(notas):
            print("Indice inválido")
            return
        nova_nota = float(input("Digite a nova nota: "))
        alunos[nome]["notas"][indice] = nova_nota
        salvar_dados(alunos)
        print("Nota editada com sucesso!")
    except ValueError:
        print("Entrada inválida...")

def adicionar_frequencia():
    nome = input("Digite o nome do aluno: ").strip()
    if nome not in alunos:
        print("Aluno não encontrado")
        return
    try:
        cargahoraria = int(input("Digite a Carga Horária do aluno: "))
        faltas = int(input("Digite o número de faltas do aluno: "))
        Frequencia = cargahoraria - ((faltas*100)/cargahoraria)
        alunos[nome]["Frequencia"] = Frequencia
        salvar_dados(alunos)
        print("Frequência adicionada com sucesso!")
    except ValueError:
        print("Entrada inválida")

def mostrar_cadastrados():
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, dados in alunos.items():
        media = sum(dados["notas"]) / len(dados["notas"]) if dados["notas"] else 0
        if media >= 7 and dados["Frequencia"] >= 75:
            situacao = "Aprovado"
        elif media >= 7 and dados["Frequencia"] < 75:
            situacao = "Reprovado por falta"
        else:
            situacao = "Reprovado por média"
        print(f"Nome: {nome}, Média: {media:.2f}, Frequência: {dados['Frequencia']}%, Situação: {situacao}")

def buscar_aluno():
    nome = input("Pesquisar aluno: ")
    if nome not in alunos:
        print("Aluno não encontrado.")
        return
    dados = alunos[nome]
    media = sum(dados["notas"]) / len(dados["notas"]) if dados["notas"] else 0
    if media >= 7 and dados["Frequencia"] >= 75:
        situacao = "Aprovado"
    elif media >= 7 and dados["Frequencia"] < 75:
        situacao = "Reprovado por falta"
    else:
        situacao = "Reprovado por média"
    print(f"Nome: {nome}, Média: {media:.2f}, Frequência: {dados['Frequencia']}%, Situação: {situacao}")

def menu():
    while True:
        print("\n=== Cadastro Acadêmico ===\n"
              "\n[ 1 ] - Adicionar aluno"
              "\n[ 2 ] - Editar aluno"
              "\n[ 3 ] - Remover aluno"
              "\n[ 4 ] - Adicionar notas"
              "\n[ 5 ] - Editar notas"
              "\n[ 6 ] - Adicionar frequencia"
              "\n[ 7 ] - Mostrar situação dos alunos"
              "\n[ 8 ] - Buscar por aluno"
              "\n[ 9 ] - Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            editar_aluno()
        elif opcao == "3":
            remover_aluno()
        elif opcao == "4":
            adicionar_notas()
        elif opcao == "5":
            editar_notas()
        elif opcao == "6":
            adicionar_frequencia()
        elif opcao == "7":
            mostrar_cadastrados()
        elif opcao == "8":
            buscar_aluno()
        elif opcao == "9":
            print("saindo...")
            break
        else:
            print("Opção inválida. Tente novamente...")

alunos = carregar_dados()
menu()
