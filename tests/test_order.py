import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validations():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

    c = Customer("Zoe")
    coffee = Coffee("Black")

    with pytest.raises(ValueError):
        Order("not a customer", coffee, 5.0)

    with pytest.raises(ValueError):
        Order(c, "not a coffee", 5.0)

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  # Too cheap

    with pytest.raises(ValueError):
        Order(c, coffee, 20.0)  # Too expensive

    with pytest.raises(ValueError):
        Order(c, coffee, "free")  # Not float

def test_order_assignment():
    c = Customer("Kai")
    coffee = Coffee("Americano")
    order = Order(c, coffee, 4.5)

    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5
