total_feminino = 0  # contador
valor_mensalidade = 0
soma_idade_feminino = 0  # acumulador
media_idade_feminino = 0
somatorio_mensalidade = 0  # acumulador
qtd_maior_18 = 0  # contador
mat = int(input("Digite a matricula : "))
while mat != 0:
    sexo = input("Digite o sexo do bebê : ").upper()  # converto para maiuscula
    idade = int(input("Idade em meses : "))
    valor_mensalidade = float(input("Digite o valor da mensalidade :"))
    if sexo == "F":  # se for menina conto e acumulo idade
        total_feminino += 1
        soma_idade_feminino = soma_idade_feminino + idade
    else:  # se for menino acumulo o valor das mensalidade
        somatorio_mensalidade = somatorio_mensalidade + valor_mensalidade

        if idade > 18:  # acumula maiores de 18 meses
            qtd_maior_18 += 1
    mat = int(input("Digite a matricula : "))

if total_feminino > 0:  # para garantir que não haverá divisão por zero
    media_idade_feminino = soma_idade_feminino / total_feminino

print("-" * 40)
print("Media das idades das meninas.....: %.2f " % media_idade_feminino)
print("Total das mensalidades...........: %.2f " % somatorio_mensalidade)
print("Quantidade de bebes + 18 meses...: %d " % qtd_maior_18)
print("-" * 40)
print("total_feminino : ", total_feminino)
print("soma_idade_feminino ", soma_idade_feminino)