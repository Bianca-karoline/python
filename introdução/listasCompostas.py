'''teste = list()
teste.append('Gustavo')
teste.append(33)
galera = list()
#Dois pontos no colchetes para copiar a lista e não criar uma ligação entre elas
#Se não usar só irá contar a última modificação
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)
print(galera[1][1])'''
'''temp = list()
pessoas = list()
s = ''
menor = maior = 0
while True:
    if len(pessoas) == 0:
        temp.append(str(input('Digite o nome: ')))
        temp.append(int(input('Digite o peso: ')))
        pessoas.append(temp[:])
    else:
        temp[0] = str(input('Digite o nome: '))
        temp[1] = int(input('Digite o peso: '))
        pessoas.append(temp[:])
    if len(pessoas) == 1:
        maior = menor = temp[1]
    if maior<temp[1]:
        maior = temp[1]
    if menor>temp[1]:
        menor = temp[1]
    s = str(input("Deseja continuar?[S/N]"))
    if s in "nN":
        break
print(f'Ao todo você cadastrou {len(pessoas)}')
print(f'O menor peso foi {menor}. Peso de ', end='')
for i in range(len(pessoas)):
    if menor == pessoas[i][1]:
        print(pessoas[i][0], end=' ')
print()
print(f'O maior peso foi {maior}. Peso de ', end='')
for i in range(len(pessoas)):
    if maior == pessoas[i][1]:
        print(pessoas[i][0], end=' ')'''
'''lista = [[],[]]
for i in range(0,7):
    n = int(input('Digite o valor: '))
    if n % 2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(lista)'''
'''matriz = [[],[],[]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input("Digite um número: ")))
for i in range(0,3):
    for j in range(0,3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print()'''
matriz = [[],[],[]]
s = st = maior = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input("Digite um número: ")))
for i in range(0,3):
    for j in range(0,3):
        print(f'[ {matriz[i][j]} ]', end=' ')
        if matriz[i][j] % 2 == 0:
            s+=matriz[i][j]
        if j == 2:
            st += matriz[i][j]
        if maior<matriz[i][j]:
            maior = matriz[i][j]
    print()
print(f'A soma dos numeros pares é: {s}')
print(f'A soma dos números da terceira coluna: {st}')
print(f'O maior numero é: {maior}')