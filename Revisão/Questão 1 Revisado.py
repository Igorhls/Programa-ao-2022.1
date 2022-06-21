a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

d = b**2 - 4*a*c

x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

print(f'Raizes: x1{x1}, x2{x2}')