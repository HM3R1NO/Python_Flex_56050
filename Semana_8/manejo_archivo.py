"""
Supongamos que tenemos un archivo de texto llamado "ejemplo.txt" con el siguiente contenido:

Este es un ejemplo de lectura de archivos en Python.
Puede ser útil para procesar archivos de texto.
Espero que estos ejemplos te sean de ayuda.

Aquí comienza un nuevo párrafo.
Este es el segundo párrafo.
"""
#Leer una línea a la vez:
# with open("ejemplo.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())  # strip() elimina caracteres de nueva línea y espacios en blanco \n
# print("===============================================================")
"""
Resultado:

Este es un ejemplo de lectura de archivos en Python.
Puede ser útil para procesar archivos de texto.
Espero que estos ejemplos te sean de ayuda.
Aquí comienza un nuevo párrafo.
Este es el segundo párrafo.
"""
# #Leer todo el contenido del archivo:
# with open("ejemplo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)

"""
Resultado:
Este es un ejemplo de lectura de archivos en Python.
Puede ser útil para procesar archivos de texto.
Espero que estos ejemplos te sean de ayuda.

Aquí comienza un nuevo párrafo.
Este es el segundo párrafo.
"""
#Leer párrafos (bloques de texto separados por líneas en blanco):

# with open("ejemplo.txt", "r") as archivo:
#     parrafo_actual = ""
#     for linea in archivo:
#         if linea.strip():  # Ignora líneas en blanco
#             parrafo_actual += linea
#         else:
#             if parrafo_actual:
#                 print(parrafo_actual)
#                 parrafo_actual = ""
#     if parrafo_actual:
#         print(parrafo_actual)

"""
Resultado:
Este es un ejemplo de lectura de archivos en Python.
Puede ser útil para procesar archivos de texto.
Espero que estos ejemplos te sean de ayuda.

Aquí comienza un nuevo párrafo.
Este es el segundo párrafo.
Estos son ejemplos básicos de lectura de archivos en Python. Puedes adaptarlos según tus necesidades y procesar el contenido del archivo de acuerdo a tus requerimientos específicos.
"""

"""
!Ejemplo y diferencias entre los modos de apertura de archivos en Python: r, r+, w, w+, a y a+.

r (lectura): Abre el archivo en modo de lectura. Si el archivo no existe, se lanza una excepción. Es decir, solo puedes leer el archivo.
"""
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

"""
r+ (lectura y escritura): Abre el archivo en modo de lectura y escritura. El archivo debe existir. Puedes leer y escribir en el archivo.
"""
with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    print("Contenido actual:", contenido)
    archivo.write("Este es un nuevo contenido.")

"""
w (escritura): Abre el archivo en modo de escritura. Si el archivo existe, lo trunca (borra su contenido). Si no existe, se crea un nuevo archivo.
"""
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es el contenido nuevo del archivo.")

"""
w+ (lectura y escritura): Abre el archivo en modo de lectura y escritura. Si el archivo existe, lo trunca (borra su contenido). Si no existe, se crea un nuevo archivo. Puedes leer y escribir en el archivo.
"""
with open("archivo.txt", "w+") as archivo:
    archivo.write("Este es el contenido nuevo del archivo.")
    archivo.seek(0)
    contenido = archivo.read()
    print("Contenido actual:", contenido)
"""
a (anexar): Abre el archivo en modo de anexar. Si el archivo existe, escribe al final del archivo sin borrar su contenido. Si no existe, se crea un nuevo archivo.
"""
with open("archivo.txt", "a") as archivo:
    archivo.write("Este es el nuevo contenido anexado al archivo.")

"""
a+ (anexar y lectura): Abre el archivo en modo de anexar y lectura. Si el archivo existe, escribe al final del archivo sin borrar su contenido. Si no existe, se crea un nuevo archivo. Puedes leer y escribir en el archivo.
"""

with open("archivo.txt", "a+") as archivo:
    archivo.write("Este es el nuevo contenido anexado al archivo.")
    archivo.seek(0)
    contenido = archivo.read()
    print("Contenido actual:", contenido)


#!==============================================
"""
Si deseas abrir un archivo en modo de escritura (w) y crearlo si no existe, pero sin generar un error si el archivo se borró por accidente, puedes hacer lo siguiente:
"""
try:
    with open("archivo.txt", "w") as archivo:
        archivo.write("Este es el contenido nuevo del archivo.")
except FileNotFoundError:
    print("El archivo no existía y ha sido creado.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)

"""
En este código, intentamos abrir el archivo en modo de escritura (w). Si el archivo no existe, se generará una excepción FileNotFoundError, pero capturamos esta excepción y manejamos el caso de que el archivo no existía, creándolo y escribiendo en él. Si ocurre otro error inesperado, lo manejamos también.

Esto garantiza que el programa no se detenga debido a la falta del archivo y, al mismo tiempo, permite crearlo si es necesario.
"""

"""
TODO: Por otro lado, cuando se agrega el símbolo "+" al modo de apertura (por ejemplo, "r+", "a+", "w+"), se permite tanto la lectura como la escritura en el archivo, dependiendo del modo específico. Esto significa que puedes leer y escribir en el archivo en el mismo flujo. Si el archivo no existe, se creará uno nuevo en modo de escritura y, por lo tanto, permitirá la escritura.

TODO: Para resumir, la principal diferencia entre "r", "a" y "w" sin el símbolo "+" es su enfoque principal en la apertura del archivo: lectura, anexado o escritura, respectivamente. El símbolo "+" agrega la funcionalidad adicional de permitir tanto la lectura como la escritura en el archivo en el mismo flujo, y en caso de "w+", trunca el archivo si ya existe.
"""