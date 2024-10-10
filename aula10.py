"""
Laço for em Python
   iterando string com for
"""
"""
for n in range (0,100,8):

    print(n)
print('###############')

for n in range(0,100):
    if n % 8 == 0:
        print(n)    """

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
       nova_string +=  letra.upper()
       
    else:
        nova_string +=  letra


print(nova_string)