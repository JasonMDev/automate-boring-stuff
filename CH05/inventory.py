#! /usr/bin/python3
# inventory.py

# inventory dictionary
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):    
    # check if key are in the inventory and add if not
    for item in addedItems:
        if item not in inventory.keys():
            inventory[item] = 0

    # now count items and add to current inventory
    for k, v in inventory.items():
        inventory[k] += addedItems.count(str(k))

    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
print(inv)
displayInventory(stuff)
