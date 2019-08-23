dia = int(input("Digite um número de 1 a 7: "))
if dia == 1:
    nome = "O número digitado corresponde à Domingo."
elif dia == 2:
    nome = "O número digitado corresponde à Segunda-feira."
elif dia == 3:
    nome = "O número digitado corresponde à Terça-feira."
elif dia == 4:
    nome = "O número digitado corresponde à Quarta-feira."
elif dia == 5:
    nome = "O número digitado corresponde à Quinta-feira."
elif dia == 6:
    nome = "O número digitado corresponde àSexta-feira."
elif dia == 7:
    nome = "O número digitado corresponde à Sábado."
else:
    nome= "A opção informada é inválida. Faça uma nova tentativa!"
print ( nome )
