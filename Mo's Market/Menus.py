import sys


border = "__________________________________________"
menu_options = "Main Menu: \n(1) Search for Items \n(2) View Shopping Cart \n(3) Proceed to Checkout \n(4) View Account Information \n(5) Quit"
account_select_options = "Welcome to Mo's Market:\n(1) Log In \n(2) Create Account"


def account_select():
    print(account_select_options)
    choice = int(input('Choice: '))
    print(border)
    match choice:
        case 1:
            log_in()
        case 2:
            create_account()
        case _:
            print("Invalid Choice. Try Again. ")
            account_select()

def log_in():
    pass

def create_account():
    pass


def main_menu():
    print(menu_options)
    choice = int(input("Choice: "))
    print(border)
    match choice:
        case 1:
            search_for_items()
        case 2:
            view_shopping_cart()
        case 3:
            proceed_to_checkout()
        case 4:
            view_shopping_cart()
        case 5:
            print("Thank you for shopping at Mo's Market.\nHave a great day!")
            sys.exit()
        case _:
            print("-> Invalid Choice. Please Try Again!")


def search_for_items():
    _item = input("Enter the name of an item: ")


def view_shopping_cart():
    pass

def proceed_to_checkout():
    pass

def view_account_information():
    pass