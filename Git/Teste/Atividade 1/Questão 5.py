# Números aleatórios

from random import random

l = []

for _ in range(5):
    l.append(int(1000*random()))
n = tuple(l)

print(f'Número = {n}')
print(f'Maior = {sorted(n)[-1]}')
print(f'Menor = {sorted(n)[0]}')