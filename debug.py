

from customer import Customer
from coffee import Coffee
from order import Order

#  customers
alice = Customer("Alice")
bob = Customer("Bob")

# Sample coffee
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# vreating orders
alice.create_order(latte, 5.0)
alice.create_order(espresso, 4.0)
bob.create_order(latte, 6.5)

# testing
print("Alice's coffees:", [c.name for c in alice.coffees()])
print("Latte customers:", [c.name for c in latte.customers()])
print("Latte avg price:", latte.average_price())
print("Most aficionado for Latte:", Customer.most_aficionado(latte).name)
