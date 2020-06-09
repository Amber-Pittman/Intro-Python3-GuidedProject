"""
Task:
  - Create Dept Store Site Map using a terminal.
  - Talk to multiple stores to sell the products. Needs to be 
      usuable by more than one store.
"""

from category import Category

class Store:
  # attributes
    # name
    # categories (departments)

  # constructor - the function that runs everytime you create a new
      # instance
  def __init__(self, name, categories):
    # self refers to the current instance of the class (in JS the 
    # word is `this`)
    self.name = name 
    self.categories = categories
    #self.employees = []
      
  def __str__(self):
    # Stir will return a string representing the Store
    output = f"Welcome to {self.name}!"
    for category in self.categories:
      output += f"\n {category}"

    return output

  def __repr__(self):
    # also returns a string
    return f"self.name = {self.name}; self.categories = {self.categories}"

running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Braves Fans Only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The American kind", [])

sports_store = Store("The Dugout", ["Running", "Baseball", "Basketball"])
grocery_store = Store("Trader Joe's", ["Dairy", "Meat", "Poultry"])


print(running_category, "\n")
print(baseball_category, "\n")
print(basketball_category, "\n")
print(football_category, "\n")
print(sports_store, "\n")
print(grocery_store, "\n")