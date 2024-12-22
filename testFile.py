"""Programm testFile.py helps to test three main classes (Menu, Order, and Invoice)
to manage the operations of a restaurant.
"""
__author__ = "8256155, Nguyen"
__author__ = "8272265, Horielov"

from class_final3 import Menu, Order, Invoice


# Testfälle für display_orders
print("Testfälle für display_orders")
# Fall 1
print("\nFall 1:")
order_system = Order()
order_system.all_orders = {
    1: [{"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}]
}
order_system.display_orders()

# Fall 2
print("\nFall 2:")
order_system = Order()
order_system.all_orders = {1: [], 2: [], 3: [], 4: [], 5: []}
order_system.display_orders()

# Testfälle für create_order
print("\nTestfälle für create_order")
# Fall 1
print("\nFall 1:")
menu = Menu()
menu.menu = {
    1: {"name": "Pizza", "price": 10}
}
order_system = Order()
# Simuliert Benutzerinteraktionen: ID, Anzahl, Extra-Wunsch
print("Bitte folgende Eingaben simulieren: 1, 2, 1 (Extra Käse), 1")
order = order_system.create_order(menu)
print(f"Erstellte Bestellung: {order}")

# Fall 2
print("\nFall 2:")
print("Keine Bestellung erstellt: None")

# Fall 3
print("\nFall 3:")
print("Ungültige ID! Bitte versuchen Sie es erneut.")

# Testfälle für delete_order
print("\nTestfälle für delete_order")
# Fall 1
print("\nFall 1:")
order_system = Order()
order_system.all_orders = {
    1: [{"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}]
}
order_system.delete_order(1, 0)  # Bestellung wird entfernt
order_system.display_orders()

# Fall 2
print("\nFall 2:")
order_system = Order()
order_system.all_orders = {
    1: [{"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}]
}
order_system.delete_order(1, 5)  # Ungültiger Bestellindex

# Testfälle für update_order
print("\nTestfälle für update_order")
# Fall 1
print("\nFall 1:")
order_system = Order()
order_system.all_orders = {2: [
    {"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}]}
order_system.update_order(2, 0, {"productname": "Salat", "quantity": 1})
order_system.display_orders()

# Fall 2
print("\nFall 2:")
order_system = Order()
order_system.all_orders = {2: [
    {"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}]}
order_system.update_order(2, 5, {"productname": "Salat", "quantity": 1})

# Testfälle für Invoice
print("\nTestfälle für Invoice")
invoice_system = Invoice()
menu = Menu()
menu.menu = {1: {"name": "Pizza", "price": 10}}

# Fall 1
print("\nFall 1:")
invoice_system.create_invoice(
    1, [{"productname": "Pizza", "quantity": 2, "request": "Keine", "request_quantity": 0}], menu)

# Fall 2
print("\nFall 2:")
invoice_system.create_invoice(1, [], menu)  # Leere Rechnung

# Fall 3
print("\nFall 3:")
invoice_system.create_invoice(
    1, [{"productname": "Salat", "quantity": 1, "request": "Keine", "request_quantity": 0}], menu)
