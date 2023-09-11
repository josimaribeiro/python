secret_word = "123"
counter = 0
conseguiu = False
while True:
    word = input("Enter the secret word: (3 tentativas)").lower()
    counter = counter + 1
    if word == secret_word:
        conseguiu = True
        break
    if word != secret_word and counter > 3:
        conseguiu = False
        break

if conseguiu:
    print("Conseguiu na ", counter, " tentativa")
else:
    print("Limite de tentativas  excedido")
