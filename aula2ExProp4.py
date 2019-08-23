num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
print("=========================")
print("Para somar digite 1")
print("-------------------------")
print("Para subtrair digite 2")
print("-------------------------")
print("Para multiplicar digite 3")
print("-------------------------")
print("Para dividir digite 4")
print("=========================")
operacao = int(input("Qual a sua escolha? "))
print("=========================")
if ((operacao > 0) and (operacao < 5)):
    if operacao == 1:
        nome = "soma"
        result = num_1 + num_2
    elif operacao == 2:
        nome = "subtração"
        result = num_1 - num_2
    elif operacao == 3:
        nome = "multiplicação"
        result = num_1 * num_2
    else:
        nome = "divisão"
        result = num_1 / num_2
    print("O Resultado da " + nome + " entre " , num_1 , " e ", num_2, " é = ", result)

    if (result % 2 == 0):
        a = "é par,"
        c = "inteiro"
    elif (result % 2 == 1):
        a = "é ímpar,"
        c = "inteiro"
    else :
        a = "não é par, nem ímpar é"
        c = "decimal"

    if (result >= 0):
        b = "positivo"
    else :
        b = "negativo"

    print("O número", result, a + " " + c +  " e " + b +  "." )
else:
    print("A opção informada é inválida")
    print("Faça uma nova tentativa.")
