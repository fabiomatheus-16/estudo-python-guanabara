#Exemplo : import(bebida) = importa toda a biblioteca
#        : from.doce.importe(agua) = importa somente aquele item da biblioteca
#Exemplo de biblioteca: math = matématica, vai trazer funcionalidades matématicas.
# import(math): ceil, floor, trunc, pow, sqrt, factorial
#from.math.import(sqrt) = somente a função raiz quadrada.

#from math import sqrt, floor
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de um {} é igual a {}'.format(num, raiz))

import emoji 
texto = emoji.emojize('Olá, mundo :earth_americas:', language='en')
print(texto)