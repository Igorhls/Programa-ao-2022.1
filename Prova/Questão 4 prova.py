n1 = float(input('Nota do Primeiro Bimestre: '))
n2 = float(input('Nota do Segundo Bimestre: '))

m = (n1 * 2 + n2 * 3) / 5

print('A média do aluno é {}' .format(m))

if 7 > m >= 2:
  print('O Aluno está em Recuperação!')

elif m < 2:
  print('O Aluno está Reprovado!')

else:
  print('O Aluno está Aprovado!')