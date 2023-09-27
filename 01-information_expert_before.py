from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())

    def add_line_item(self, product: ProductDescription, quantity: int) -> None:
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5_000, description="Gaming headset")
    keyboard = ProductDescription(price=7_500, description="Mechanical gaming keyboard")

    row1 = SaleLineItem(product=headset, quantity=2)
    row2 = SaleLineItem(product=keyboard, quantity=3)

    sale = Sale([row1, row2])

    # Problem, how to get the total cost of the sale??

    total_cost = 0
    for item in sale.items:
        total_cost += item.product.price * item.quantity

    print(f"the total cost is: {total_cost}")


if __name__ == "__main__":
    main()
