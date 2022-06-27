m = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

data = input("Digite a sua data de nascimento utilizando numeros no formato dia/mes/ano: ")
dia, mes, ano = data.split("/")
mes = int(mes)-1

print ("Voce nasceu em {} de {} de {}" .format(dia, m[mes], ano))