import re

'''
Laboratorio de Lenguajes Formales y de Programación
Sección: A-
Tutor: Mario Josué Solis Solórzano
Josué Daniel Rojché García
Carnet: 201901103
'''

# /************* Ejemplo #1 *******************
print('************** Ejemplo #1 *******************')
texto = 'El carro es pequeña, el carro es azul.'
print("Correcta: ",re.findall("carro", texto))
print("Incorrecta: ", re.match("carro", texto))

# /************** Ejemplo #2 *******************
print('\n************** Ejemplo #2 *******************')
texto1 = 'La musica es fantastica, y es tranquila.'
print("Correcta: ",re.search("musica", texto1))
print("Incorrecta: ", re.match("musica", texto1))

# /************** Ejemplo #3 *******************
print('\n************** Ejemplo #3 *******************')
texto2 = '''El gato llora mucho, el gato tiene hambre, por favor compra comida para el gato.'''
print("Correcta: ",re.findall("gato", texto2))
print("Incorrecta: ", re.match("gato", texto2))