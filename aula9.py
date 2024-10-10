"""
Iterando strings com while em Python
"""

minha_string = 'o rato roeu a roupa do rei de roma!'
tamanho_string = len(minha_string)
c= 0

while c < tamanho_string:

    print(c,minha_string[c])
    c += 1