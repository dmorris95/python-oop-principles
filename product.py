#Task 1

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_information(self):
        print("Products ID:",self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)

#Task 2
class Book(Product): #book class inherits from the product class
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    #Task 3
    #method override for the book class
    def display_information(self):
        print("Products ID:",self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Author:", self.author)


#Task 2
class Electronic(Product): #electronic class inherits from product class
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    #Task 3
    #method override for the electronic class
    def display_information(self):
        print("Products ID:",self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Specs:", self.specs)

#Task 2
class Clothing(Product): #clothing class inherits from product class
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    #Task 3
    #method override for the clothing class
    def display_information(self):
        print("Products ID:",self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Clothing Size:", self.size)
