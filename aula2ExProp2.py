nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = round((nota_1 + nota_2)/ 2, 1)
print ("As notas foram = ", nota_1, "e", nota_2)
print ("A média é = ", round(media, 1))
if(media >= 9.0):
    conceito = "A"
elif ((media >= 7.5) and (media < 9)):
    conceito = "B"
elif ((media >= 6) and (media < 7.5)):
    conceito = "C"
elif ((media >= 4) and (media < 6)):
    conceito = "D"
else:
    conceito = "E"

print ("O conceito = "+ conceito)

if (media >= 6):
    print ("O aluno está Aprovado.")
else:
    print ("O aluno está Reprovado.")
