import math

area_a_ser_pintada = int(input('Digite o tamanho da área a ser pintada em metros quadrados: ')) # area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1 #considerar folga de 10%
metros_por_litro = int(input('Digite quantos metros a tinta faz por litro: '))
litros_a_serem_usados = area_com_folga / metros_por_litro
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}')

litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_com_apenas_galoes = numero_de_galoes *25
print(f'Você deverá usar {numero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_com_apenas_galoes}')

# Compra de tinta optimizada por valor
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas = numero_de_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes = numero_de_galoes *25

valor_total = valor_de_latas + valor_com_galoes

print(f'Você deverá usar {numero_de_latas} latas de 18 litros e mais {numero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_total} para ter o menor desperdício de tinta possível')