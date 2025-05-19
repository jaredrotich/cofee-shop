# import pytest
# from customer import Customer
# from coffee import Coffee
# from order import Order

# def test_customer_name_validation():
#     with pytest.raises(ValueError):
#         Customer("")  # Too short
#     with pytest.raises(ValueError):
#         Customer("ThisNameIsWayTooLong")  # Too long
#     with pytest.raises(ValueError):
#         Customer(123)  # Not a string

# def test_customer_orders_and_coffees():
#     Customer.all_customers.clear()
#     Order.all_orders.clear()

#     customer = Customer("Alice")
#     coffee1 = Coffee("Mocha")
#     coffee2 = Coffee("Latte")

#     o1 = customer.create_order(coffee1, 2.5)
#     o2 = customer.create_order(coffee2, 3.0)

#     assert len(customer.orders()) == 2
#     assert coffee1 in customer.coffees()
#     assert coffee2 in customer.coffees()

# def test_most_aficionado():
#     Customer.all_customers.clear()
#     Order.all_orders.clear()

#     c1 = Customer("Marto")
#     c2 = Customer("Shiro")
#     coffee = Coffee("Espresso")

#     c1.create_order(coffee, 3.0)
#     c1.create_order(coffee, 4.0)
#     c2.create_order(coffee, 5.0)

#     assert Customer.most_aficionado(coffee) == c1
