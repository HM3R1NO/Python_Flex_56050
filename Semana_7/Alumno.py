"""
Crea una clase Auto que contenga 2 atributos de instancia.

Con esa clase, crea un auto y muestra los datos del auto creado.

Como se define una clase, el constructor (__init__), sus atributos de instancia y como una vez creado un objeto como acceder a sus datos.

"""


class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Crear una instancia de la clase Auto
mi_auto = Auto("Toyota", "Corolla")

# Mostrar los datos del auto creado
print(f"Marca: {mi_auto.marca}")
print(f"Modelo: {mi_auto.modelo}")

"""
Crea una clase llamada Alumno, que posea como atributos de instancia el nombre y la nota del estudiante. Como métodos propios de la clase, se deberán definir correspondientemente el constructor, el método imprimir y resultado. 
Aclaración: Tanto los atributos como métodos, son de tipo públicos.
Importante: En la siguiente actividad en clase, implementaremos nuestro Diagrama de Clase, directamente en Python.

"""

# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def imprimir(self):
#         print(f"Nombre del alumno: {self.nombre}")
#         print(f"Nota del alumno: {self.nota}")

#     def resultado(self):
#         if self.nota >= 7:
#             return "Aprobado"
#         else:
#             return "Reprobado"
    
#     def __str__(self):
#         return f"Nombre del alumno: {self.nombre} \n Nota del alumno: {self.nota}"

# # Crear una instancia de la clase Alumno
# alumno1 = Alumno("Juan", 8)

# # Utilizar los métodos para imprimir los datos del alumno y su resultado
# alumno1.imprimir()
# print(f"Resultado: {alumno1.resultado()}")
# print(20*"*")
# print(alumno1)

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
