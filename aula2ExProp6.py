print("=========================")
print("Filé Duplo digite 1")
print("-------------------------")
print("Alcatra digite 2")
print("-------------------------")
print("Picanha digite 3")
print("-------------------------")
tipo = int(input("Qual o produto selecionado?"))
if (tipo > 0 and tipo < 4):
    peso = float(input("Quantidade do item: "))
    if (tipo == 1 and peso <= 5):
        tipo = "Filé Duplo"
        preco = round((peso * 4.90), 2)
    elif (tipo == 1) and (peso > 5):
        tipo = "Filé Duplo"
        preco = round((peso * 5.80), 2)

    elif (tipo == 2) and (peso <= 5):
        tipo = "Alcatra"
        preco = round((peso * 5.90), 2)
    elif (tipo == 2) and (peso > 5):
        tipo = "Alcatra"
        preco = round((peso * 6.80), 2)

    elif (tipo == 3) and (peso <= 5):
        tipo = "Picanha"
        preco = round((peso * 6.90), 2)
    elif (tipo == 3) and (peso > 5):
        tipo = "Picanha"
        preco = round((peso * 7.80), 2)
    else:
        print("Peso inválido")
    print("===FORMA DE PAGAMENTO===")
    print("Dineiro ou cheque DIGITE 1")
    print("-------------------------")
    print("Cartão Débito ou Crédito DIGITE 2")
    print("-------------------------")
    print("Cartão Tabajara DIGITE 3")
    print("-------------------------")
    opcao = int(input("Qual a opção de Pagamento? "))
    print("=========================")
    if (opcao > 0) and (opcao < 4):
        print ("Você está levando ", peso , "kls de " + tipo ) 
        print ("Valor total: R$ ", preco  )
        if (opcao == 3):
            desconto = round((preco * 0.1), 2) 
            print ("Desconto Especial Tabajara: R$ ", desconto )
            print ("Valor a pagar: R$ ", preco - desconto )
        else:
            print ("Desconto Especial Tabajara: Adquira Nosso Cartão!!")
            print ("Valor a pagar: R$ ", preco  ) 
        print("=========================")  
    else:
        print ("Opção inválida. Tente novamente!!")
else:
    print ("Informações inválidas. Tente novamente")
   
