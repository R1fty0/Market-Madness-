class Item:
    def __init__(self, name, cost, description):
        """ Creates a new item that a user can interact with. """
        self.name = name
        self.cost = cost
        self.description = description

    def get_item_attribute(self, attribute):
        """ Returns one of the item's attributes. """
        match attribute.upper():
            case 'NAME':
                return self.name
            case 'COST':
                return self.cost
            case 'DESCRIPTION':
                return self.description


class Inventory:
    def __init__(self, name) -> None:
        self.inventory = dict()
        self.name = name

    def get_item(self, item: Item) -> Item:
        """ Gets the requested item from the inventory. """
        for name in self.inventory.keys():
            if name == item.name:
                return self.inventory[name]

    def update_item(self, item: Item, remove=False):
        """ Removes or adds an item to the inventory. """
        try:
            if remove:
                self.inventory.pop(item.name)
            else:
                self.inventory.update({item.name: item})
        except AttributeError:
            return

    def show_item_details(self, item):
        if self.get_item(item) is not None:
            print(f'{item.name}: \n - Cost: ${item.cost} \n - Description: {item.description}')


class Stock:
    def __init__(self) -> None:
        """ Creates a stockpile of goods that the user can buy. """
        self.stock = dict()

    def get_inventory(self, inventory):
        """ Gets the requested inventory. """
        for name in self.stock.keys():
            if name == inventory.name:
                return self.stock[name]
            break

    def update_stock(self, inventory: Inventory, add_inventory=False):
        """ Removes or adds an inventory to the stock. """
        if add_inventory:
            self.stock.update({inventory.name: inventory})
        else:
            self.stock.pop(inventory.name)