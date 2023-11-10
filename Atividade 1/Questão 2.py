# Contador de votos

vt = int(input('Entre com o total de votos: '))
vb = int(input('Entre com os votos em branco: '))
vn = int(input('Entre com os votos nulos: '))

vv = vt - vb - vn

print(f'Votos validos = {100*(vv/vt): .2f}%')
print(f'Votos branco = {100*(vb/vt): .2f}%')
print(f'Votos nulos = {100*(vn/vt): .2f}%')