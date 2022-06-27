# Números repetidos

l = []

for _ in range(10):
    n = input('Digite um número: ')
   
    if l.count(n) == 0:
            l.append(n)

print(l)

          
