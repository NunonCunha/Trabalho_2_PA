
import socket
#biblioteca para converter qualquer tipo de dado em binário
import marshal
#Biblioteca para o uso de threadings
import threading
#Biblioteca para utilizar a função encoding para utilização de caracteres especiais no ficheiro
import codecs
#Biblioteca para trabalhar com datas e horas
import datetime

# Numero de porta na qual o servidor estara esperando Ligações.
serverPort = 7000
# Criar o socket
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Associa o socket á porta escolhida, O Primeiro argumento vazio indica
# que aceitamos ligações em qualquer interface de rede desse host
socketServidor.bind(('', serverPort))
# Configura o socket para aceitar ligações
socketServidor.listen()

#Lista para envio de palavras para o cliente
lista_palavras_cliente = []

#Função principal que vai ser chamada no menu no final do programa
def main(path):
    #Abertura do ficheiro, o bloco Try permite que o utilizador receba uma mensagem personalizada caso não seja possivel abrir o ficheiro
    try:
        file = open(f"{path}", 'r',encoding='utf-8')
    except:
        print("\n[Servidor]Erro ao abrir o ficheiro, O programa vai terminar")
        return "[Cliente]Erro ao abrir o ficheiro, O programa vai terminar"
        exit()

    #leitura do ficheiro para uma lista
    texto = file.read().lower()

    #Fecha a ligação ao ficheiro
    file.close()

    #Cria uma lista com caracteres
    pont_list_chr=[]

    def chr_list(begin, end):
        #lê um inteiro e converte em caracter, e adiciona á lista
        for i in range(begin, end):
            pont_list_chr.append(chr(i))

    #Range de caracteres na tabela ASCII
    chr_list(33,48)
    chr_list(58,65)
    chr_list(91,97)
    chr_list(123,127)

    #Função para remover todos os caracteres especiais
    def remove_char(text):   

        for char in pont_list_chr:
                text = text.replace(char, '')
        return text

    #Atribui a string a variavel texto mas sem os caracteres especiais
    texto = remove_char(texto)

    #Função para converter a String sem os caracteres especiais em lista
    #A função strip() remove os espaços no inicio e fim da string
    def convert_list(text):

        for line in text:
            line = line.strip()
        lista = list(text.split())
        return lista

    #Cria uma lista de palavras separadas por espaço
    lista_final = convert_list(texto)

    #Função para criar um dicionario com os pares de palavras e a sua ocorrencia no texto lido
    def get_words_count(lista):

        dic = {}
        counter = 0
        for word in lista:
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
        
        return dic

    #Cria um novo dicionário com a contagem das palavras
    dicionario = get_words_count(lista_final)

    #Função para organizar o dicionário e fazer print ordenado
    def order_score(dic):
        '''ordenação do dicionário com função lambda em que a comparação é feita com o valor x[1]
        utilizamos o reverse=True para alterar a ordem do sorted()
        referencia para a função lambda. (https://docs.python.org/3/reference/expressions.html#lambda) 
        (https://towardsdatascience.com/two-simple-method-to-sort-a-python-dictionary-a7907c266dba)'''

        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        # Ciclo para percorrer o dicionario, mostra a palavras e o valor, das 20 mais utilizadas
        lugar = 1

        while lugar < 20:
            for i in dic[:20]:     
                lista_palavras_cliente.append(f"{lugar} º - {i[0]} - {i[1]} ocorrências")
                lugar += 1   
                


    #Execução das funções do programa
    order_score(dicionario)  

#Função que trata os pedidos dos clientes
def pedido_Cliente(socketCliente):
    
    # Recebe os dados do cliente
    pacote = socketCliente.recv(1024)
    #Descodifica os dados recebidos
    path = marshal.loads(pacote)

    #Informação dos dados recebidos pelo servidor
    print(f"Servidor recebeu o pacote: {path}")

    # Executa a função main para obter as palavras
    print("A processar os Dados...")

    #Função para tratar as palavras
    main(path)

    # Envia mensagem de resposta para o cliente
    socketCliente.send(marshal.dumps(lista_palavras_cliente))
    print(f"[Servidor] Lista de palavras enviadas ao cliente")

    # Fecha a conexão
    socketCliente.close()

print ('O servidor esta pronto para receber pacotes...')

# Loop infinito para tratar diversas ligações
while True:
    # Aguardar nova Ligação
    print ('A Aguardar Ligações...')
    connectionSocket, addr = socketServidor.accept()

    #Trata o pedido do cliente com threads
    t = threading.Thread(target=pedido_Cliente, args=(connectionSocket,))

    # Inicia a thread
    t.start()
