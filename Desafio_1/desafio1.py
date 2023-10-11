####################################################################!
#pip install colorama
import os
from colorama import init, Fore, Style

# Inicializa colorama para habilitar colores en la terminal
init(autoreset=True)

# Nombre del archivo de texto para almacenar los datos de usuarios
archivo_usuarios = "usuarios.txt"

# Base de datos para almacenar usuarios
base_de_datos = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    email = input("Ingrese el correo electrónico del usuario: ")

    if nombre and edad and email:
        usuario = {
            'nombre': nombre,
            'edad': edad,
            'email': email
        }
        base_de_datos[email] = usuario
        guardar_datos()
        print(f"Usuario {nombre} registrado exitosamente.")
    else:
        print("Debe completar todos los campos.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    if base_de_datos:
        print("Usuarios registrados:")
        for email, usuario in base_de_datos.items():
            print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Email: {email}")
    else:
        print("No hay usuarios registrados en la base de datos.")

# Función para guardar los datos de usuarios en un archivo de texto
def guardar_datos():
    with open(archivo_usuarios, 'a') as archivo:
        for email, usuario in base_de_datos.items():
            archivo.write(f"{usuario['nombre']},{usuario['edad']},{email}\n")

# Función para cargar los datos de usuarios desde un archivo de texto
def cargar_datos():
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as archivo:
            for linea in archivo:
                nombre, edad, email = linea.strip().split(',')
                base_de_datos[email] = {
                    'nombre': nombre,
                    'edad': int(edad),
                    'email': email
                }

# Función principal
def main():
    cargar_datos()  # Cargar datos al inicio del programa
    while True:
        print("\nMenú:")
        print(Fore.GREEN + "1. Registrar usuario")
        print(Fore.BLUE + "2. Mostrar usuarios registrados")
        print(Fore.RED + "3. Salir")
        print(Style.RESET_ALL)
        
        opcion = input("Elija una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            print(Fore.YELLOW + "Saliendo del programa.")
            print(Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, elija una opción válida.")
            print(Style.RESET_ALL)

    guardar_datos()  # Guardar datos al salir del programa

if __name__ == "__main__":
    main()

