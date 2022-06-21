def colaboradores(n):
    return n*10/100

def parceiros(n):
    return n*7/100    

n = float(input('Digite o valor do produto: '))
print(f'o valor do produto com o desconto de colaborador é {colaboradores(n)}')
print(f'O valor do produto com o desconto de parceiros é {parceiros(n)}')
