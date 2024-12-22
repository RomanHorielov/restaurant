"""Programm Restaurant_class.py helps defines three main classes (Menu, Order, and Invoice)
to manage the operations of a restaurant. These classes provide functionalities
to handle menu management, order processing, and invoice generation.
"""
__author__ = "8256155, Nguyen"
__author__ = "8272265, Horielov"


import pandas as pd
import os


class Menu:
    """
    Class to manage menu items for a restaurant.

    Attributes:
        menu (dict): Dictionary containing menu items with IDs as keys.
    """

    def __init__(self):
        """Initialize an empty menu."""
        self._menu = {}

    def load_Menu(self, file_path):
        """
        Load the menu from a CSV file.

        Args:
            file_path (str): Path to the CSV file containing menu data.

        Raises:
            FileNotFoundError: If the file is not found.
            Exception: For other errors during file reading.
        """
        try:
            menu_data = pd.read_csv(file_path)
            # Create Menu with ID as key in dictionaries
            self._menu = {
                row['ID']: {
                    'name': row['name'],
                    'price': row['price']
                }
                for _, row in menu_data.iterrows()
            }
            print("Menu wurde erfolgreich geladen!")
        except FileNotFoundError:
            print(f"File '{file_path}' nicht gefunden!")
        except Exception as e:
            print(f"Fehler beim Lesen der Datei: {e}")

    def show_Menu(self):
        """
        Display the menu in a formatted way.

        Prints:
            A list of menu items with their IDs, names, and prices.
        """
        print("____Menu____")
        for menu_id, item in self._menu.items():
            print(
                f"ID: {menu_id} - Name: {item['name']} - Price: {item['price']} EUR")

    def get_menu_item_by_id(self, menu_id):
        """
        Get a menu item by its ID.

        Args:
            menu_id (int): The ID of the menu item.

        Returns:
            dict: Menu item details if found, else None.
        """
        return self._menu.get(menu_id, None)


class Order:
    """
    Class to manage orders for a restaurant.

    Attributes:
        all_orders (dict): Dictionary containing orders grouped by table IDs.
    """

    def __init__(self):
        """Initialize orders for 5 tables."""
        self._all_orders = {1: [], 2: [], 3: [], 4: [], 5: []}

    def add_order(self, table_id, order):
        """
        Add an order to a specific table.

        Args:
            table_id (int): ID of the table.
            order (dict): Details of the order.
        """
        if table_id in self._all_orders:
            self._all_orders[table_id].append(order)
        else:
            print("Tisch Nummer ist ungueltig")

    def display_orders(self):
        """
        Display all orders for all tables.

        Prints:
            Orders grouped by table IDs.
        """
        print("Alle Bestellungen")
        for table_id, table_orders in self._all_orders.items():
            print(f"Tisch {table_id}:")
            for oder in table_orders:
                print(f"Produkt: {oder['productname']} Anzahl: {oder['quantity']} - Sonderwunsch: {
                      oder['request']} - Anzahl der Sonderwunsch: {oder['request_quantity']}")

    def create_order(self, menu):
        """
        Create a new order by interacting with the user.

        Args:
            menu (Menu): Menu instance for accessing menu items.

        Returns:
            dict: The created order details or None if creation is canceled.
        """
        menu.show_Menu()  # Show Menu
        menu_id = int(
            input("Geben Sie die ID des Produkts ein (oder 0 zum Beenden): "))
        if menu_id == 0:
            return None  # User stopped create Order

        # Product information from menu
        menu_item = menu.get_menu_item_by_id(menu_id)
        if not menu_item:
            print("Ungültige ID! Bitte versuchen Sie es erneut.")
            return None

        # Get Order from the guest
        quantity = int(input("Anzahl der Produkte: "))
        request = int(input("1 fur Extra und 0 fur Normal oder Ausschluss: "))
        if request == 1:
            request_details = input("Geben die Sonderwunsch ein: ")
            request_quantity = int(
                input("Geben die Anzahl der Sonderwunsch ein: "))
        else:
            request_details = input("Geben die Sonderwunsch ein: ")
            request_quantity = 0

        # Create order as dictionary
        return {
            "productname": menu_item["name"],
            "quantity": quantity,
            "price": menu_item["price"],
            "request": request_details,
            "request_quantity": request_quantity
        }

    def delete_order(self, table_id, order_index):
        """
        Delete an order by index for a specific table.

        Args:
            table_id (int): The table ID.
            order_index (int): The index of the order to delete.
        """
        if table_id in self._all_orders:
            if 0 <= order_index < len(self._all_orders[table_id]):
                removed_order = self._all_orders[table_id].pop(order_index)
                print(f"Bestellung wurde entfernt: {removed_order}")
            else:
                print(
                    f"Ungültiger Bestellindex! Bitte wählen Sie eine gültige Bestellung aus.")
        else:
            print("Tisch Nummer ist ungueltig!")

    def update_order(self, table_id, order_index, new_order):
        """
        Update an existing order for a specific table.

        Args:
            table_id (int): The table ID.
            order_index (int): The index of the order to update.
            new_order (dict): The new order details.
        """
        if table_id in self._all_orders:
            if 0 <= order_index < len(self._all_orders[table_id]):
                self._all_orders[table_id][order_index] = new_order
                print("Bestellung wurde erfolgreich aktualisiert!")
            else:
                print(
                    f"Ungültiger Bestellindex! Bitte wählen Sie eine gültige Bestellung aus.")
        else:
            print("Tisch Nummer ist ungueltig!")


class Invoice:
    """
    Class to create invoices for a restaurant.

    Methods:
        create_invoice(id, orders, menu): Create an invoice file for a specific table.
    """

    def create_invoice(self, id, orders, menu):
        """
        Create an invoice for a table and save it to a file.

        Args:
            id (int): Table ID.
            orders (list): List of orders for the table.
            menu (Menu): Menu instance for price lookup.
        """
        total_bill = 0
        file_name = f"Invoice table{id}.txt"
        with open(file_name, "w") as file:
            file.write(f"Rechnung: Tisch {id}\n")
            file.write(f"{'-'*50}\n")
            file.write(f"\n{'Produkt': <15}{'Anzahl':<10}{'Preis': <10}{
                       'Sonderwunsch':<20}{'Anzahl':<20} {'EUR':30}\n")
            for i in orders:
                productname = i["productname"]
                quantity = i["quantity"]
                request_details = i["request"]
                request_quantity = i["request_quantity"]

                # Get the price as productname
                price = None
                for menu_id, menu_item in menu._menu.items():
                    if menu_item["name"] == productname:
                        price = menu_item["price"]
                        break

                if price is None:
                    print(f"Die Preis fuer {
                          productname} kann nicht im Menu finden!")
                    continue
                total_product = quantity * price + request_quantity
                total_bill += total_product
                file.write(f"\n{productname:<15} {quantity:<10} {price:<10} {
                           request_details:<20} {request_quantity:<20} {total_product:5} \n")
            # Calculate total bill
            file.write(f"{'-'*50}\n")
            file.write(f"Total: {total_bill:20}")
