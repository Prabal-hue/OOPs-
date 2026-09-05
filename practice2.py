# Creat a class Laptop with attribute: brand, RAM, price. Creat 2 objects with different values 

class Laptop:
    brand="default"
    RAM=" 8gb"
    price=" 1 lakh"
    
obj1= Laptop()
obj1.brand="Lenovo"
obj1.RAM="8gb"
obj1.price="60 thousand"
print("Laptop brand-", obj1.brand)

obj2= Laptop()
obj2.brand="Macbook"
obj2.RAM="16gb"
obj2.price="1 lakh"
print("Laptop brand-", obj2.brand)