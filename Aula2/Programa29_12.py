"""
Para converter graus Celsius em graus Fahrenheit, multiplique por 1,8 e adicione 32.

°F = °C × 1, 8 + 32

Para converter graus Fahrenheit em graus Celsius, subtraia 32 e divida por 1,8.

°C = (°F − 32) ÷ 1, 8
"""


f = float(input("Digite a temperatura em graus Fahrenheit  : "))
c = (f - 32) / (1.8)
print(f, " Fahrenheit é  Celcius é %.2f" %  c)
print(f, " Fahrenheit é  Celcius é ", round(c,2))

c = float(input("Digite a temperatura em graus Celcius  : "))
f = (c * 1.8) + 32

print(c, " Fahrenheit é  Fahrenheit é %.2f" %  f)
print(c, " Fahrenheit é  Fahrenheit é ", round(f,2))

