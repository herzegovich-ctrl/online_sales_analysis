from product import Product
from product_manager import ProductManager
from cart import Cart
import random


def main():
    manager = ProductManager()

    manager.add_product(Product("Mlijeko 2L", 1.50, 5))
    manager.add_product(Product("Integralni Hljeb", 0.95, 15))
    manager.add_product(Product("Jaja 6kom", 1.80, 12))
    manager.add_product(Product("Maslac 250g", 3.00, 3))
    manager.add_product(Product("Sok 1L", 1.50, 8))
    manager.add_product(Product("Sir 200g", 4.20, 4))
    
    cart = Cart()

    available = manager.products
    sample_size = min(3, len(available))
    chosen = random.sample(available, sample_size)

    for prod in chosen:
        cart_item = Product(prod.name, prod.price, 1)
        cart.add_product(cart_item)

    print("Cart contents:")
    print(cart.show_cart())

    print(f"\nTotal due: {cart.total_due():.2f}")