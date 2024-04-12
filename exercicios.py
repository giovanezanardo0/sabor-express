# # # # 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# # numero = int(input("Digite um número: "))
# # if numero % 2 == 0:
# #     print("O número é par.")
# # else:
# #     print("O número é ímpar.")


# # # # 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# # # # Criança: 0 a 12 anos;
# # # # Adolescente: 13 a 18 anos;
# # # # Adulto: acima de 18 anos.


# # idade = int(input("Digite sua idade: "))
# # if 0 < idade <= 12:
# #     print("Criança")
# # elif 12 < idade <= 18:
# #     print("Adolescente")
# # elif idade > 18:
# #     print("Adulto")
# # else:
# #     print("Valor inválido!")


# # # 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# # #
# # # 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# # x = int(input("informe numero de x"))
# # y = int(input("informe numero de y"))

# # # Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# # if x > 0 and y > 0:
# #     print("Primeiro Quadrante")
# # # Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# # elif x < 0 and y > 0:
# #     print("Segundo Quadrante")
# # # Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# # elif x < 0 and y < 0:
# #     print("Terceiro Quadrante")
# # # Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# # elif x > 0 and y < 0:
# #     print("Quarto Quadrante")
# # # Caso contrário: o ponto está localizado no eixo ou origem.
# # else:
# #     print("eixo de origem")

# Exercícios
# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Lista com quatro nomes;
nomes = [
    "Giovane",
    "Larissa",
    "Gabriel",
    "Gian",
]
# Lista com o ano que você nasceu e o ano atual.
anos = [1991, 2024]
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for i in nomes:
    print(i)
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma_impares = 0

for x in numeros:
    if x % 2 != 0:  # Verifica se o número é ímpar
        soma_impares += x  # Adiciona o número ímpar à soma
print(soma_impares)

#OU

soma_impares = 0
for i in range(1, 11, 2): #O segundo argumento de da função range é exclusivo, então range(1, 11) inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range). Isso garante que apenas números ímpares sejam considerados.
    soma_impares += i
print(soma_impares)


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
#Exception é uma classe base para todas as exceções em Python. 
# Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. 
# O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, 
# como mensagens de erro.    

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
# ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. 
# Este bloco except é destinado a lidar especificamente com esse tipo de erro.