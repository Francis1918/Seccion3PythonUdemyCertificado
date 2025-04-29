#formato de cadenas en python
# uso de f-strings (Requires Python 3.6+) y Recomendado por la comunidad
# Definicion de variables
nombre = 'Juan'
apellido = 'Gonzalez'
edad= 30
resultado = f'Hola {nombre} {apellido}, tengo {edad} años'
print(resultado)
#metodo format
resultado2 = 'Hola {} {}, tengo {} años'.format(nombre, apellido, edad)
print(resultado2)