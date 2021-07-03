# importa a biblioteca para a utilzação do python
import socket

# Armazena na variavél o ip do cliente
ip = "127.0.0.1"
# Define a porta onde deve ser enviado os dados
port = 9093
# Inicia a variavel para armazenar a mensagem cifrada
mensagem_cifrada = ""
# Inicia a ariavel para armazenar a mensagem normal
mensagem_normal = ""
# Inicia a variavel para armazenar a chave
chave = ""
# Define o ADDR como sendo o ip e a porta
addr = (ip, port)
# Faz a conexão com  o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Faz a conexão com o servidor
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# faz a conexão com o servidor
client_socket.connect(addr)

# Cria uma classe para a cifra de Cesar


class Cesar:
    def __init__(self):
        self.__letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Define uma função para incriptar as mensgens que tem como parametro a mensgam e chave

    def encrypt(self, texto_plano, key):
        # Cria a variavel que irá armazenar o texto cifrado
        cipher_text = ''
        # passa a mensagem original para letras maiúsculas
        texto_plano = texto_plano.upper()
        # itera sobre os caracteres do texto
        for ch in texto_plano:
            # Verifica se o caractere esxiste no alfabeto

            if ch in self.__letters:
                # Soma a chave com o index da letra atual
                idx = self.__letters.find(ch) + key

                # Verifica se o index é maior que 26
                if idx >= 26:
                    # Subtrai 26 do index
                    idx -= 26
                    # Adiciona a mnsagfem cifrada a letra cifrada
                cipher_text += self.__letters[idx]

        # Retorna a mensagem cifrada
        return cipher_text


# Enquanto a mensagem normal for diferente de 0
while(mensagem_normal != 0):
    # Armazena à mensgam normal o valor ditado plo usuário
    mensagem_normal = input("Digite uma mensagem ")
    # Armazena a variavél opt a opção desejada
    opt = int(input("Qual opção você deseja realizar: 0) Sair 1) Cifra de Cesar"))

    if opt == 0:
        # Imprime uma mensgam de saída
        print("Fechando conexão!")
        break

    if opt == 1:
        # Armazena o valor da chave atraves de um inout do usuário
        chave = int(input("Digite uma chave "))
        # Encripta a mensagem utizando a chave informada
        mensagem_cifrada = Cesar().encrypt(mensagem_normal, chave)
        # atualiza o valor de mensagem cifrada para a concatenação de  mensagem e ")"
        mensagem_cifrada = mensagem_cifrada + ')'
        # Envia a mensagem cifrada para o servidor
        client_socket.sendall(mensagem_cifrada.encode('utf-8'))
        # Imprim na tela uma confirmação de mensagem enviada
        print("Mensagem enviada")

# Fecha a conexão entre cliente e servidor
client_socket.close()
