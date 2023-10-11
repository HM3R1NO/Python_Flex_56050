#Crear el archivo setup.py para el paquete:
from setuptools import setup, find_packages

setup(
    name='shopping-page',
    version='0.1',
    packages=find_packages(),
)

# setup(
#     name="mi_primer_paquete",
#     version="1.0",
#     author="Clase 8 CODER - Python",
#     description="Estamos haciendo el primer paquete distribuido",
#     author_email="coder@coder.com",
#     packages=["mi_primer_paquete"]
# )

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