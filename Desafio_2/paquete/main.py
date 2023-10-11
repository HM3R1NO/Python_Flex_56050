#Código del módulo main.py (utilizará la clase Customer):
from paquete.customer import Customer

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
