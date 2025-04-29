#generador de Email
nombre = ' Francis Bravo '
organiazacion = ' Escuela Politécnica Nacional '
dominio = ' epn.edu.ec '
print(f'Nombre: {nombre}')
#Normalizar el nombre
nombre_usuario = nombre.strip()#un metodo a la vez

nombre_usuario = nombre_usuario.lower()#un metodo a la vez
nombre_usuario = nombre_usuario.replace(' ', '.')#un metodo a la vez
print(f'Nombre de usuario: {nombre_usuario}')
print(f'Organizacion: {organiazacion}')
organiazacion = organiazacion.strip()#un metodo a la vez
#extension del dominio
dominio = dominio.strip()
print(f'Dominio: {dominio}')
#Generar el email
email = f'{nombre_usuario}@{dominio}'
print(f'Email: {email}')