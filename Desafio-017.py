'017'
'Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo '
'retângulo. Calcule e mostre o comprimento da hipotenusa.'
import math
n1 = float(input("Valor do cateto adjacente : "))
n2 = float(input("Valor do cateto oposto : ")) 
print(f"O valor da hipotenusa {math.hypot(n1,n2)}")