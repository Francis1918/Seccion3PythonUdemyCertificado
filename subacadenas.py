#extraer una sub cadena usando slicing
#Manejo de sub cadenas
cadena = "Hola Mundo"
#Extraer la subcadena "Hola"
subcadena_hola = cadena[0:4]
print(subcadena_hola)
print(f"La subcadena es: {subcadena_hola}")
#forma alternativa
print(f'La subcadena es: {cadena[0:4]}')
#Extraer la subcadena "Mundo"
subcadena_mundo = cadena[5:10]
print(subcadena_mundo)
print(f"La subcadena es: {subcadena_mundo}")
#Forma alternativa
print(f'La subcadena es: {cadena[5:10]}')
#Extraer la subcadena "Mundo" usando slicing negativo
subcadena_mundo_negativo = cadena[-5:]
print(subcadena_mundo_negativo)
print(f"La subcadena es: {subcadena_mundo_negativo}")
#Forma alternativa
print(f'La subcadena es: {cadena[-5:]}')
