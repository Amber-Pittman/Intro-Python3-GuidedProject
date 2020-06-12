# Parent Class OR Base Class 
# Sometimes, it can be referred to as Superclass - super links to 
#   whatever is written inside the parens of the child class

# class Product:
#     def __init__(self, name, price):
#       self.name = name
#       self.price = price
#       self.discount = 0 #discount
# You could also put self.discount = discount if you set the value 
#   and the param inside the init function
# Example:
class Product:
  def __init__(self, name, price, discount = 0): 
    self.name = name
    self.price = price
    self.discount = discount

  def __str__(self):
    return f"{self.name}: ${self.price} Great Deal!"

# Child Class OR Subclass
# The children classes of the parent class are referred to as Sibling classes
class Sneaker(Product):
  def __init__(self, name, price, shoe_size, brand, color):
    
    super().__init__(name, price, 0)
    self.shoe_size = shoe_size
    self.brand = brand
    self.color = color

  def __str__(self):
    # If you didn't want to use the parent's stir function, you just wouldn't call it at all.
    parent_str = super().__str__()
    return f"{parent_str}"

# class SoccerBall(Product):
#   def __init__(self, name, price, material):
#     super().__init__(name, price)
#     self.material = material

# Instead of creating another instance to get the new discount value, you can add it in the
#   super inti function in numerical form and remove the soccer_ball instance below.
class SoccerBall(Product):
  def __init__(self, name, price, material):
    super().__init__(name, price, 10)
    self.material = material

  def __str__(self):
    # If you didn't want to use the parent's stir function, you just wouldn't call it at all.
    #parent_str = super().__str__()
    #return f"{parent_str} WILSOOOOOOOOONNNNN!!!"
    return f"{self.name}: ${self.price} WILSOOOOOOOOONNNNN!!!"

  def kick(self):
    print("The ball flew away!")

#instances
nike_free = Sneaker("Nike Free", "100", "10", "Nike", "Lime Green")
soccer_ball = SoccerBall("Wilson", "15", "Leather")
#soccer_ball.discount = 10
generic_product = Product("Generic Thing", "2.49")


print(nike_free.name)
print(nike_free.price)
print(nike_free.shoe_size)
print(nike_free.brand)
print(nike_free.color)
print(nike_free.discount)
print(soccer_ball.discount)
print(generic_product)
print(nike_free)
print(soccer_ball)
soccer_ball.kick() #yes, this will print.
