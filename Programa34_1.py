anoAtual = int(input("Digite o ano atual : "))
anoNascimento = int(input("Digite o ano nascimento : "))
idade = anoAtual - anoNascimento

print("Sua idade : ",str(idade))

if idade < 16:
    print("Não pode votar")
else:
    print("Pode votar")
