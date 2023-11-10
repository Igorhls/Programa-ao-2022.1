import random
from random import choice

ln = []
for _ in range(0,4):
    n = input('Digite um nome: ')
    ln.append(n)

print(choice(ln))



