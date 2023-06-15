'''from time import sleep
for i in range(10,-1, -1):
    print(i)
    sleep(1.0)
print("Fim")'''

'''for i in range(2,51,2):
    print(i)
print("Fim")'''
'''s = 0
cont = 0
for i in range(1,501,2):
    if(i%3 == 0 and i%2 != 0):
        s += i
        cont += 1
print("A soma dos {} números é {}".format(cont,s))'''
'''t = int(input("Digite o número que deseja ver a tabuada: "))
for i in range(1, 11):
    print("{} X {} = {}".format(i,t,(i*t)))'''
'''s =0
for i in range(0,6):
    n = int(input("Digite um número: "))
    if n%2 == 0:
        s += n
print(s)'''
'''n1 = int(input("Digite um número: "))
pa = int(input("Digite a razão da PA: "))
n10 = n1 + 9 * pa
for i in range(n1, n10 + pa, pa):
    print(i)'''
'''p = int(input("Digite um número: "))
primo = True
for i in range(p-1, 2, -1):
    if(p%i == 0):
        primo = False
if primo == True:
    print("{} é um número primo".format(p))
else:
    print("{} não é um número primo".format(p))'''
'''cMenor =0
cMaior = 0
for i in range(0,7):
    n = int(input("Digite o ano de nascimento: "))
    if (2023 - n) < 18:
        cMenor += 1
    else:
        cMaior += 1
print("Ao todo tivemos {} pessoas menores de idade e {} pessoas maiores".format(cMenor, cMaior))'''
'''menor = 0
maior = 0
for i in range(0,5):
    p = float(input("Digite o peso: "))
    if i==0:
        menor = p
        maior = p
    if menor > p:
        menor = p
    if maior < p:
        maior = p

print("O menor peso é {} e o maior é {}".format(menor,maior))'''
'''media = 0
h = 0
cont = 0
for i in range(0,4):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo(M/F): ")).lower()
    media += idade
    if sexo == "m" and h < idade:
        h = idade
        n = nome
    if sexo == "f" and idade < 20:
        cont += 1

media = media /4
print("A media de idade do grupo é: {}\nO nome do homem mais velho: {}\nQuantidade de mulheres com menos de 20 anos: {}".format(media, n, cont))'''