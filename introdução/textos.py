'''Exercicio 22
nome = str(input("Digite seu nome completo: "))
print(nome.upper())
print(nome.lower())

print(len(nome) - nome.count(' '))
separa = nome.split()
print(separa[0])'''

'''Exercicio 23
numero = input("Digite um numero de 0 a 9999: ")
print("unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}".format(numero[3],numero[2],numero[1],numero[0]))'''

'''Exercicio 24
cidade = input("Digite o nome de uma cidade: ")

print(cidade[:5]=="Santo")'''
'''Exercicio 25
nome2 = input("Digite o nome: ")
print('silva' in nome2.lower())'''
'''Exercicio 26
frase = input("Digite uma frase: ").lower()
print("A letra 'A' aparece {} vezes".format(frase.count("a")))
print("A primeira posição da letra 'A' é {}".format(frase.find("a")+1))
print("A ultima vez que a letra 'a' aparece é {}".format(frase.rfind("a")+1))'''
'''Exercicio 27
nome3 = input("Digite o nome completo: ").split()
print("Primeiro nome: {}\nÚltimo nome: {}".format(nome3[0], nome3[len(nome3)-1]))'''