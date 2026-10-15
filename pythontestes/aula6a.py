n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: ' ))
s = n1 + n2
#print('A soma entre:', n1, 'e', n2, 'equivale a:', s) - Sintaxe antigo.
print('A soma entre {} e {} equivale a:{}'.format(n1, n2, s)) #Sintaxe moderno