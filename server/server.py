import socket
import threading

#Porto de connecção entre o servidor e o cliente
PORTA = 7000
#Nome do servidor, a função permite obter o nome do computador de forma dinâmica, assim o nosso programa pode correr em diferentes computadores
nome_servidor = socket.gethostbyname(socket.gethostname())
#Tupla de dados a passar para a connection
ADDR = (nome_servidor,PORTA)
#Formato em que queremos os dados depois de descodificados
FORMATO = "utf-8"
#variavel que passa informação de que a ligação foi terminada
DESLIGAR_LIGACAO = "Ligação Terminada"

#Cria a ligação para o servidor receber as ligações dos clientes neste caso TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Faz a associação do socket com a porta e o nome do servidor
servidor.bind(ADDR)

#Função que vai tratar individualmente cada cliente
def cliente (connection, endereco):
    print(f"O cliente {endereco} ligou-se.")

    #Loop que fica a espera de informação do CLiente
    while 1:
        #Recebe os dados do cliente
        dados_cliente = connection.recv(1024).decode(FORMATO)
        if dados_cliente == DESLIGAR_LIGACAO:
            break
            
        print(dados_cliente)

        connection.close()


    

#Função que inicia o servidor, ficando a espera que o cliente se ligue
#Trata de todas as ligações dos clientes
def start():
    #Coloca o servidor a espera de ligações
    servidor.listen()

    while True:
        #Guarda a informação da ligação e do endereço do cliente
        connection, endereco =  servidor.accept()
        #Criação da Thread para o cliente
        thread = threading.Thread(target=cliente, args=(connection, endereco))
        #iniciar a thread
        thread.start()
        #Este comando permite obter o numero de ligações activas ao nosso servidor
        #Temos de colocar -1 porque existe sempre uma thread activa start() que está a espera de novas ligações
        print(f"Número de ligações {threading.active_count() - 1}")

print("O Servidor está a iniciar...")
start()

