import os
numero = []
nomes =  []
voto =   []


dados = [1,2,3,4,5]
print(sum(dados))

def cadastro(num, nome):    
    numero.append(num)
    nomes.append(nome)
    voto.append(0)
    return "A chapa foi cadastrada com sucesso"
    
def pesquisar():  
    limpar()  
    print("Número\tNome")
    cont = 0
    while cont < len(nomes):
        print(numero[cont], "\t", nomes[cont])
        cont += 1

def atualizar(num):
    novonumero = int(input("Digite o novo número"))
    novonome = "Israel"
    if num in numero:
        posicao = numero.index(num)
        numero[posicao] = novonumero
        nomes[posicao] = novonome
        return "Chapa atualizada com sucesso"


    return 0
def deletar(num):       
    if num in numero:       
       posicao = numero.index(num)       
       numero.pop(posicao)
       nomes.pop(posicao)
       voto.pop(posicao)
       return "A chapa de número", num, " ", "foi removida com sucess"
    else:
        return  ("Não existe esta chapa com esse número" , num)
    
def msn():
    print("Opção inválida")
def limpar():
    os.system('cls')    

def votos(num):
     if num in numero:
         posicao = numero.index(num)
         voto[posicao] = (voto[posicao]) + 1
         return "Voto cadastrado com sucesso"
     
def verificar():
    total = sum(voto)
    cont = 0
    while cont < len(numero):
        print("CHAPA:", (nomes[cont]),  "NÚMERO DA CHAPA: ", (numero[cont]), "VOTOS", voto[cont], ((voto[cont] * 100) / total ), "%")
        cont += 1 

    



  

op = 10
while op != 0:
   
    op = int(input("Digite sua opção:"+ 
                   "\n 1 - Cadastrar uma chapa"+
                   "\n 2 - Pesquisar uma chapa"+
                   "\n 3 - Atualize uma chapa"+
                   "\n 4 - Delete uma chapa"+
                   "\n 5 - Votar"+
                   "\n 6 - Resultado"+
                   "\n 0 - Feche o sistema"+
                   "\nEscolha a opção:    "))
    if op == 1:
        limpar()
        opcao = int(input("Digite o numero da chapa"))
        valor = input("Digite o nome da chapa")
        print(cadastro(opcao, valor)) 
    elif op == 2:        
        pesquisar()
    elif op == 3:
        valor = int(input("Digite o número da chapa para atualizar"))        
        retorno = atualizar(valor)   
        print(retorno)    
    elif op == 4:
        valor = int(input("Digite o número da chapa para deletar"))        
        retorno = deletar(valor)   
        print(retorno)
    elif op == 5:
        valor = int(input("Digite a chapa que vc quer votar:"))
        print(votos(valor))
    elif op == 6:
        verificar()    

 

    