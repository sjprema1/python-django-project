class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)
        print(self.items)

    def total(self) -> int:
        print(sum(item.price for item in self.items))
        print(item.name for item in self.items)

    def __len__(self):
        return len(self.items)

s = ShoppingCart()
i = Item("sugar",50)
i1 = Item("bella",70)
s.add(i)
s.add(i1)
s.total()