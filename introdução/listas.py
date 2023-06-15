'''num = list()
menor = maior = 0
for i in range(0,5):
    num.append(int(input('Digite um número: ')))
    if i == 0:
        maior = menor = num[i]
    if num[i]>maior:
        maior = num[i]
    if num[i]<menor:
        menor = num[i]
print(f'O menor número digitado é {menor} na posição', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}', end=' ')
print()
print(f'O maior número digitado é {maior} na posição', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}', end=' ')
print()'''
'''lista = list()
s = ''
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado não foi adicionado na lista')
    s = str(input("Deseja continuar?[S/N]")).lower()
    if s in 'nN':
        break
lista.sort()
print(lista)'''
'''lista = list()
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n>lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos+=1
print(lista)'''
'''lista = list()
s = ''
while True:
    lista.append(int(input("Digite um número: ")))
    s = str(input("Deseja continuar?[S/N]")).lower()
    if s in 'nN':
        break
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {len(lista)} numeros')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')'''
lista = list()
par = list()
impar = list()
s = ''
while True:
    lista.append(int(input("Digite um número: ")))
    s = str(input("Deseja continuar?[S/N]")).lower()
    if s in 'nN':
        break
for i in range(0, len(lista)):
    if lista[i] %2 ==0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(f'A lista de números pares é {par}')
print(f'A lista de números impares é {impar}')