from collections import Counter
lista = [0,0,1,2,0,5,55]
print(Counter(lista))

print(Counter(lista).most_common(1))
'''Não muda a variavel'''
print(sorted(lista))
'''A lista passa a ser organizada'''
lista.sort()
print(lista)

print(sorted(lista, key=abs, reverse=True))