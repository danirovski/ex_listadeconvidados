# Exercício - Elabore um programa que pergunte quantas pessoas serão convidadas para uma festa
# e itere essas pessoas numa lista, e após inserir toda a quantidade de convidados, gere uma lista  e mostre o total
# de pessoas convidadas.


#Definição de variáveis
qtd_convidados = int(input('Quantas pessoas serão convidadas? '))
lista = []
contador = 1

#Laço de repetição para coletar as entradas dos nomes dos convidados

while contador <= qtd_convidados:
    nomes = input('Insira o nome do convidado: ')
    contador += 1
    inserir = lista.append(nomes)
print('Lista de pessoas que serão convidadas para a sua festa: ')
print('**************------------------*****************************---------------------***********************')

# Laço de repetição for para imprimir a ficha com a relação de nomes convidados

for pessoa in lista:
    print(pessoa)
    
# Imprimir o total de pessoas
print('Total de ',len(lista), 'pessoas')
