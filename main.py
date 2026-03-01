import sys

import mysql.connector

import database
import auth
import admin
import shop
import utils


def main():
    utils.print_separator("SHOPPING CART")
    try:
        database.initialize()
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        print("Check your credentials in the .env file.")
        sys.exit(1)

    while True:
        utils.print_separator("MAIN MENU")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        utils.print_separator()

        choice = utils.get_int_input("Select option: ", 1, 3)

        if choice == 3:
            print("\nThank you for visiting. Goodbye.")
            break

        elif choice == 1:
            try:
                user = auth.login()
                if user == "admin":
                    admin.run_admin_panel()
                else:
                    shop.run_shop(user)
            except KeyboardInterrupt:
                print("\nReturning to main menu.")

        elif choice == 2:
            try:
                auth.signup()
            except KeyboardInterrupt:
                print("\nReturning to main menu.")


if __name__ == "__main__":
    main()
