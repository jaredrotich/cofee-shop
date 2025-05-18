from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Marto")
c2 = Customer("Shiro")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 2.0)
c2.create_order(coffee1, 5.0)

print("Customers for Latte:", [c.name for c in coffee1.customers()])
print("Most aficionado for Latte:", Customer.most_aficionado(coffee1).name)
