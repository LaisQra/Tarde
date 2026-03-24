
#Laís_Atividade
operacao = input("Digite a Operacão desejada:\n""(+,-,/,%,**):")
                 
numero1 = float (input("Digite o primeiro numero"))
numero2 = float(input ("Digite o primeiro numero"))


if (operacao == "+"):
     print(f"{numero1} + {numero2} = {numero1+numero2}")
elif (operacao == "-"):
    print(f"{numero1} - {numero2} = {numero1-numero2}")
elif (operacao == "/"):
     print(f"{numero1} / {numero2} = {numero1/numero2}")
elif (operacao == "*"):
     print(f"{numero1} * {numero2} = {numero1*numero2}")
elif (operacao == "%"):
     print(f"{numero1} % {numero2} = {numero1%numero2}")
elif (operacao == "**"):
     print(f"{numero1} **{numero2} = {numero1**numero2}")
else:
    print("Operação Invalida")
    













