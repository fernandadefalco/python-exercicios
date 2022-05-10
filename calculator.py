#Definindo a função da calculcadora
def calculadora(opcao,num1,num2):
    
    if opcao == 1:
        return print(f"{num1} + {num2} = {num1+num2:.1f}")
    elif opcao == 2:
        return print(f"{num1} - {num2} = {num1-num2:.1f}")
    elif opcao == 3:
        return print(f"{num1} x {num2} = {num1*num2:.1f}")
    else:
        return print(f"{num1} / {num2} = {num1/num2:.1f}")

#Início da apresentação na tela
print("************************* Python Calculator *************************")
print('''Selecione a opção desejada: 
         1) Soma
         2) Subtração
         3) Multiplicação
         4) Divisão''')

opcao = input("Digite sua opção (1/2/3/4): ")

#Validação com o usuário
valido = True
while valido:
    if opcao.isdigit() == False:
        opcao = input("Opção inválida, digite sua opção (1/2/3/4): ")
    elif opcao not in ('1','2','3','4'):
        opcao = input("Opção inválida, digite sua opção 2 (1/2/3/4): ")
    else:
        valido = False
        
#Inserção de parâmetros
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calculadora(opcao,num1,num2)
