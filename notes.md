## Inheritance

Right now, our Store only has a set of categories. A store needs to actually have something to sell. Categories help us go to places where there are items we might want to buy but we don't really have any products yet. 

Let's add some products to our categories. Here's where we might start seeing a couple of issues when we actually want to start creating a product class. 

Taking a sports store as an example, what kind of products might we actually sell at a sports store?
  * Sneakers
  * Soccer balls
  * Weights
  * Bike

So you might notice that all those products kind of have very different attributes to them. When we're buying a soccer ball, there are things we might want to consider but when we're buying sneakers there are completely different sets of things we might want to consider. But if we're creating a class called `Product`, what attributes might we want to have in a product class that kind of fit all four of these pretty different items?
  * Name
  * Price

  ```
  class Product:
    name
    price
  ```

We're kind of at this point where the name and price attributes is pretty much all that really, actually is common between the products. Now, if a person wants to learn about sneakers they want the name and the price but they may also want shoe size. People looking at bikes may want to know about frame size. If you're looking at weights, you probably want to know how heavy they are.

Imagine if we were trying to actually create an instance of a product for a sneaker, we would have a name, a price, and a shoe size. But what do we do with the frame size and the weight attributes? Nothing. There's no such thing as a frame size - weight is _maybe_ important but arguably not something that you are checking at the store. 

The point is now, if we want to make a class that fits a lot of different items (_instances_), we are going to end up with a lot of attributes that probably aren't going to be related to all different cases. Instead, we should use **inheritance** to create different, more-specific products that we  can use to create the actual instances. 

Like we determined earlier, name and price are important. Shoe size, frame size, and weight are not going to be important for everything. So what if instead we create another class that took all the information that Product has and then optionally added in a few more parameters that just make sense for it? 

Imagine we created a Sneaker class. We're going to inherit from the Product class. We're going to essentially say a sneaker is a product but it has a few more features to it. So it's a product that inherits from the Product, but it here has shoe size, the brand of the shoe, and color of the shoe.

Now, if we wanted to create a running shoe, we don't have to create a product and try to cram all of the different attributes in it. We can create a sneaker that inherits from the class Product, so it actually has name and price already in it from the Product class but it also has a few other attributes added to it. 

What we've done is create a class called Sneaker which takes in the Product attributes. Inheritance allows our Sneaker class to have everything that Product does, with more of it's on specific attributes added to it. We get Product's attributes for free but we get to add a few more attributes that we might care about. 

  ```
  class Product:
    name
    price

  class Sneaker(Product):
    shoe_size
    brand
    color
  ```

Like Sneakers, we could do the same with soccer balls, too. We can add in more attributes that only matter for soccer balls but do not matter for shoes. 

In the Soccer_Ball class, we'll have name and price from the product, but then add a size for soccer balls that come in S, M, or L. Meaning it can't be confused with shoe size metrics.

Now if we determine that we want to add something to all products, let's say all products should also have a sale percentage sometimes. We would add an attribute to sale_percent for Product. Obviously, because the Sneaker and the Soccer_Ball classes inherit from Product, they would also get that sale_percent attribute "for free."

In other words, if Association is "one class has another class," the way Inheritance works is Sneaker _is a_ Product. That's the key distinction in this case. So a sneaker doesn't have products in it; however, it is a product. So when you can identify that one class _is a_ base class and the other class is associated with it, that is how Inheritance happens. 

  ```
  class Product:
    name
    price
    sale_percent

  class Sneaker(Product):
    shoe_size
    brand
    color

  class Soccer_Ball(Product):
    size
  ```

## Code Along

Since we've established these relationships, let's actually implement them in our app. There is a way in Python to specify that one class inherits from some other class base class. Just go ahead and copy the example code above and place it in a new file, `product.py`. 

First, start off with defining an init function. We decided that the two params are name and price. Everything will look pretty simple, with self.name is name and self.price is price. 

For good measure, let's come up with a stir function in case we ever want to print a product itself. We'll just have it return self.name and self.price.

The problem with putting the individual items into the Product class is that every single product must have a value for shoe_size, even if you're shopping for soccer balls and has nothing to do with shoe_size. Clearly, that is not the most appropriate place for that attribute. 

Instead of cramming those individual products into the Product class, we'll move it to it's own individual class. In the Sneaker class, we're going to open up our parentheses and we're going to write Product in there. At this point, we've indicated that Sneaker inherits from a class called Product and now, Sneaker is a product. Meaning, we can now actually have name and price be managed by the Product class and any parameters that we care about for a sneaker itself, we add into the Sneaker class and _only_ that class. 

We will still have our init function in the Sneaker class. We need to consider that a sneaker will still have a name and a price. But we determined there are a couple more parameters it should have. It should have a shoe size, a brand, and a color. You will need to add name and price inside the init function as well as Sneaker's personal attributes. 

Side note, the order of the params inside of init in the child class do _not_ matter because these are named params and as long as you remember to assign the values to match the order of the params in the init function, it will be fine. However, it _does_ matter in the super() function because the first constructor for the Product class is, in fact, name and then price.

Now we can do self.shoe_size, self.brand, and self.color. However, instead of writing self.name and self.price, we can use a function that all classes have - super(). The super function will pull in the parent class' attributes - it gives us access to the parent instance of our class. It's kind of like doing self except it's doing it for the parent self, not the child self. Super can be used inside classes to refer to the parent class - that's really the only way it is used.

Still dealing with super(), we can call the parent's init function. Then, inside the parent init function on super, pass in the parent's parameters. In this case, it's name and price. Doing that, we don't have to worry about having self.name or self.price inside the Sneaker class.

Super is not necessarily calling the Parent constructor, because technically, the whole line of `super().__init__(...)` is calling the parent constructor. 

To prove that super() works, let's create an _instance_ of a sneaker and print it out to see what kind of attrs that sneaker will have. We'll call it `nike_free`. Now, instead of creating a product, we'll create a Sneaker saying that it is a Nike Free. Then create a string for the dollar amount to represent the price, with the size of 10, and the brand is Nike. Create a color for it as well. 

Note how we haven't actually wrote self.name and self.price. If we wanted to, we could print `nike_free.name`,`nike_free.price`, `nike_free.brand`, and `nike_free.color`. So 2 params that are a part of the Product class and the other params are part of the Sneaker class. If you run the program, you will see that we are going to get all the attrs for the Nike Free sneaker from the Sneaker class.

Now let's create another class that has absolutely nothing to do with Sneaker. The SoccerBall class will have name and price pulling in from Product. We'll add another attr, material. Now we need to use super once again to actually get the Product attrs. Then, we'll add the material parameter using self.

Let's create an instance of Soccer_Ball. In the instance, we will add a name, price, and the material. Now we can see we have two completely separate products - one is a Sneaker, one is a Soccer Ball - but we can print the Nike Free price and the Soccer Ball price. Both of those attrs will be there. 

Now, if we wanted to add one more param to all the products, we can add it to the Product class then update Sneaker and Soccer Ball to include that new param. We'll use discount as stores often have sales going on. Without adding the discount parameter into the init function of Product, you can declare self.discount and give it a value of 0 since the sale isn't ongoing. On top of that, you don't need to declare the discount variable in the init functions of Sneaker nor SoccerBall. 

You can then create an instance of discount on soccer_ball and assign it a new value. Print out the soccer_ball.discount. You should see the new value in the terminal. If we had 1000s of products and we didn't have that parameter in the parent class, we would have to go in and meticulously add the same code over and over to each child class. You _could_ at the percentage inside the super init function on the child function in numerical form if you wanted to and then remove the child.discount = 10 instance.

Now, let's say we had a generic product. We can still create Products; just because it's used in child classes or parent classes, that doesn't really matter. Make an instance of this generic product without creating a new class. Give it a name and a price. Which is bigger? The generic product or the sneaker product? Since the generic product is only taking in the Product params and using nothing else, it is smaller. Child classes are always bigger than Parent classes.

So we can share attr in classes but what about functions? We have that str function in Product and so far we haven't called it; we haven't done anything with it. At this moment, if you printed the Generic Product, the output would just be the name and it's price point. Now, if you printed just nike_free, you will get the name and the price point as well because of that stir method. This is because the Child classes inherit the stir function in the Parent class.

Let's say that soccer balls should print a special message. It would inherit all the methods as well. In the soccer ball class, define the stir function. By creating a stir function inside the child class, it overwrites the parent's stir function. In it, create a promo message for it. When you print the generic product, you will see that it gets the added flair of the promo message on it. 

Essentially what happens is when a function gets called on the soccer ball, it will first try to find that stir function inside itself. If it didn't find it there - if it doesn't exist - then it would look in the parent class for a stir method. If the stir function doesn't exist anywhere, then it will kind of just break. 