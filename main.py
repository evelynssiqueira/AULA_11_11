lista=[12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, -52]

#a) imprima o maior número
maior = None
for i in lista:
    if not maior:
        maior = i
    if i > maior:
        maior = i
print(f'O maior valor é:{maior}')
print(f'O maior valor é: {max(lista)}')
#b) imprima o menor número
menor = None
for i in lista:
    if not menor:
        menor = i
    if i < menor:
        menor = i
print(f'O menor valor é:{menor}')
print(f'O menor valor é: {min(lista)}')
#c) imprima os números pares
for i in lista:
    if i % 2 == 0:
      print(f'{i} é par')
#c.1) criar lista pares
listaPares = []
for i in range(0,len(lista)):
    if (lista[i] % 2 == 0):
        listaPares.append(lista[i])
print(listaPares)

#d) imprima o número de ocorrencias do primeiro elemento da lista

ocorrencia = lista.count(lista[0])
print(f' O número de ocorrências é: {ocorrencia}')

ocorrenciaItem = 0
for i in range(0,len(lista)):
    if (lista[i] == lista[0]):
        ocorrenciaItem += 1
print(f' O número de ocorrências é: {ocorrenciaItem}')

#e) imprima a média dos elementos

soma = sum(lista)
divisor = len(lista)
media = soma/divisor
print(f' A média é: {media:.3f}')

#f) imprima a soma dos elementos de valor negativo
