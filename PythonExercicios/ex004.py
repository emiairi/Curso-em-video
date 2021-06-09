texto = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(texto))
'''print('Só tem espaço?', texto.isspace())
print('É um número?', texto.isnumeric())
print('É alfabético?', texto.isalpha())
print('É alfanumérico?', texto.isalnum())
print('Está em maiúsculo?', texto.isupper())
print('Está em minúsculo?', texto.islower())
print('Está capitalizado?', texto.istitle())'''

print('Só tem espaço? {}'.format(texto.isspace()))