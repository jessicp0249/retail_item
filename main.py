# File: main.py
# Description: Program will print out a table of retail items.
# Author: Jessica Priester
# Email: jessicp0249@student.vvc.edu
# Created: 30 October 2019

# Class stores information about a retail item.
class RetailItem:
  def __init__(self, descript="none", units=0, price=0.0):
    self.descript = descript # Description
    self.units = units # Uints in inventory
    self.price = price # Price per unit

# Create list of RetailItem objects
items = [
  RetailItem("Jacket", 12, 	59.95),
  RetailItem("Designer Jeans", 40, 34.95),
  RetailItem("Shirt", 20, 24.95)
]

# Print table headings
print("%-10s%-15s%-20s%-5s" % ("Item", "Description", "Units in Inventory", "Price"))

# Print each info for each item in list
for i in range(len(items)):
  item_col = "Item #" + str(i+1)
  unit_col = str(items[i].units)
  print("%-10s%-15s%-20s%0.2f" % (item_col, items[i].descript, unit_col, items[i].price))
