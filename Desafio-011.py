'011'
'Faça um programa que leia a largura e a altura de uma parede em metros. O programa deve:'
'Calcular a área da parede (Lembrando: área = largura * altura).'
'Calcular a quantidade de tinta necessária para pintá-la, sabendo que cada litro de '
'tinta pinta uma área de 2 metros quadrados (2m²).'

n1 = float(input("Digite a largura (em metros) : "))
n2 = float(input("Digite a altura (em metros : )"))
print(f"A parede é de {n1}x{n2} sua área é de {n1*n2}")
print(f"A tinta necessaria é de {(n1*n2)/2}") 