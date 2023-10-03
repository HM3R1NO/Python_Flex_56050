"""
Descripción de la actividad. 

Crea una Clase Vehiculo, de la cual van a heredar la clase Auto (del microdesafío) y la clase Lancha (nueva, tiene como atributo nombre de motor). Además, crea una clase MovimientosEmbarcacion de la cual también heredará Lancha.
Implementa los métodos arrancar, tocar_bocina, virar_a_estribor, virar_a_babor y  abrir_capot en la clase que corresponda. Solo debes mostrar un mensaje indicando que se ejecutó la acción.

"""

class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado.")

    def tocar_bocina(self):
        print("El vehículo ha tocado la bocina.")

class Auto(Vehiculo):
    def abrir_capot(self):
        print("El capot del auto se ha abierto.")

class MovimientosEmbarcacion:
    def virar_a_estribor(self):
        print("La embarcación ha virado a estribor.")

    def virar_a_babor(self):
        print("La embarcación ha virado a babor.")

class Lancha(Vehiculo, MovimientosEmbarcacion):
    def __init__(self, nombre_motor):
        self.nombre_motor = nombre_motor

    def abrir_capot(self):
        print("No hay capot en una lancha.")

# Crear una instancia de la clase Auto y llamar a sus métodos
mi_auto = Auto()
mi_auto.arrancar()
mi_auto.tocar_bocina()
mi_auto.abrir_capot()

# Crear una instancia de la clase Lancha y llamar a sus métodos
mi_lancha = Lancha("MotorX")
mi_lancha.arrancar()
mi_lancha.tocar_bocina()
mi_lancha.virar_a_estribor()
mi_lancha.virar_a_babor()
mi_lancha.abrir_capot()
