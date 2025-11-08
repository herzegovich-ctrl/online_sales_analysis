from typing import List
from product import Product


class ProductManager:

    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        for p in self.products:
            if p.name.lower() == product.name.lower():
                p.price = product.price
                p.quantity += product.quantity
                return
        self.products.append(product)

    def show_products(self) -> str:
        if not self.products:
            return "No products available."
        lines = [p.info() for p in self.products]
        return "\n".join(lines)

    def total_inventory_value(self) -> float:
        return sum(p.total_value() for p in self.products)