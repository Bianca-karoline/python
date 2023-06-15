'''n = str(input("Digite [M/F]")).lower()
while n not in "mf":
    n = str(input("Digite [M/F]")).lower()'''
'''from random import randint
i = 1
c = randint(0,10)
j = int(input("Digite um número: "))
while j != c:
    c = randint(0, 10)
    j = int(input("O computador pensou em outro número tente novamente! "))
    i += 1

print("Você precisou de {} palpites para vencer".format(i))'''
'''n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
op = 0
while op != 5:
    op = int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4]Novos números\n[5]Sair do programa\n"))
    if op == 1:
        print("A soma dos dois números é: {}".format(n1+n2))
    elif op == 2:
        print("A multiplicação dos dois números é: {}".format(n1*n2))
    elif op == 3:
        if n1 > n2:
            print("O maior número é: {}".format(n1))
        elif n2>n1:
            print("O maior número é: {}".format(n2))
        else:
            print("Os dois números são iguais")
    elif op == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))'''
'''n = int(input("Digite um número: "))
result = n
while n > 1:
    result *= n-1
    n -= 1
print(result)'''
'''n = int(input("Digite um número: "))
pa = int(input("Digite a PA: "))
c = 0
while c <10:
    print(n)
    n += pa
    c += 1'''
'''n = int(input("Digite um número: "))
pa = int(input("Digite a PA: "))
c = 0
f = 10
while c <f:
    print(n)
    n += pa
    c += 1
    if c == f:
        f += int(input("Digite quantos termos deseja ver: "))

print("Você visualizou {} termos da PA".format(c))'''

'''n = int(input("Digite um número: "))
c = 1
a= 0
b =1
d = 1
while c != n:
    print("{} -".format(a,b),end='')
    d = a + b
    a = b
    b = d
    c +=1'''

'''n = int(input("Digite um número: "))
s = 0
c = 0
while n != 999:
    s += n
    n = int(input("Digite um número: "))
    c += 1
print("A soma dos {} números digitados é: {}".format(c,s))'''

'''media = 0
maior = 0
menor = 0
c = 0
resp = "S"
while resp in "Ss":
    n = int(input("Digite um número: "))
    media += n
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    resp = str(input("Deseja continuar[S/N]")).upper()
media = media / c
print(f"A média dos {c} números digitados é {media}\nO maior número é {maior} e o  menor {menor}")'''
'''n = s = c = 0
while True:
    n = int(input(("Digite um número (999 para parar): ")))
    if n == 999:
        break
    c += 1
    s += n
print(f"A soma dos {c} é {s}")'''
'''n = int(input("Digite um número e veja sua tabuada: "))
while True:
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    n = int(input("Digite um número e veja sua tabuada: "))
    if n < 0:
        break
print("Programa encerrado")'''
'''from random import randint
j = i = c = 0
frase = ""
while True:
    print("----------- PAR OU ÍMPAR --------")
    j = int(input("Diga o valor: "))
    frase = str(input("Par ou ímpar?[P/I]: ")).lower()
    c = randint(0,10)
    print(f"Você jogou {j} e o computador {c}")
    if frase in "pP":
        if (j+c)%2 != 0:
            break
    else:
        if (j+c)%2 == 0:
            break
    i += 1
    print("O jogador venceu!")
print(f"O jogador perdeu depois de {i} vitórias")'''
'''h = m = i = 0
s = ''
while True:
    sexo = str(input("Digite o sexo[M/F]: ")).lower()
    idade = int(input("Digite a idade: "))
    if idade > 18:
        i += 1
    if sexo in "Mm":
        h += 1
    if sexo in "Ff" and idade <20:
        m += 1
    s = str(input("Deseja continuar cadastrando?[S/N]")).lower()
    if s in "Nn":
        break
print(f"Maiores de 18: {i}\t Homens cadastrados: {h} \tMulheres com menos de 20 anos: {m}")'''
'''total = qtd = b = 0
produto = s = 'S'
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    if preco > 1000:
        qtd += 1
    if b > preco or total == 0:
        b = preco
        produto = nome
    total += preco
    s = str(input("Deseja continuar?[S/N]: ")).upper()
    if s in "Nn":
        break
print(f"O total da compra: {total}\nProdutos custando mais que 1000: {qtd}\nProduto mais barato: {produto}")'''
total = valor = int(input("Qual valor deseja sacar: "))
ced = 50
qtd = 0
while True:
    if total >= ced:
        total -= ced
        qtd += 1
    else:
        print(f"Total de {qtd} de cédulas de R${ced:.2f}")
        if ced == 50:
            qtd = 0
            ced = 20
        elif ced == 20:
            qtd = 0
            ced = 10
        elif ced == 10:
            qtd = 0
            ced = 1
        else:
            break
print("Acabou")