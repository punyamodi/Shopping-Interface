import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "shopping_cart")

CATEGORIES = ["ELECTRONICS", "GROCERY", "TOYS", "CLOTHING"]

ADMIN_EMAIL = "admin@admin.com"
ADMIN_PASSWORD = "admin123"
