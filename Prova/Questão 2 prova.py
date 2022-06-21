frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A quantidade de ´A` nesta frase é de: {frase.count("A")}\n'
        f'O ultimo ´A` esta na posição: {frase.rfind("A")+1 - frase.count(" ")}\n'
         f'O primeiro ´A` esta na posição: {frase.find("A"[0])+1}')