import Inventory
import Menus

stock = Inventory.Stock()
fruits_inventory = Inventory.Inventory("Fruits")
apple = Inventory.Item("Apple", 0.5, "A delicious fruit.")
stock.update_stock(fruits_inventory, True)
fruits_inventory.update_item(apple)



if __name__ == "__main__":
    Menus.account_select()