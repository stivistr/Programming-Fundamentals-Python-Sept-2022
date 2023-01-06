class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.space = self.__capacity

    def add_item(self, item: str):
        if self.space > 0:
            self.items.append(item)
            self.space -= 1
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.space}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
