"""
Ejemplo de un programa que modela clientes en una página de compras utilizando Programación Orientada a Objetos en Python. Además, crearé un paquete redistribuible que incluirá el programa.

Estructura de directorios para el paquete:
arduino
Copy code
shopping_page/
    ├── __init__.py
    ├── customer.py
    └── main.py
setup.py
"""
#Código del módulo customer.py:
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def view_cart(self):
        if self.cart:
            print(f"{self.name}'s Shopping Cart:")
            for item in self.cart:
                print(f"- {item}")
        else:
            print(f"{self.name}'s Shopping Cart is empty.")

    def checkout(self):
        if self.cart:
            print(f"{self.name} has checked out. Thank you for your purchase!")
            self.cart = []
        else:
            print(f"{self.name}'s Shopping Cart is empty.")

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}"

#Código del módulo main.py (utilizará la clase Customer):
from customer import Customer

# Crear algunos clientes
customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")

# Realizar compras
customer1.add_to_cart("Product 1")
customer1.add_to_cart("Product 2")
customer2.add_to_cart("Product 3")

# Mostrar carritos de compras
customer1.view_cart()
customer2.view_cart()

# Proceso de pago
customer1.checkout()
customer2.checkout()

# Mostrar estado después del pago
customer1.view_cart()
customer2.view_cart()

#Crear el archivo setup.py para el paquete:
from setuptools import setup, find_packages

setup(
    name='shopping-page',
    version='0.1',
    packages=find_packages(),
)
"""
Para crear el paquete redistribuible, ejecuta el siguiente comando en la terminal:
bash
    python setup.py sdist

Esto creará un archivo shopping-page-0.1.tar.gz en el directorio dist.

Ahora puedes instalar el paquete en tu entorno virtual o en cualquier otro lugar utilizando pip:
    pip install dist/shopping-page-0.1.tar.gz

Luego, puedes importar y usar la clase Customer en tu proyecto.

Este ejemplo demuestra la programación orientada a objetos con una clase Customer, atributos de instancia (name, email, cart), métodos (add_to_cart, view_cart, checkout), y el uso de un paquete redistribuible. Puedes expandir este programa según tus necesidades.
"""