for i in range(0,3):
    nome = input("Digite o nome  do funcionario  : ")
    salarioBruto = float(input("Digite o salario : "))
    valorDesconto = salarioBruto * 8 / 100
    salarioLiquido = salarioBruto - valorDesconto
    print("O desconto foi ", valorDesconto)
    print("O salario liquido é ", salarioLiquido)


