from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    manager.add_product(Product("Mlijeko 1L", 1.20, 10))
    manager.add_product(Product("Hljeb", 0.80, 20))
    manager.add_product(Product("Jaja 10kom", 2.50, 5))
    manager.add_product(Product("Maslac 250g", 3.00, 3))

    manager.add_product(Product("hljeb", 0.85, 5))

    print("Products:")
    print(manager.show_products())

    total = manager.total_inventory_value()
    print(f"\nTotal inventory value: {total:.2f}")


if __name__ == "__main__":
    main()