nome = input("Digite seu nome : ")
salarioBruto = float(input("Digite o salario : "))

desc8 = salarioBruto * (8 / 100)
salarioLiq = salarioBruto - desc8

print(f"O desconto foi de {desc8}, o salario liquido ficou em {salarioLiq}")
