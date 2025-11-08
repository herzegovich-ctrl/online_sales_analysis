from typing import List
from product import Product


class Cart:

    def __init__(self):
        self.cart_items: List[Product] = []

    def add_product(self, product: Product):
        self.cart_items.append(Product(product.name, product.price, product.quantity))

    def total_due(self) -> float:
        return sum(item.price * item.quantity for item in self.cart_items)

    def show_cart(self) -> str:
        if not self.cart_items:
            return "Cart is empty."
        lines = []
        for i, item in enumerate(self.cart_items, start=1):
            lines.append(f"{i}. {item.info()} | Line total: {item.price * item.quantity:.2f}")
        return "\n".join(lines)