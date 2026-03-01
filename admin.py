from database import get_connection
from config import CATEGORIES
import utils


def run_admin_panel():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        utils.print_separator("ADMIN PANEL")
        print("1. Add New Item")
        print("2. Remove Item")
        print("3. Update Price")
        print("4. Update Category")
        print("5. Update Name")
        print("6. Update Stock")
        print("7. View All Items")
        print("8. View All Users")
        print("9. Exit Admin Panel")
        utils.print_separator()

        choice = utils.get_int_input("Select option: ", 1, 9)

        if choice == 1:
            _add_item(cursor, conn)
        elif choice == 2:
            _remove_item(cursor, conn)
        elif choice == 3:
            _update_price(cursor, conn)
        elif choice == 4:
            _update_category(cursor, conn)
        elif choice == 5:
            _update_name(cursor, conn)
        elif choice == 6:
            _update_stock(cursor, conn)
        elif choice == 7:
            _view_all_items(cursor)
        elif choice == 8:
            _view_all_users(cursor)
        elif choice == 9:
            break

    cursor.close()
    conn.close()


def _display_items(cursor):
    cursor.execute(
        "SELECT id, name, price, category, stock FROM items ORDER BY category, name"
    )
    rows = cursor.fetchall()
    if not rows:
        print("No items in catalog.")
        return False
    utils.print_table(rows, ["ID", "Name", "Price", "Category", "Stock"])
    return True


def _get_item(cursor, item_id):
    cursor.execute(
        "SELECT id, name, price, category, stock FROM items WHERE id = %s",
        (item_id,)
    )
    return cursor.fetchone()


def _add_item(cursor, conn):
    utils.print_separator("ADD ITEM")
    _display_items(cursor)

    name = utils.get_str_input("Item Name: ", max_length=100)
    price = utils.get_float_input("Price: ", min_val=0.01)

    print("Categories: " + ", ".join(CATEGORIES))
    while True:
        category = input("Category: ").strip().upper()
        if category in CATEGORIES:
            break
        print(f"Choose from: {', '.join(CATEGORIES)}")

    stock = utils.get_int_input("Initial Stock: ", min_val=1)

    cursor.execute(
        "INSERT INTO items (name, price, category, stock) VALUES (%s, %s, %s, %s)",
        (name, price, category, stock)
    )
    conn.commit()
    print(f"\nItem '{name}' added successfully.")
    _display_items(cursor)


def _remove_item(cursor, conn):
    utils.print_separator("REMOVE ITEM")
    if not _display_items(cursor):
        return

    item_id = utils.get_int_input("Enter Item ID to remove: ", min_val=1)
    item = _get_item(cursor, item_id)
    if not item:
        print("Item not found.")
        return

    confirm = input(f"Remove '{item[1]}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Operation cancelled.")
        return

    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    print(f"Item '{item[1]}' removed successfully.")
    _display_items(cursor)


def _update_price(cursor, conn):
    utils.print_separator("UPDATE PRICE")
    if not _display_items(cursor):
        return

    item_id = utils.get_int_input("Enter Item ID: ", min_val=1)
    item = _get_item(cursor, item_id)
    if not item:
        print("Item not found.")
        return

    new_price = utils.get_float_input(
        f"New price for '{item[1]}' (current: {item[2]}): ", min_val=0.01
    )
    cursor.execute("UPDATE items SET price = %s WHERE id = %s", (new_price, item_id))
    conn.commit()
    print("Price updated successfully.")
    _display_items(cursor)


def _update_category(cursor, conn):
    utils.print_separator("UPDATE CATEGORY")
    if not _display_items(cursor):
        return

    item_id = utils.get_int_input("Enter Item ID: ", min_val=1)
    item = _get_item(cursor, item_id)
    if not item:
        print("Item not found.")
        return

    print("Categories: " + ", ".join(CATEGORIES))
    while True:
        new_cat = input(f"New category for '{item[1]}' (current: {item[3]}): ").strip().upper()
        if new_cat in CATEGORIES:
            break
        print(f"Choose from: {', '.join(CATEGORIES)}")

    cursor.execute("UPDATE items SET category = %s WHERE id = %s", (new_cat, item_id))
    conn.commit()
    print("Category updated successfully.")
    _display_items(cursor)


def _update_name(cursor, conn):
    utils.print_separator("UPDATE NAME")
    if not _display_items(cursor):
        return

    item_id = utils.get_int_input("Enter Item ID: ", min_val=1)
    item = _get_item(cursor, item_id)
    if not item:
        print("Item not found.")
        return

    new_name = utils.get_str_input(f"New name for '{item[1]}': ", max_length=100)
    cursor.execute("UPDATE items SET name = %s WHERE id = %s", (new_name, item_id))
    conn.commit()
    print("Name updated successfully.")
    _display_items(cursor)


def _update_stock(cursor, conn):
    utils.print_separator("UPDATE STOCK")
    if not _display_items(cursor):
        return

    item_id = utils.get_int_input("Enter Item ID: ", min_val=1)
    item = _get_item(cursor, item_id)
    if not item:
        print("Item not found.")
        return

    new_stock = utils.get_int_input(
        f"New stock for '{item[1]}' (current: {item[4]}): ", min_val=0
    )
    cursor.execute("UPDATE items SET stock = %s WHERE id = %s", (new_stock, item_id))
    conn.commit()
    print("Stock updated successfully.")
    _display_items(cursor)


def _view_all_items(cursor):
    utils.print_separator("ALL ITEMS")
    _display_items(cursor)


def _view_all_users(cursor):
    utils.print_separator("ALL USERS")
    cursor.execute(
        "SELECT id, name, email, address, created_at FROM users ORDER BY created_at DESC"
    )
    rows = cursor.fetchall()
    if not rows:
        print("No registered users.")
        return
    utils.print_table(rows, ["ID", "Name", "Email", "Address", "Joined"])
