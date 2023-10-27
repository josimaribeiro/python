matricula = int(input("Digite matricula : "))

while matricula != 0:
    salarioBruto = float(input("Digite o salario : "))
    valorDesconto = salarioBruto * (9 / 100)

    salarioLiquido = salarioBruto - valorDesconto

    #print("Valor do desconto R$ {:.2f}".format(valorDesconto))
    #print("Salario liquido   R$ {:.2f}".format(salarioLiquido))

    print(f"Valor desconto  R$ {valorDesconto:.2f}")
    print(f"Salario liquido R$ {salarioLiquido:.2f}")

    matricula = int(input("Digite matricula : "))
