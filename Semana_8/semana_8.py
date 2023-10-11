# import sys
# print(sys.argv)

# import sys

# # Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
# if len(sys.argv) == 3:
#     texto = sys.argv[1]
#     repeticiones = int(sys.argv[2])
#     for r in range(repeticiones):
#         print(texto)
# else:
#     print("Error - Introduce los argumentos correctamente")
#     print('Ejemplo: escribir_lineas.py "Texto" 5')

"""
TODO: MICRODESAFIO
#Descripción de la actividad. 
Hacer una clase fácil, como Alumno, con nombre y nota, con un método imprimir().
Crear una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo.

Creación y uso de un módulo creado por nosotros.
"""
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota
        
#     def imprimir(self):
#         print("Imprimiendo...")


# alumno = Alumno("Emanuel",7)
# alumno.imprimir()
"""
?2)Descripción de la actividad. 

Calcula tu edad con la mayor precisión posible y cuántos segundos faltan para tu cumpleaños. Utiliza un módulo llamado fechas.py.

!Usando los módulos del microdesafio 08 y la actividad “edad y precisión” genera un paquete redistribuíble.

"""
# from datetime import datetime


# dia = int(input('Ingrese dia (numero) de nacimiento: '))
# mes = int(input('Ingrese mes (numero) de nacimiento: '))
# anio = int(input('Ingrese año de nacimiento: '))

# hoy = datetime.now()
# nacimiento = datetime(anio, mes, dia)

# tiempo = hoy - nacimiento
# print(tiempo)
# anios = tiempo.days // 365
# meses = (tiempo.days % 365) // 30 # aproximado
# dias = (tiempo.days % 365) % 30
# horas = tiempo.seconds // 3600
# min = (tiempo.seconds % 3600) // 60
# seg = (tiempo.seconds % 360) % 60

# print(f'Tenes Años: {anios}, meses: {meses}, dias: {dias}, horas: {horas}, minutos: {min}, segundos: {seg}.')

# proximo = datetime(hoy.year + 1, mes, dia)
# (proximo - hoy).total_seconds

# print(f'Faltan {(proximo - hoy).total_seconds()} seg para tu cumpleaños.')


"""
?3)Descripción de la actividad. 

Crea un programa que pida por teclado (input) los datos de tus tres hobbies favoritos y los mismos se guarden en un archivo que se llame miHobbieFavorito.txt.

EXTRA: Hazlo con un for o un while para no repetir tanto…

"""

# archivo = open('miHobbieFavorito.txt', 'w')
# for i in range(1,4):
#     archivo.write(input('Ingrese su hobbie numero {i}: ')+ " \n")
# archivo.close()


"""
?4) Ejemplo en vivo: Tablas

Desarrollaremos:

una función que pida un número entero y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.

una función que pida un número entero, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe, debe mostrar un mensaje por pantalla informando de ello.

Estas 2 funciones deben ser seleccionadas por el usuario dentro de un menú.

"""
# def generar(numero):
#   datos = open(f'tabla-{numero}.txt', 'w')
#   for i in range(1,11):
#     datos.write(f'{numero} x {i} = {numero*i}\n')
#   datos.close()

# def mostrar(numero):
#   try:
#     datos = open(f'tabla-{numero}.txt', 'r')
#   except FileNotFoundError as e:
#     print('No se encontro el archivo correspondiente.')
#   print(datos.read())
#   datos.close()
  
# def buscar_linea(numero):
#   linea = int(input('Ingrese linea (1 a 10):'))
#   try:
#     datos = open(f'tabla-{numero}.txt', 'r')
#     lineas = datos.readlines()
#     print(lineas[linea-1])
#     datos.close()
#   except FileNotFoundError as e:
#     print('No se encontro el archivo correspondiente.')
#     confirmacion = input('Desea generar la tabla? ("si" para confirmar)').lower()
#     if confirmacion == 'si': 
#         generar(numero)
#         buscar_linea(numero)

# def menu():
#     while True:
#         print('''Menu
#         1. Generar tabla de multiplicar.
#         2. Mostrar tabla de multiplicar.
#         3. Mostrar linea de la tabla de multiplicar.
#         4. Salir
#         ''')
#         opcion = input('Ingrese opcion: ')
#         if opcion not in ['1','2','3','4']:
#             print('No ingreso ninguna opcion valida.')
#             continue
#         if opcion == '1':
#             num = int(input('Ingrese numero a operar:'))
#             generar(num)
#         elif opcion == '2':
#             num = int(input('Ingrese numero a operar:'))
#             mostrar(num)
#         elif opcion == '3':
#             num = int(input('Ingrese numero a operar:'))
#             buscar_linea(num)
#         elif opcion == '4':
#             break

# menu()

"""
?5)Otra opción

Descripción de la actividad. 

Agrega al ejemplo anterior una opción que pida dos números n y m, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
Si el fichero no existe, debe mostrar un mensaje por pantalla informando de ello y consultando si se desea generar.

"""


"""
?6)Agenda de contactos

Descripción de la actividad. 

Crea un menú con las opciones de agendar contacto y ver información de contacto.
Para agendar se solicitará al usuario: nombre, apellido, teléfono, dirección.
Para ver informacion se pedirá el nombre y apellido.
La información será un listado de diccionarios, donde cada diccionario tendrá como claves lo solicitado al usuario y como valor lo que ingrese el usuario. A su vez, este listado debe estar guardado en un archivo JSON.


"""
import json

def obtener_agenda():
    try:
        with open(f'agenda.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError as e:
        return []

def agendar():
    agenda = obtener_agenda()
    contacto = {
        'nombre': input('Ingrese su nombre: '),
        'apellido': input('Ingrese su apellido: '),
        'telefono': input('Ingrese su telefono: '),
        'direccion': input('Ingrese su direccion: '),
    }
    agenda.append(contacto)
    with open(f'agenda.json', 'w') as archivo:
        json.dump(agenda, archivo, indent=4)

        
def ver_contacto():
    nombre_a_buscar = input('Ingrese nombre: ')
    apellido_a_buscar = input('Ingrese apellido: ')
    agenda = obtener_agenda()
    for contacto in agenda:
        if contacto['nombre'] != nombre_a_buscar or contacto['apellido'] != apellido_a_buscar:
            continue
        print(f"""
    Nombre: {contacto['nombre']}
    Apeliido: {contacto['apellido']}
    Telefono: {contacto['telefono']}
    Direccion: {contacto['direccion']}
    """)
        break
    else:
        print(f'No se encontro el contacto {nombre_a_buscar} {apellido_a_buscar}.')

def menu():
  print('''Menu
  1. Agendar contacto.
  2. Ver contacto.
  ''')
  opcion = input('Ingrese opcion: ')
  if opcion not in ['1','2']:
    print('No ingreso ninguna opcion valida.')
    return
  if opcion == '1':
    agendar()
  elif opcion == '2':
    ver_contacto()

menu()
