#Calculando a area de um circulo com a library math

import math

raio_do_circulo = int(input("Digite o raio do circulo: "))
area_do_circulo = math.pi * raio_do_circulo ** 2

print (f"{area_do_circulo:.2f}")

#Retorna dia, mes e ano a partir de uma data

data = str(input("Insira a data no formato DD/MM/YYYY: "))
data_list = data.split('/')

dia = data_list[0]
mes = data_list[1]
ano = data_list[2]

print(f"O dia é {dia}, o mês é {mes} e o ano é {ano}.")