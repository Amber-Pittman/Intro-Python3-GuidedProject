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
    # return a string representing the store
    output = f"Welcome to {self.name}!"
    i = 1 
    for category in self.categories:
        output += f'\n {i}. {category.name}'
        i += 1
    return output

  def __repr__(self):
    # also returns a string
    return f"self.name = {self.name}; self.categories = {self.categories}"

running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Braves Fans Only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The American kind", [])
soccer_category = Category("Soccer", "The real football", [])

# REPL = Read Evaluate Print Loop
sports_store = Store("The Dugout", [running_category, baseball_category, basketball_category, football_category, soccer_category])
choice = -1 # indexes start at 0, so if you type in 2, 
            # you'll get the first one on the list

print(sports_store)
print("Type q to quit")
while True:
  # Read
  choice = input("Please choose a category (#): ")
  # Loop
  try:
    # Evaluate
    if (choice == "q"):
      break
    choice = int(choice) - 1 
    if choice >= 0 and choice < len(sports_store.categories):
      chosen_category = sports_store.categories[choice]
    # Print
      print(chosen_category, "\n")
    else:
      print("The number is out of range.")
  except ValueError:
    print("Please enter a valid number.")