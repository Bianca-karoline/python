'''extenso = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = 0
while True:
    n = int(input(f'Digite um número: '))
    if 0 <= n <= 20:
        print(f'{extenso[n]}')
        break'''
'''from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
menor = maior = 0

print(numeros)
print(f'O menor número é {min(numeros)}, o maior número é {max(numeros)}')'''
'''n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')'''
'''palavras = ('aprender', 'python', 'estudar', 'programar')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')'''