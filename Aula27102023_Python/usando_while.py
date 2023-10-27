matricula = int(input("Digite matricula"))

while matricula != 0:
    total_vendas = float(input("Digite suas vendas :"))
    comissao = total_vendas * 3 / 100
    print('Sua comissão é...: {:.2f}'.format(comissao))
    matricula = int(input("Digite matricula"))
    # fim do while

print("Fim")
