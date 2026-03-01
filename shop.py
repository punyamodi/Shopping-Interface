from database import get_connection
from config import CATEGORIES
import cart as cart_module
import utils


def run_shop(user_email):
    while True:
        utils.print_separator("SHOP")
        print("1. Browse by Category")
        print("2. Search Items")
        print("3. View All Items")
        print("4. View Cart")
        print("5. Manage Cart")
        print("6. Checkout")
        print("7. Order History")
        print("8. Back to Main Menu")
        utils.print_separator()

        choice = utils.get_int_input("Select option: ", 1, 8)

        if choice == 1:
            _browse_by_category(user_email)
        elif choice == 2:
            _search_items(user_email)
        elif choice == 3:
            _display_and_add(user_email)
        elif choice == 4:
            cart_module.view_cart(user_email)
        elif choice == 5:
            _manage_cart(user_email)
        elif choice == 6:
            cart_module.checkout(user_email)
        elif choice == 7:
            cart_module.view_order_history(user_email)
        elif choice == 8:
            break


def _browse_by_category(user_email):
    utils.print_separator("BROWSE BY CATEGORY")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    print(f"{len(CATEGORIES) + 1}. Back")

    choice = utils.get_int_input("Select category: ", 1, len(CATEGORIES) + 1)
    if choice == len(CATEGORIES) + 1:
        return

    category = CATEGORIES[choice - 1]
    _display_and_add(user_email, category=category)


def _search_items(user_email):
    query = utils.get_str_input("Search for: ")
    _display_and_add(user_email, search=query)


def _display_and_add(user_email, category=None, search=None):
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute(
            "SELECT id, name, price, category, stock FROM items WHERE category = %s AND stock > 0 ORDER BY name",
            (category,)
        )
        title = f"ITEMS  {category}"
    elif search:
        cursor.execute(
            "SELECT id, name, price, category, stock FROM items WHERE name LIKE %s AND stock > 0 ORDER BY name",
            (f"%{search}%",)
        )
        title = f"RESULTS FOR '{search.upper()}'"
    else:
        cursor.execute(
            "SELECT id, name, price, category, stock FROM items WHERE stock > 0 ORDER BY category, name"
        )
        title = "ALL ITEMS"

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    utils.print_separator(title)
    if not rows:
        print("No items found.")
        return

    utils.print_table(rows, ["ID", "Name", "Price", "Category", "Stock"])

    choice = input("\nEnter Item ID to add to cart (or press Enter to go back): ").strip()
    if not choice:
        return

    try:
        item_id = int(choice)
    except ValueError:
        print("Invalid item ID.")
        return

    item_ids = [row[0] for row in rows]
    if item_id not in item_ids:
        print("Item ID not in current list.")
        return

    quantity = utils.get_int_input("Quantity: ", min_val=1)
    cart_module.add_item_to_cart(user_email, item_id, quantity)


def _manage_cart(user_email):
    rows, grand_total = cart_module.view_cart(user_email)
    if not rows:
        return

    print("\n1. Remove Item from Cart")
    print("2. Back")

    choice = utils.get_int_input("Select option: ", 1, 2)
    if choice == 2:
        return

    item_id = utils.get_int_input("Enter Item ID to modify: ", min_val=1)
    cart_ids = [row[0] for row in rows]
    if item_id not in cart_ids:
        print("Item not found in cart.")
        return

    current_qty = next(row[3] for row in rows if row[0] == item_id)
    print(f"Current quantity: {current_qty}")
    qty_to_remove = utils.get_int_input(
        f"Quantity to remove (1-{current_qty}): ", min_val=1, max_val=current_qty
    )
    cart_module.remove_from_cart(user_email, item_id, qty_to_remove)
