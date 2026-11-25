'004'
algo = input("Digite qualquer coisa ")

print("O tipo primitivo desse valor é : ", type(algo))
print("Só tem espaços?", algo.isspace())
print("É número?",algo.isnumeric())
print("É alfabetico (Só letras)?", algo.isalpha())
print("É alfanumerico (Números e letras)?", algo.isalnum())
print("Está maiúsculas?",algo.isupper())
print("Está minúsculas?",algo.islower())
print("Está capitalizada (com a primeira maiuscula)?",algo.istitle())