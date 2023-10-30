import os

cores = ['blue', 'red', 'yellow']


if 'yellow' in cores:
    print("Existe a cor amarela")
else:
    print("Não Existe a cor amarela")

numero = []
nomes = []
def cadastro(num, nome):    
    numero.append(num)
    nomes.append(nome)
    return "A chapa foi cadastrada com sucesso"
    
def pesquisar():  
    limpar()  
    cont = 0
    while cont < len(nomes):
        print(numero[cont])
        print(nomes[cont])                  
        cont += 1

def atualizar():
    return 0
def deletar(num):
    if num in numero:
        print("O numero que deseja excluir é ", num)
    else:
        print("Não tem o valor")
def msn():
    print("Opção inválida")
def limpar():
    os.system('cls')      

op = 10
while op != 0:
   
    op = int(input("Digite sua opção:"+ 
                   "\n 1 - Cadastrar uma chapa"+
                   "\n 2 - Pesquisar uma chapa"+
                   "\n 3 - Atualize uma chapa"+
                   "\n 4 - Delete uma chapa"+
                   "\n 0 - Feche o sistema"+
                   "\nEscolha a opção:    "))
    if op == 1:
        limpar()
        num = int(input("Digite o numero da chapa"))
        nome = input("Digite o nome da chapa")
        print(cadastro(num, nome)) 
    elif op == 2:        
        pesquisar()
    elif op == 4:
        op = int(input("Digite o número da chapa para deletar"))        
        deletar(op)       
 

    