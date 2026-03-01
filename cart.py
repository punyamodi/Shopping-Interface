from database import get_connection
import utils


def add_item_to_cart(user_email, item_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, price, stock FROM items WHERE id = %s",
        (item_id,)
    )
    item = cursor.fetchone()
    if not item:
        print("Item not found.")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "SELECT quantity FROM cart WHERE user_email = %s AND item_id = %s",
        (user_email, item_id)
    )
    existing = cursor.fetchone()
    current_in_cart = existing[0] if existing else 0
    total_requested = current_in_cart + quantity

    if total_requested > item[3]:
        available = item[3] - current_in_cart
        print(f"Insufficient stock. You can add at most {available} more unit(s).")
        cursor.close()
        conn.close()
        return

    if existing:
        cursor.execute(
            "UPDATE cart SET quantity = %s WHERE user_email = %s AND item_id = %s",
            (total_requested, user_email, item_id)
        )
    else:
        cursor.execute(
            "INSERT INTO cart (user_email, item_id, quantity) VALUES (%s, %s, %s)",
            (user_email, item_id, quantity)
        )

    conn.commit()
    cursor.close()
    conn.close()
    print(f"'{item[1]}' added to cart (qty: {total_requested}).")


def view_cart(user_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.item_id, i.name, i.price, c.quantity, i.price * c.quantity AS total
        FROM cart c
        JOIN items i ON c.item_id = i.id
        WHERE c.user_email = %s
        ORDER BY i.name
    """, (user_email,))
    rows = cursor.fetchall()

    utils.print_separator("YOUR CART")
    if not rows:
        print("Your cart is empty.")
        cursor.close()
        conn.close()
        return [], 0

    utils.print_table(rows, ["Item ID", "Name", "Unit Price", "Quantity", "Total"])
    grand_total = sum(float(row[4]) for row in rows)
    print(f"\nGrand Total: {grand_total:.2f}")

    cursor.close()
    conn.close()
    return rows, grand_total


def remove_from_cart(user_email, item_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT quantity FROM cart WHERE user_email = %s AND item_id = %s",
        (user_email, item_id)
    )
    row = cursor.fetchone()
    if not row:
        print("Item not found in cart.")
        cursor.close()
        conn.close()
        return

    current_qty = row[0]
    if quantity >= current_qty:
        cursor.execute(
            "DELETE FROM cart WHERE user_email = %s AND item_id = %s",
            (user_email, item_id)
        )
        print("Item removed from cart.")
    else:
        new_qty = current_qty - quantity
        cursor.execute(
            "UPDATE cart SET quantity = %s WHERE user_email = %s AND item_id = %s",
            (new_qty, user_email, item_id)
        )
        print(f"Quantity updated to {new_qty}.")

    conn.commit()
    cursor.close()
    conn.close()


def checkout(user_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.item_id, i.name, i.price, c.quantity, i.price * c.quantity AS total
        FROM cart c
        JOIN items i ON c.item_id = i.id
        WHERE c.user_email = %s
    """, (user_email,))
    items = cursor.fetchall()

    if not items:
        print("Your cart is empty. Add items before checking out.")
        cursor.close()
        conn.close()
        return

    utils.print_separator("ORDER SUMMARY")
    utils.print_table(items, ["Item ID", "Name", "Unit Price", "Quantity", "Total"])
    grand_total = sum(float(item[4]) for item in items)
    print(f"\nGrand Total: {grand_total:.2f}")

    confirm = input("\nConfirm order? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Order cancelled.")
        cursor.close()
        conn.close()
        return

    for item in items:
        item_id, name, price, quantity, total = item
        cursor.execute("""
            INSERT INTO orders (user_email, item_id, item_name, unit_price, quantity, total_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user_email, item_id, name, price, quantity, total))
        cursor.execute(
            "UPDATE items SET stock = stock - %s WHERE id = %s",
            (quantity, item_id)
        )

    cursor.execute("DELETE FROM cart WHERE user_email = %s", (user_email,))
    conn.commit()
    cursor.close()
    conn.close()
    print("\nOrder placed successfully. Thank you for shopping!")


def view_order_history(user_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, item_name, unit_price, quantity, total_price, ordered_at
        FROM orders
        WHERE user_email = %s
        ORDER BY ordered_at DESC
    """, (user_email,))
    rows = cursor.fetchall()

    utils.print_separator("ORDER HISTORY")
    if not rows:
        print("No orders found.")
        cursor.close()
        conn.close()
        return

    utils.print_table(rows, ["Order ID", "Item", "Unit Price", "Qty", "Total", "Ordered At"])
    total_spent = sum(float(row[4]) for row in rows)
    print(f"\nLifetime Spend: {total_spent:.2f}")

    cursor.close()
    conn.close()
