numeros = []


for i in range(10):
    num = int(input(f'Digite {i+1}° número: '))
    numeros.append(num)


# Ordem inversa
for i in range(9, -1, -1):
    print(numeros[i])


print('\n==================\n')


#Ordem normal
for i in range(0, 10, 1):
    print(numeros[i])
