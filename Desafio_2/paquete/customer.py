#Código del módulo customer.py:
class Customer:
    def __init__(self, name, apellido, email):
        self.name = name
        self.email = email
        self.apellido=apellido
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
        print("agregue")

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
    

