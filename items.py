'''
item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity
'''
#creation of a class..
#creating our own datatype to use in our code.

#creation of the class
class Item: # class name must be capital.
    def __init__(self,) -> None:
        pass
    #creation of method( a function in a class.)
        #our method must have atleast a parameter known as'self'.
    def Calculate_total_price(self, x, y):
        return x * y


#instantiating some objects of the class..
    #meaning to create objects of the class.
item_1 = Item()
#assigning attributes to instances (objects) of a class, we use dots(.)
item_1.name = "Phone"
item_1.price = 100
item_1.quantity = 5
print(item_1.Calculate_total_price(item_1.price,item_1.quantity))
'''
the above three are related;each one of the attributes are assigned to 
one instance of the class
'''
item_2 = Item()
item_2.name = "Laptop"
item_2.price = 1000
item_2.quantity = 3
print(item_2.Calculate_total_price(item_2.price,item_2.quantity))

# creating methods and executing them on instances or objects.
'''This is going to be done the class fuction.'''

