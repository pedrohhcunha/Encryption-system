# Importa a biblioteca para autilização do socket
import socket

# Define o alfabeto de letras a serem usadas
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Define o nome do host
host = ''
# Define a porta que será utilizada
port = 9093
# Cria a variavel que irá armazenar a mensagem recebida
pega_mensagem = ''
# Concatena o host e a porta que serão usadas
addr = (host, port)
# Criação do socket para receber uma conexão do tipo TCP/IP
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Zera o TIME_WAIR do Socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Define a porta e o IP de onde deve-se aguardar conexão
serv_socket.bind(addr)
# Define o limite de conexões ao servidor
serv_socket.listen(1)
# Inicializa uma variável para armazenar o tamenho da mensagem recebida
tam_mensagem = 0

print('Aguardando cliente...')  # Imprime uma string
# Deixa o server na escuta aguardando conexões
con, cliente = serv_socket.accept()
print('Na espera de mensagem')  # Imprime uma string
while(pega_mensagem != 0):
    # Aguarda um dado enviada com até 1024 bytes
    pega_mensagem = con.recv(1024)
    # Decodificada a mensagem para utf-8
    pega_mensagem = pega_mensagem.decode('utf-8')
    # Imprime na tela uma string e a mensagem recebida
    print("Chegou a mensagem " + pega_mensagem)

    # Verifica se o caractere existe na mensagem recibida
    if (pega_mensagem.find(')')):

        # Atribui a pega_mensagem o valor real da mensagem
        pega_mensagem = pega_mensagem.split(')')[0]
        # Imprime a mensagem na tela
        print(pega_mensagem)
        # Armazena a chave em uma variavel atráves de um input
        chave = input("Digite a chave de quebra da mensagem: ")

        # Cria uma variavel para armazenar o valor da mensagem decodificada
        decodedMessage = []
        # Itera sobre os caracteres da mensagem
        for letter in pega_mensagem:
            # Busca o index da letra atual no arrau de letras
            indexLetterInAlfabet = letters.find(letter)
            # Armazena o indice da letra já decodificada
            letterDecoded = indexLetterInAlfabet - int(chave)
            # Verifica se o indice da letra decodificada é menor que 0

            if letterDecoded < 0:
                # Adiciona 26 ao indice da letra decodificada
                letterDecoded += 26
            # Adiciona a letra decodificada a lista de letras já decodificada
            decodedMessage.append(letters[letterDecoded])

        # Transforma o array em uma string
        output = ''.join(decodedMessage)
        # Imprime na tela a mensagem decodificada
        print(output)

# Finaliza a conexão com o socket
serv_socket.close()
