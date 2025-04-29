# inmutabilidad en cadenas
cadena1 = "Hola mundo"
#cadena1[0] = "h"  # Esto generará un error porque las cadenas son inmutables
# el str no soporta la asignación de un índice
# cadena1[0] = "h"  # Esto generará un error porque las cadenas son inmutables
cadena2=cadena1#respaldo de la variable de cadena1 original antes del cambio
cadena1 = 'Adios'
print(cadena1)
print(cadena2)