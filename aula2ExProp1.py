nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2)/ 2
if media < 7 :
    print("Reprovado ")
elif media > 9.7 :
    print("Aprovado com Distinção")
else:
    print("Aprovado")
