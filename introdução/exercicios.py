"""import math
print("-------------- Exercício 18 ----------------")
angulo = int(input("Digite o angulo: "))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print("Seno: {}\nCosseno: {}\nTangente: {}\n".format(sen, cos,tan))
"""
'''print("-------- Exercício 19 ---------------------")
import random
nomes = [str(input("Digite os nomes: ")), str(input("Digite os nomes: ")), str(input("Digite os nomes: ")), str(input("Digite os nomes: "))]
print(random.choice(nomes))

print("---------------- Exercício 20 ------------------")
random.shuffle(nomes)
print(nomes)'''
'''print("-------------- Exercício 21 ---------------")
import pygame
usa o pacote pygame para abrir um arquivo MP3 externo
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''
texto = "Curso em video python"
'''começo e fim da cadeia de caracteres'''
print(texto[0:9]) 
"""começo, fim e quantidade de casas para andar"""
print(texto[9:21:2])
print(texto[9::3])
'''determina o fim'''
print(texto[:9])
'''determina o começo'''
print(texto[9:])
'''tamanho do texto'''
len(texto)
'''conta os caracteres de comparação'''
texto.count("o")
'''conta os caracteres entre os intervalos'''
texto.count("o", 0,13)