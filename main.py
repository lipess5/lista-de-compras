lista_compras = []

def adicionar():
    item_compras = input("Digite um item para adicionar ao carrinho: ").strip().title()

    lista_compras.append(item_compras)
    print(f"{item_compras} adicionado à lista!")

def remover():
    print(f"Lista atualizada: {lista_compras}")

    item_remove = input("Digite o item que deseja remover: ").strip().title()

    if item_remove in lista_compras:
        lista_compras.remove(item_remove)
        print(f"Lista atualizada com sucesso: {lista_compras}")
    else:
        print("Item não encontrado!")


while True:
    print("-- LISTA DE COMPRAS --")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar lista")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        remover()
    elif opcao == "3":
        print(f"Lista: {lista_compras}")
    elif opcao == "4":
        print("Saída com sucesso!")
        print(f"Sua lista final foi: {lista_compras}")
        break
