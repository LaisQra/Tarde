#Lais_Atividade

nota1 =  float (input("Qual nota do primeiro aluno"))
nota2 =  float (input("Qual nota do segundo aluno"))
nota3 =  float (input("Qual nota do terceiro aluno"))
nota4 =  float (input("Qual nota do quarto aluno"))

Resultado =  (nota1 + nota2 + nota3 + nota4)/4
print(f"A média das notas é :{Resultado:.2f}")


if (Resultado >= 7):
    print("Aluno Aprovado")
elif (Resultado < 7):
   print ("Aluno está recuperação")
elif (Resultado < 5):
   print ("Aluno está reprovado")



                 
























