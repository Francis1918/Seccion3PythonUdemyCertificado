#buscar subcadenas en un string
#uso del metodo find() solo regresa de la primera vez que encuentra la subcadena
# Definimos la cadena de texto
cadena ='hola, mundo!'
indice = cadena.find('mundo')
# Verificamos si se encontró la subcadena
print(f"El indice de la cadena es: {indice}")
#obtener el indice de la subcadena hola
indice = cadena.find('hola')
print(f"El indice de la cadena es: {indice}")