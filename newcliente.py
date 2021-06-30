#! /usr/bin/env python


#import thread
import threading
import os.path
from random import randrange
import random
import hashlib
import socket
import time
import copy
import socket
import sys
from math import *

# TCP

ip = "127.0.0.1"
port = 9093
mensagem_cifrada = ""
mensagem_normal = ""
mensagem_transposicao = ""
chave = ""
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect(addr)


class Cesar:
    def __init__(self):
        self.__letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, texto_plano, key):

        cipher_text = ''
        texto_plano = texto_plano.upper()
        for ch in texto_plano:
            if ch in self.__letters:  # se o caracter existe no alfabeto
                # se encontrar o indice no alfabeto, soma com a chave
                idx = self.__letters.find(ch) + key
                if idx >= 26:
                    idx -= 26
                cipher_text += self.__letters[idx]
        return cipher_text


def le_arquivo(arquivo):
    leitura_arq = ""
    f = open(arquivo)
    leitura_arq = f.read()
    return leitura_arq


def escrever_arquivo(arquivo, texto):
    f = open(arquivo, 'w')
    f.writelines(texto)
    f.close()
    return 1


while(mensagem_normal != 0):

    mensagem_normal = input("Digite uma mensagem ")
    #mensagem_normal = le_arquivo ("mensagem.txt")
    # print(mensagem_normal)

    opt = int(input(
        "Qual opcao voce deseja realizar: 0) Sair 1) Cifra de Cesar 2) Hacker de Cesar"))
    if opt == 0:
        break
    if opt == 1:
        chave = int(input("Digite uma chave "))
        mensagem_cifrada = Cesar().encrypt(mensagem_normal, chave)
        escrever_arquivo("cifrada.txt", mensagem_cifrada)
        mensagem_cifrada = mensagem_cifrada + ')'
        client_socket.sendall(mensagem_cifrada.encode('utf-8'))
    if opt == 2:
        chave = int(input("Digite uma chave "))
        mensagem_cifrada = Cesar().encrypt(mensagem_normal, chave)
        escrever_arquivo("cifrada.txt", mensagem_cifrada)
        mensagem_cifrada = mensagem_cifrada + '!' + mensagem_normal
        client_socket.sendall(mensagem_cifrada.encode('utf-8'))

    print("Mensagem enviada")
client_socket.close()
