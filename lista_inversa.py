'''
Dada uma lista encadeada de caracteres formada por uma seqüência alternada de letras e dígitos, construa um método que retorne uma lista 
na qual as letras são mantidas na seqüência original e os dígitos são colocados na ordem inversa. Exemplos:

A 1 E 5 T 7 W 8 G
retorna: A E T W G 8 7 5 1

3 C 9 H 4 Q 6
retorna: C H Q 6 4 9 3

Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos dígitos.
'''

lista = list(input("Insira uma lista de elementos separada por vírgula: ").split(","))
lista_num =[]
lista_letra =[]

i= 0 
while i <len(lista):
    if lista[i].isdigit():
        lista_num.append(lista[i])
    else:
        lista_letra.append(lista[i])
    i+=1

lista_final = lista_letra + lista_num[-1::-1]

print(lista_final)