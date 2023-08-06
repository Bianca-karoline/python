# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(var)}')
print(f'Só tem espaços? {var.isspace()}')
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f'É alfanumérico? {var.isalnum()}')
print(f'É um decimal? {var.isdecimal()}')
print(f'Está em caixa baixa? {var.islower()}')
print(f'Está em caixa alta? {var.isupper()}')
