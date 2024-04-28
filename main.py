#Task 4

from product import Product, Book, Clothing, Electronic

one_book = Book("343", "Important Topics", 15.99, "Ron Smith")
one_book.display_information()

two_electronic = Electronic("211", "Television", 349.99, "LCD 55\"")
two_electronic.display_information()

main_prod = Product("001", "Default", 1.00)
main_prod.display_information()

big_clothing = Clothing("329", "Brand T-shirt", 19.99, "XL")
big_clothing.display_information()