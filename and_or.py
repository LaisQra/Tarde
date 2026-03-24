"""
> MAIOR
<MENOR 
=> MAIOR OU IGUAL
<= MENOR OU IGUAL
== IGUAL (COPARATIVO)
!= DIFERENTE
"""

print(10>5 or 10<5)


#or()
admin = "admin"
senha = "123456"

if(admin == "admin" or senha == "12345"):
    print ("Seja bem vindo")
idade = 17 
autorizacao = "sim"

if (idade >= 18 or autorizacao == "sim"):
    print("Bem vindo")

    #and

login = "admin"
senha ="123456"

if (login == "admin" and senha == "123456"):
         print ("Acesso permitido")
else:
         print ("Voce nao tem acesso permitido")

