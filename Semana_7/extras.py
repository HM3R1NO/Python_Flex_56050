# yield es una palabra clave en Python que se utiliza en la definición de funciones generadoras. Las funciones generadoras son una forma especial de funciones que permiten generar una secuencia de valores uno a la vez, a medida que se solicitan, en lugar de generar todos los valores de una vez y almacenarlos en la memoria. Esto es especialmente útil cuando se trabaja con secuencias potencialmente grandes de datos.

# Cuando se usa yield dentro de una función, esta función se convierte en una función generadora. En lugar de utilizar return para devolver un valor y finalizar la función, yield se utiliza para proporcionar un valor al llamador y luego "pausar" la función en su estado actual. La función se reanuda desde donde se pausó la próxima vez que se llama, y continúa ejecutándose hasta encontrar otro yield o hasta que termine.

# Aquí hay un ejemplo simple de una función generadora que genera números pares:

def generador_pares(maximo):
    for i in range(2, maximo + 1, 2):
        yield i

# Uso de la función generadora
pares = generador_pares(10)
for numero in pares:
    print(numero)

"""
En este ejemplo, la función generador_pares utiliza un bucle for para generar números pares del 2 al valor máximo especificado. En lugar de utilizar return para devolver los valores, se utiliza yield para proporcionar cada número par uno a la vez. Cuando se itera sobre el generador en un bucle for, la función se pausa después de cada yield y se reanuda en el siguiente ciclo del bucle.

El uso de yield en funciones generadoras permite ahorrar memoria, ya que no es necesario almacenar toda la secuencia de valores en la memoria, especialmente cuando se trabaja con grandes conjuntos de datos o secuencias infinitas. También es útil cuando se necesita generar valores de manera perezosa, es decir, generarlos solo cuando se necesiten.
"""
"""
===========================================================================
Python tiene varios métodos especiales (también conocidos como métodos mágicos o métodos dunder, debido a que su nombre comienza y termina con doble guion bajo __). Estos métodos permiten definir el comportamiento personalizado de objetos en diferentes contextos, como la representación de cadenas, la aritmética, la comparación y más. Aquí hay algunos ejemplos de métodos especiales junto con sus descripciones:

__str__(self): Este método permite definir una representación legible en forma de cadena de un objeto. Se llama cuando se utiliza la función str() o la función print() en una instancia de la clase.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

persona1 = Persona("Juan", 30)
print(persona1)  # Esto llama a __str__

# __len__(self): Este método permite definir la longitud de un objeto, y se llama cuando se utiliza la función len() en una instancia de la clase.
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

mi_lista = MiLista([1, 2, 3, 4, 5])
print(len(mi_lista))  # Esto llama a __len__

#__add__(self, other): Este método permite definir la operación de suma (+) entre dos objetos de la misma clase.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

punto1 = Punto(1, 2)
punto2 = Punto(3, 4)
resultado = punto1 + punto2  # Esto llama a __add__
print(resultado.x, resultado.y)

#__eq__(self, other): Este método permite definir el comportamiento de igualdad (==) entre dos objetos de la misma clase.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return self.edad == other.edad

persona1 = Persona("Juan", 30)
persona2 = Persona("María", 30)
print(persona1 == persona2)  # Esto llama a __eq__

"""
!Estos son solo algunos ejemplos de métodos especiales en Python. Hay muchos más, y cada uno permite personalizar el comportamiento de los objetos de acuerdo con las necesidades de tu programa.
"""