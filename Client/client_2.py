from socket import *
import struct
import marshal

#nome ou ip do servidor, como a chamada é local utilizamos localhost ou 127.0.0.1
serverName = 'localhost'
#Porta do servidor que está a escuta para esta ligação
serverPort = 7000 

#Bloco de código de ligação ao servidor, caso não seja possível é devolvido um erro
try:
	# Criacao do socket
	socket_Cliente = socket(AF_INET, SOCK_STREAM)
	# ligação ao servidor
	socket_Cliente.connect((serverName,serverPort))
except Exception as m:
	print("Erro ao conectar!")
	quit()

#Função principal, menu do cliente
def main ():
    print("***********************************")
    print("* Trabalho 1 Programação Avançada *")
    print("* Nome: Nuno Cunha                *")
    print("* Número: 20202457                *")
    print("* Turma: G.S.C                    *")
    print("***********************************")
    print("\n")

    print("****************************************************************")
    print("* 1 - Noites de Cintra, by Alberto Pimentel                    *")
    print("* 2 - Postumas de Braz Cubas, by Machado de Assis              *")
    print("* 3 - The Adventures of Sherlock Holmes, by Arthur Conan Doyle *")
    print("* 4 - The Picture of Dorian Gray, by Oscar Wilde               *")
    print("* 5 - Introduzir Caminho                                       *")
    print("* 6 - Sair                                                     *")
    print("****************************************************************")        

    #Recebe a opção do utilizador
    option = input(("\n\nEscolha uma das opções: "))

    while True:    

        if option == '1':
            path = "Livros\pg34719.txt"
            return path
            break
        elif option == '2':
            path = "Livros\pg54829.txt"
            return path
            break
        elif option == '3':
            path = "Livros\pg1661-0.txt"
            return path
            #Função que pára a execução do programa
            break
        elif option == '4':
            path = "Livros\pg4078.txt"
            return path
            break
        elif option == '5':
            path = input("\nIntroduza o caminho e o nome do ficheiro (exemplo: c:\\teste.txt):\n")
            return path
            break
        elif option == '6':
            print("\nAté Breve")
            #Função que termina a execução do programa
            exit()        
        else:
            print("\nOpção inválida!") 
            option = input(("Escolha outra opção: "))


#Função para fazer o print das palavras recebidas
def imprimir_lista(lista):

    for i in range(len(lista)):
        print(lista[i])

#Envio dos dados introduzidos pelo cliente para o servidor
socket_Cliente.send(marshal.dumps(main()))

#Dados racabidos do servidor
palavras = socket_Cliente.recv(4096)
#decode dos dados recebidos
lista_palavras = marshal.loads(palavras)

#chamada da função para fazer o print das palavras
imprimir_lista(lista_palavras)

#Fecha o socket
socket_Cliente.close()

