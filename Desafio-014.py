'014'
'Escreva um programa que converta uma temperatura digitada em graus Celsius (°C) e a '
'converta para graus Fahrenheit (°F).'
'F= (9 x C)/5 + 32'
n1 = float(input("Digite a temperatura em °C: "))
print(f"A tempereatura de {n1} °C corresponde a {((n1*9)/5)+32:.2f}")