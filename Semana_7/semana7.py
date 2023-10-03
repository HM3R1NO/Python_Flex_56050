"""
? Auto
Crear una clase Auto que contenga 2 atributos de instancia.  
Con esta clase crear un auto y mostrar los datos del auto creado.
"""

class Auto:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

mi_auto = Auto('Ford', 'K')


print(f"Marca: {mi_auto.marca}")
print(f"Modelo: {mi_auto.modelo}")


"""
? Pasemoslo a Python
Implementar la Clase de Alumno, creada en la actividad anterior, directamente en Python.   
Aclaraciones Generales:
* El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
* El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos o igual a 5 puntos desaprueba la materia, más de 5 puntos aprueba. Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
* Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.
"""

class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def imprimir(self):
    print(self.nombre, self.nota)

  def resultado(self):
    print('Aprobado' if self.nota > 5 else 'Desaprobado')

alumno1 = Alumno('Pepe', 3)
alumno2 = Alumno('Ricardo', 6)

"""
? Vehiculos

Crear una Clase Vehiculo de la cual van a heredar la clase Auto (del microdesafio) y la clase Lancha (nueva, tiene como atributo nombre de motor). Ademas, crear una clase MovimientosEmbarcacion de la cual tambien heredara Lancha.   
Implementar los metodos arrancar, tocar_bocina, virar_a_estribor, virar_a_babor y  abrir_capot en la clase que corresponda. Solo deben mostrar un mensaje que se ejecuto la accion.
"""

class Vehiculo:
  def arrancar(self):
    print('Brrrum')
  def tocar_bocina(self):
    print('Piiii!!! Piiii!!!')

class MovimientosEmbarcacion:
  def virar_a_estribor(self):
    print('Virando a estribor.')
  def virar_a_babor(self):
    print('Virando a babor.')

class Auto(Vehiculo):
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  def abrir_capot(self):
    print('Abriendo capot.')

class Lancha(Vehiculo, MovimientosEmbarcacion):
  def __init__(self, motor):
    self.motor = motor
    
"""
?Televisores

Crear un programa que al pasarle una lista de televisores devuelva el total a pagar.
Tener en cuenta los siguientes puntos sobre los televisores:
1. Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso.
2. Los colores disponibles son blanco, negro, rojo, azul y gris.
3. Por defecto, el color sera blanco, el consumo energético sera F, el precio_base es de 100 $ y el peso de 5 kg.
4. Tienen 3 funcionalidades:
  * Una para comprobar que la letra (consumo energético) es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y sera privada.
  * Otra para comprobar que el color es correcto (no importa si el nombre esta en mayúsculas o en minúsculas), sino usa el color por defecto. Se invocara al crear el objeto y sera privada al igual que la anterior.
  * Y la ultima devolvera el precio final del televisor, que aumentara su precio según el tamaño y su consumo energético.  

!La lista de precios segun tamaño y consumo son:
```
Letra | Precio
  A   |   $100
  B   |    $80
  C   |    $60
  D   |    $50
  E   |    $30
  F   |    $10
```
```
Tamaño            | Precio
Entre 0 y 19 kg   |    $10
Entre 20 y 49 kg  |    $50
Entre 50 y 79 kg  |    $80
Mayor que 80 kg   |   $100
```

Probar con los siguientes televisores:
* precio base 250, color rojo, consumo energético E y peso 10  
* precio base 143, color negro, consumo energético C y peso 13  
* precio base 54, color gris, consumo energético A y peso 7  
* precio base 300, color violeta, consumo energético B y peso 23  
"""

class Televisor:

  colores = ['blanco', 'negro', 'rojo', 'azul', 'gris']
  letras_costo = {'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10}

  def __init__(self, precio_base=100, color='blanco', letra_consumo='F', peso=5):
    self.precio_base = precio_base
    self.color = self.__comprobar_color(color)
    self.letra_consumo = self.__comprobar_consumo(letra_consumo)
    self.peso = peso

  def __comprobar_consumo(self, letra):
    return letra if letra.upper() in self.letras_costo.keys() else 'F'

  def __comprobar_color(self, color):
    return color if color.lower() in self.colores else 'blanco'

  def precio_final(self):
    if 0 <= self.peso <= 19:
      precio_x_tamanio = 10
    elif 20 <= self.peso <= 49:
      precio_x_tamanio = 50
    elif 50 <= self.peso <= 19:
      precio_x_tamanio = 80
    elif 80 <= self.peso:
      precio_x_tamanio = 100
    precio_x_consumo = self.letras_costo.get(self.letra_consumo)
    return self.precio_base + precio_x_consumo + precio_x_tamanio


def total_a_pagar(lista_teles):
    suma = 0
    for tele in lista_teles:
      suma += tele.precio_final()
    return suma


compras = [
    Televisor(250,'rojo', 'E', 10),
    Televisor(143,'negro', 'C', 13),
    Televisor(54,'gris', 'A', 7),
    Televisor(300,'violeta', 'B', 23),
]

print(total_a_pagar(compras))

"""
? Electrodomesticos

Ahora cambiemos la clase Televisor a Electrodomestico y creemos una nueva clase Televisor y otra Lavadora que hereden de Electrodomestico. Estas nuevas clases deberan, ademas de cumplir con lo heredado, agregar lo siguiente:  
El Televisor:
* Tener los atributos “resolucion” (float, por defecto 20 pulgadas) y “sintonizador TDT” (booleano, por defecto False);
* Y, al precio final, si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% y si tiene un sintonizador TDT incorporado, aumentara $50  

La Lavadora:
* Tener el atributo carga (float, por defecto 5 kg);
* Y, al precio final, si tiene una carga mayor de 30 kg, aumentara el precio $50

"""

class Electrodomestico:

  colores = ['blanco', 'negro', 'rojo', 'azul', 'gris']
  letras_costo = {'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10}

  def __init__(self, precio_base=100, color='blanco', letra_consumo='F', peso=5):
    self.precio_base = precio_base
    self.color = self.__comprobar_color(color)
    self.letra_consumo = self.__comprobar_consumo(letra_consumo)
    self.peso = peso

  def __comprobar_consumo(self, letra):
    return letra if letra.upper() in self.letras_costo.keys() else 'F'

  def __comprobar_color(self, color):
    return color if color.lower() in self.colores else 'blanco'

  def precio_final(self):
    if 0 <= self.peso <= 19:
      precio_x_tamanio = 10
    elif 20 <= self.peso <= 49:
      precio_x_tamanio = 50
    elif 50 <= self.peso <= 19:
      precio_x_tamanio = 80
    elif 80 <= self.peso:
      precio_x_tamanio = 100
    precio_x_consumo = self.letras_costo.get(self.letra_consumo)
    return self.precio_base + precio_x_consumo + precio_x_tamanio


def Televisor(Electrodomestico):
  # v1
  def __init__(self, precio_base, color, letra_consumo, peso, resolucion=20, sintonizador_TDT=False):
    super(self).__init__(precio_base, color, letra_consumo, peso)

  # v2
  # def __init__(self, resolucion=20, sintonizador_TDT=False, *args, **kwargs):
  #   super(self).__init__(*args, **kwargs)

  def precio_final(self):
    extras = 0
    if self.resolucion > 40:
      extras *= 1.3
    if self.sintonizador_TDT:
      extras += 50
    return super(self).precio_final()


def Lavadora(Electrodomestico):
  # v1
  def __init__(self, precio_base, color, letra_consumo, peso, carga=5):
    super(self).__init__(precio_base, color, letra_consumo, peso)

  # v2
  # def __init__(self, carga=5, *args, **kwargs):
  #   super(self).__init__(*args, **kwargs)

  def precio_final(self):
    return super(self).precio_final() + 50 if self.carga > 30 else 0