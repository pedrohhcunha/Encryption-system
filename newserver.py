#! /usr/bin/env python

# import thread
import threading
import os.path
import random
import hashlib
import socket
import time
import os
import copy
import socket

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
host = ''
port = 9093
pega_mensagem = ''
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(1)
tam_mensagem = ""

print('Aguardando cliente...')
con, cliente = serv_socket.accept()
print('Na espera de mensagem')
while(pega_mensagem != 0):
    pega_mensagem = con.recv(1024)
    alfabeto_normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print("Chegou a mensagem " + pega_mensagem.decode('utf-8'))
    pega_mensagem = pega_mensagem.decode('utf-8')

    # se encontrar o caractere retorna seu indice
    if (pega_mensagem.find('!', 0, len(pega_mensagem)) != -1):

        tam_mensagem = len(pega_mensagem)/2 + 1

        # Codificar aqui o hacker de Cesar

    if (pega_mensagem.find(')', 0, len(pega_mensagem)) != -1):
        tmp = pega_mensagem.split(')')
        pega_mensagem = tmp[0]
        decipher_text = ''
        print(pega_mensagem)
        chave = input("Digite a chave de quebra da mensagem")

        decodedMessage = []
        for letter in pega_mensagem:
            indexLetterInAlfabet = alfabeto_normal.find(letter)
            letterDecoded = indexLetterInAlfabet - int(chave)
            if letterDecoded < 0:
                print(letterDecoded, 'foi menor que 0')
                letterDecoded += 26
            print(indexLetterInAlfabet, letterDecoded)
            decodedMessage.append(alfabeto_normal[letterDecoded])

        output = ''.join(decodedMessage)
        print(output)
        # Codificar aqui a decifragem da mensagem

serv_socket.close()
