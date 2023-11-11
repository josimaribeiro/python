pet = []
pet.append("Cão")
pet.append("Gato")
pet.append("Marreco")
pet.append("Boi")

for i in pet:
    print(i)

print("_" * 30)

pet.remove("Cão")

for i in pet:
    print(i)

pet.pop(1)
print("_" * 30)
for i in pet:
    print(i)
