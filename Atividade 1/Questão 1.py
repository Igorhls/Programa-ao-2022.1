# Equação do segundo grau

a = int(input('Entre com o valor de A: '))
b = int(input('Entre com o valor de b: '))
c = int(input('Entre com o valor de c: '))

d = b**2 - 4*a*c

x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

print(f'Raizes: x1={x1}, x2={x2}')