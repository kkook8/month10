from dataclasses import dataclass


@dataclass  # デコレーター decorater
class Product:
    code: str
    name: str
    price: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("商品価格は０以上です")


@dataclass(frozen=True)
class CartItem:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("商品数量は０以上です")

    def subtotal(self):
        return self.product.price*self.quantity
