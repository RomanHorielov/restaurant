"""This program, Restaurant_main.py, provides a solution for managing a restaurant's operations.
It includes classes for Menu, Order, and Invoice to handle core functionalities such as:
- Displaying the menu.
- Managing orders for tables.
- Generating invoices for completed orders.
"""
__author__ = "8256155, Nguyen"
__author__ = "8272265, Horielov"


from class_final3 import Menu
from class_final3 import Order
from class_final3 import Invoice
import pandas as pd
import os


def main():
    """
    Function to manage restaurant operations such as showing the menu,
    creating orders, displaying orders, generating invoices, and modifying orders.
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "food.csv")
    menu = Menu()
    menu.load_Menu(file_path)

    order_system = Order()
    invoice_system = Invoice()
    print("Geben Sie ein:\n 1: show Menu")
    print("2: Bestellung machen")
    print("3: Ueberblick der Bestellung")
    print("4: Rechnung erstellen")
    print("5: Bestellung löschen")
    print("6: Bestellung ändern")
    print("0: Beenden")

    while True:
        choose = int(input("Auswaehlen Funktion: "))
        print("Geben Sie ein:\n 1: show Menu")
        print("2: Bestellung machen")
        print("3: Ueberblick der Bestellung")
        print("4: Rechnung erstellen")
        print("5: Bestellung löschen")
        print("6: Bestellung ändern")
        print("0: Beenden")

        if choose == 0:
            # Exit the system
            break

        elif choose == 1:
            # Reload and display the menu
            menu.load_Menu(file_path)
            menu.show_Menu()

        elif choose == 2:
            # Create a new order for a specific table
            table_id = int(input("Welche Tisch bestellt jetzt?: "))
            if table_id not in order_system._all_orders:
                print("Tischnummer ungueltig! Bitte erneut versuchen.")
                continue

            while True:
                new_order = order_system.create_order(menu)
                if not new_order:
                    break  # User stopped creating orders
                # Add order to the list
                order_system.add_order(table_id, new_order)

        elif choose == 3:
            # Display all current orders
            order_system.display_orders()

        elif choose == 4:
            # Generate an invoice for a specific table
            id = int(input("Rechnung fuer welche Tisch: "))
            if id not in order_system._all_orders:
                print("Tischnummer ungueltig!")
                continue
            orders = order_system._all_orders[id]
            invoice_system.create_invoice(id=id, orders=orders, menu=menu)
            print(f"Rechnung fuer Tisch {id} ist erstellt")

        elif choose == 5:
            # Delete an order for a specific table
            table_id = int(
                input("Für welchen Tisch möchten Sie eine Bestellung löschen?: "))
            if table_id not in order_system._all_orders:
                print("Tischnummer ungueltig!")
                continue

            order_system.display_orders()  # Show all the orders
            order_index = int(
                input("Geben Sie die Nummer der zu löschenden Bestellung ein (0-basiert): "))
            order_system.delete_order(table_id, order_index)

        elif choose == 6:
            # Update an order for a specific table
            table_id = int(
                input("Für welchen Tisch möchten Sie eine Bestellung ändern?: "))
            if table_id not in order_system._all_orders:
                print("Tischnummer ungueltig!")
                continue

            order_system.display_orders()  # Show all the orders
            order_index = int(
                input("Geben Sie die Nummer der zu ändernden Bestellung ein (0-basiert): "))
            if 0 <= order_index < len(order_system._all_orders[table_id]):
                print("Bitte geben Sie die neuen Bestelldaten ein:")
                new_order = order_system.create_order(menu)
                if new_order:
                    order_system.update_order(table_id, order_index, new_order)
            else:
                print("Ungültiger Bestellindex! Bitte versuchen Sie es erneut.")


if __name__ == "__main__":
    main()
