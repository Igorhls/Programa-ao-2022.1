lp = []
im = 0

for _ in range(0,3):
    p = input('Digite nome, idade: ')
    nome, idade = p.split(',')
    lp.append({'nome': nome, 'idade': int(idade) })
    im += int(idade)





qp = len(lp)
im = im / qp

print(f'{qp} Cadastradas')
print(f'Idade Media: {im}')



