# import pytest
# from customer import Customer
# from coffee import Coffee
# from order import Order

# def test_coffee_name_validation():
#     with pytest.raises(ValueError):
#         Coffee("A")  # Too short
#     with pytest.raises(ValueError):
#         Coffee(123)  # Not a string

# def test_coffee_orders_and_customers():
#     Coffee.all_coffees.clear()
#     Order.all_orders.clear()
#     Customer.all_customers.clear()

#     coffee = Coffee("Latte")
#     c1 = Customer("Ali")
#     c2 = Customer("Betty")

#     c1.create_order(coffee, 3.0)
#     c2.create_order(coffee, 3.5)

#     assert len(coffee.orders()) == 2
#     assert c1 in coffee.customers()
#     assert c2 in coffee.customers()

# def test_num_orders_and_average_price():
#     Coffee.all_coffees.clear()
#     Order.all_orders.clear()
#     Customer.all_customers.clear()

#     coffee = Coffee("Cappuccino")
#     c1 = Customer("Jay")

#     c1.create_order(coffee, 4.0)
#     c1.create_order(coffee, 6.0)

#     assert coffee.num_orders() == 2
#     assert coffee.average_price() == 5.0
