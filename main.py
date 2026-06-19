clientes=[]
produtos=[]
vendas=[]
materiais=[]

def cadastrarMaterial():
    nome=input("Digite o nome do material: ")
    while nome == "":
        print("Campo nome deve ser preenchido!")
        nome=input("Digite o nome do material novamente: ")
    for material in materiais:
        if material["nome"].lower() == nome.lower():
            print("Material ja cadastrado no estoque!")
            return
    categoria=input("Digite a categoria do material: ")
    quantidade=int(input("Digite a quantidade de materiais: "))
    while quantidade < 0:
        print("Quantidade inválida, digite novamente.")
        quantidade=int(input("Digite a quantidade de materiais novamente: "))
    preco=float(input("Digite o preço do material: "))
    while preco < 0:
            print("Preço inválido, digite novamente.")
            preco=float(input("Digite o preço novamente: "))
    unidade=input("Digite a unidade de medida do material: ")

    material ={
        "nome": nome,
        "categoria" : categoria,
        "quantidade" : quantidade,
        "preco" : preco,
        "unidade" : unidade
    }

    materiais.append(material)
    print("Material cadastrado com sucesso!")


def listarMaterial():
    if len(materiais)==0:
        print("Nenhum material cadastrado no estoque!")
        return
    
    print("-------MATERIAIS CADASTRADOS-------")
    for i in range (len(materiais)):
        material=materiais[i]

        print(f"--------------MATERIAL {i + 1}-----------------")
        print(f"Nome: {material['nome']}")
        print(f"Categoria: {material['categoria']}")
        print(f"Quantidade: {material['quantidade']}")
        print(f"Preço: {material['preco']}")
        print(f"Unidade de medida: {material['unidade']}")

def buscarMaterial():
    if len(materiais)== 0:
        print("Nenhum material cadastrado no estoque!")
        return
    nome=input("Digite o nome do material que você deseja procurar no estoque: ")

    while nome == "":
        print("Campo nome deve ser preenchido!")
        nome=input("Digite novamente o nome do material: ")

    for material in materiais:
        if material["nome"].lower()== nome.lower():
            print("Material encontrado!")
            print(f"Nome: {material['nome']}")
            print(f"Categoria: {material['categoria']}")
            print(f"Quantidade: {material['quantidade']}")
            print(f"Preço: {material['preco']}")
            print(f"Unidade de medida: {material['unidade']}")
            break
    else:
        print("Material não encontrado no estoque!")

def editarEstoque():
    if len(materiais) == 0:
        print("Nenhum material cadastrado no estoque!")
        return

    while True:
        print("-----------MENU EDITAR ESTOQUE------------")
        print("1 - Registrar entrada de estoque")
        print("2 - Registrar saída de estoque")
        print("3 - Atualizar o material")
        print("4 - Remover material")
        print("0 - Sair")

        opcao = int(input("Digite qual opção você deseja: "))

        match opcao:

            case 1:
                nome = input("Digite o nome do material que você deseja alterar a quantidade no estoque: ")

                while nome == "":
                    print("Campo nome deve ser preenchido!")
                    nome = input("Digite o nome do material novamente: ")

                for material in materiais:
                    if material["nome"].lower() == nome.lower():
                        print("Material encontrado no estoque!")

                        qtd = int(input("Digite a quantidade que você deseja adicionar ao estoque: "))

                        while qtd < 0:
                            print("Quantidade inválida, digite novamente!")
                            qtd = int(input("Digite novamente a quantidade: "))

                        material["quantidade"] += qtd
                        print("Estoque atualizado com sucesso!")
                        break
                else:
                    print("Material não encontrado no estoque!")

            case 2:
                nome = input("Digite o nome do material que você deseja alterar a quantidade no estoque: ")

                while nome == "":
                    print("Campo nome deve ser preenchido!")
                    nome = input("Digite o nome do material novamente: ")

                for material in materiais:
                    if material["nome"].lower() == nome.lower():
                        print("Material encontrado no estoque!")

                        qtd = int(input("Digite a quantidade que você deseja remover do estoque: "))

                        while qtd < 0:
                            print("Quantidade inválida, digite novamente!")
                            qtd = int(input("Digite novamente a quantidade: "))

                        if qtd > material["quantidade"]:
                            print("Erro: quantidade maior que o estoque!")
                        else:
                            material["quantidade"] -= qtd
                            print("Estoque atualizado com sucesso!")

                        break
                else:
                    print("Material não encontrado no estoque!")

            case 3:
                nome = input("Digite o nome do material que você deseja editar no estoque: ")

                while nome == "":
                    print("Campo nome deve ser preenchido!")
                    nome = input("Digite o nome do material novamente: ")

                for material in materiais:
                    if material["nome"].lower() == nome.lower():
                        print("Material encontrado no estoque!")

                        print("Opções de atualização:")
                        print("1 - Editar preço")
                        print("2 - Editar nome")
                        print("3 - Editar quantidade")
                        print("4 - Editar categoria")

                        sub_opcao = int(input("Digite sua escolha: "))

                        match sub_opcao:

                            case 1:
                                preco = float(input("Digite o novo preço do material: "))

                                while preco < 0:
                                    print("Preço inválido, digite novamente.")
                                    preco = float(input("Digite o novo preço novamente: "))

                                material["preco"] = preco

                            case 2:
                                novo_nome = input("Digite o novo nome do material: ")

                                while novo_nome == "":
                                    print("Campo nome deve ser preenchido!")
                                    novo_nome = input("Digite novamente: ")

                                material["nome"] = novo_nome

                            case 3:
                                quantidade = int(input("Digite a nova quantidade do material: "))

                                while quantidade < 0:
                                    print("Quantidade inválida, digite novamente.")
                                    quantidade = int(input("Digite novamente: "))

                                material["quantidade"] = quantidade

                            case 4:
                                categoria = input("Digite a nova categoria do material: ")

                                while categoria == "":
                                    print("Categoria inválida, digite novamente.")
                                    categoria = input("Digite novamente: ")

                                material["categoria"] = categoria

                            case _:
                                print("Escolha inválida!")

                        break
                else:
                    print("Material não encontrado no estoque!")

            case 4:
                print("----------REMOVER MATERIAL---------")
                nome = input("Digite o nome do material que você deseja remover: ")

                while nome == "":
                    print("Campo nome deve ser preenchido!")
                    nome = input("Digite novamente o nome do material: ")

                for material in materiais:
                    if material["nome"].lower() == nome.lower():
                        materiais.remove(material)
                        print("Material removido com sucesso!")
                        break
                else:
                    print("Material não encontrado no estoque!")

            case 0:
                print("Saindo...")
                break

            case _:
                print("Escolha inválida!")

def relatorioEstoque():
    if len(materiais) == 0:
        print("Nenhum material cadastrado no estoque!")
        return

    print("-----------------RELATÓRIO ESTOQUE------------------")

    total_itens=0
    alertas=0
    valor_total=0

    for material in materiais:
        print(f"Nome: {material['nome']}")
        print(f"Categoria: {material['categoria']}")
        print(f"Quantidade: {material['quantidade']}")
        print(f"Preço: R$ {material['preco']:.2f}")
        print(f"Unidade: {material['unidade']}")
        print("-----------------------------------")

        total_itens += 1
        valor_total += material["quantidade"] * material["preco"]

    print("\n========== RESUMO ==========")
    print(f"Total de materiais cadastrados: {total_itens}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    print("\n========== ALERTAS ==========")

    for material in materiais:
        if material["quantidade"] < 10:
            print(f" {material['nome']} está com apenas {material['quantidade']} unidades")
            alertas += 1

    if alertas == 0:
        print("Nenhum material com estoque baixo.")

    else:
        print(f"Materiais com estoque abaixo: {alertas}")

while True:

    print("=============MENU PRINCIPAL=============")
    print("1 - Cadastrar material")
    print("2 - Listar materiais")
    print("3 - Buscar material")
    print("4 - Editar estoque")
    print("5 - Relatório do estoque")
    print("0 - Sair")
    opcao=int(input("Digite qual opção você deseja: "))

    match (opcao):
        case 1:
            cadastrarMaterial()
        case 2:
            listarMaterial()
        case 3:
            buscarMaterial()
        case 4:
            editarEstoque()
        case 5:
            relatorioEstoque()
        case 0:
            print("Saindo......")
            break
        case _:
            print("Opção digitada inválida, digite novamente")