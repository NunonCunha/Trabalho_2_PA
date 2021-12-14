from socket import *
import struct
import marshal

serverName = 'localhost' # Ou '127.0.0.1'
serverPort = 7000 

try:
	# Criacao do socket
	socket_Cliente = socket(AF_INET, SOCK_STREAM)
	# Conexao com o servidor
	socket_Cliente.connect((serverName,serverPort))
except Exception as m:
	print("Erro ao conectar!")
	quit()


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
            path = "pg34719.txt"
            return path
            break
        elif option == '2':
            path = "Livros\pg54829.txt"
            return path
            break
        elif option == '3':
            path = "Livros\pg1661-0.txt"
            return path
            #Função que para a execução do programa
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


socket_Cliente.send(marshal.dumps(main()))
data = socket_Cliente.recv(1024)
lista_palavras = marshal.loads(data)
print(lista_palavras)
socket_Cliente.close()

