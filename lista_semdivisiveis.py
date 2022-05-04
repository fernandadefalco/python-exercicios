'''
Remove Divisíveis

Faça uma função que recebe uma lista com inteiros e devolva a lista sem os números divisíveis por 2 e/ou por 5. 

'''
#Definindo a função
def listasemDivisiveis(lista):
    i = 0
    lista_final=[]
    
    while i < len(lista):
        if lista[i]%2 != 0 and lista[i]%5 != 0:
            lista_final.append(lista[i])
        i+=1
    return lista_final

#Recebendo o input do usuário
lista_input =  list(input("Insira uma lista de elementos separada por vírgula: ").split(","))

#Transforma os elementos da lista do input em inteiros
i =0 
while i <len(lista_input):
    lista_input[i]= int(lista_input[i])
    i +=1
    
print(f"{lista_input} sem os números divisíveis por 2 e/ou por 5 resulta em {listasemDivisiveis(lista_input)}")