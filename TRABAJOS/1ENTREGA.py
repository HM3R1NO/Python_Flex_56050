# Base de datos de usuarios almacenada como un diccionario
usuarios_db = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios_db:
        print("El usuario ya está registrado. Por favor, elija otro nombre de usuario.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios_db[usuario] = contrasena
        print("Usuario registrado con éxito.")

# Función para verificar las credenciales de inicio de sesión
def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in usuarios_db and usuarios_db[usuario] == contrasena:
        print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario))
    else:
        print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")

# Función principal para ejecutar el programa
def main():
    while True:
        print("\nMenú:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()