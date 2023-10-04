"""
Atributos privados
"""

class Alumno:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def imprimir(self):
        print(f"Nombre del alumno: {self._nombre}")
        print(f"Nota del alumno: {self._nota}")

#Metodo getter
class Alumno:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def obtener_nombre(self):
        return self._nombre

    def obtener_nota(self):
        return self._nota

    def imprimir(self):
        print(f"Nombre del alumno: {self._nombre}")
        print(f"Nota del alumno: {self._nota}")

# Crear una instancia de la clase Alumno
alumno1 = Alumno("Juan", 8)

# Utilizar los métodos getter para obtener los atributos privados
nombre = alumno1.obtener_nombre()
nota = alumno1.obtener_nota()

print(f"Nombre del alumno: {nombre}")
print(f"Nota del alumno: {nota}")


#Metodo setter
class Alumno:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def obtener_nombre(self):
        return self._nombre

    def obtener_nota(self):
        return self._nota

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def establecer_nota(self, nueva_nota):
        self._nota = nueva_nota

    def imprimir(self):
        print(f"Nombre del alumno: {self._nombre}")
        print(f"Nota del alumno: {self._nota}")

# Crear una instancia de la clase Alumno
alumno1 = Alumno("Juan", 8)

# Utilizar el método setter para modificar el atributo privado
alumno1.establecer_nombre("María")
alumno1.establecer_nota(9)

# Obtener y mostrar los nuevos valores de los atributos
nombre = alumno1.obtener_nombre()
nota = alumno1.obtener_nota()

print(f"Nombre del alumno: {nombre}")
print(f"Nota del alumno: {nota}")
