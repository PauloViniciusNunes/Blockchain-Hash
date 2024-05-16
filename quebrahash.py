import time
from random import randint as rant
from os import system as sys

alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hash = ''
sys('color a')
dificuldade = int(input("Defina a dificuldade: "))
for i in range(0, dificuldade):

    hash += alfa[rant(0, len(alfa) - 1)]

inicio = time.time()

while True:
    hash_key = ''
    for j in range(0, dificuldade):
        hash_key += alfa[rant(0, len(alfa) - 1)]
    print(hash_key)
    if hash_key == hash:
        sys('cls')
        break


fim = time.time()

minutos = int((fim-inicio)/60)
segundos = int((fim-inicio)%60)
print(f"HASH DESCOBERTO: {hash_key}")
print(f"Tempo para quebrar o hash: {minutos} minutos e {segundos} segundos")
input("")

