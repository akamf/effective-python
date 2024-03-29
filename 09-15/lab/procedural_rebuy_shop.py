from typing import Union, Dict, Optional

shop_inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
item_id: int = 0

def buy(computer: Dict[str, Union[str, int, bool]]) -> int:
    global item_id
    item_id = item_id + 1
    shop_inventory[item_id] = computer
    return item_id

def update_price(item_id: int, new_price: int) -> None :
    if item_id in shop_inventory:
        shop_inventory[item_id]['price'] = new_price
    else:
        print(f'Cannot update price for an item that does not exist')

def sell(item_id: int) -> None :
    del shop_inventory[item_id]
    
def print_item(item_id: int) -> None :
    if item_id in shop_inventory:
        print(f'Item with id {item_id} : {shop_inventory[item_id]}')
    else:
        print(f'Item with id {item_id} does not exist')

def refurbish(item_id: int, new_os : Optional[str] = None) -> None :
    if item_id in shop_inventory:
        
        computer = shop_inventory[item_id]
        
        if int(computer['made_in_year']) < 2000:
            computer['price'] = 0
        elif int(computer['made_in_year']) < 2010:
            computer['price'] = 250
        elif int(computer['made_in_year']) < 2018:
            computer['price'] = 650
        else:
            computer['price'] = 1000
        
        if new_os is not None:
            computer['os'] = new_os
    else:
        print('Cannot refurbish an item that does not exist')