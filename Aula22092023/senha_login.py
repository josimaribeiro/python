'''
Faca um programa que peça uma senha e um login,
se a senha for:  123 e o login: admin
escreva a mensagem: "acesso permitido" caso contrário
escreva : "acesso negado"

'''

login = input("Digite o login => ")
senha = input("Digite a senha => ")
if (senha == "123" and login=="admin"):
    print("Acesso liberado")
else:
    print("Acesso negado")
