class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price must be non-negative")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def info(self) -> str:
        return f"Name: {self.name} | Price: {self.price:.2f} | Quantity: {self.quantity}"

    def update_quantity(self, new_quantity: int):
        if new_quantity < 0:
            raise ValueError("Quantity must be non-negative")
        self.quantity = int(new_quantity)

    def total_value(self) -> float:
        return self.price * self.quantity

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price:.2f}, quantity={self.quantity})"