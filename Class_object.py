
# class Rectangle():

#     def __init__(self):
#         self.lenght=10
#         self.breadth=5

#     def area(self):
#         return self.lenght * self.breadth
    
#     def permeter(self):
#         return 2 * (self.lenght + self.breadth)
    

# r = Rectangle()
# print("Length: ", r.lenght)
# print("Breadth: ", r.breadth)
# print("Area: ", r.area())
# print("Perimeter: ", r.permeter())

# class Rectangle2:

#     def __init__(self, l, b):
#         self.lenght = l
#         self.breadth = b

#     def area(self):
#         return self.lenght * self.breadth
    
#     def perimeter(self):
#         return 2 * (self.lenght + self.breadth)
    
# r = Rectangle2(4,5)

# print("Length: ", r.lenght)
# print("Breadth: ", r.breadth)
# print("Area: ", r.area())
# print("Perimeter: ", r.perimeter())


# class Rectangle3:

#     def __init__(self, l=1, b=1):
#         self.lenght = l
#         self.breadth = b

#     def area(self):
#         return self.lenght * self.breadth
    
#     def perimeter(self):
#         return 2 * (self.lenght + self.breadth)
    
# r = Rectangle3(5)

# print("Length: ", r.lenght)
# print("Breadth: ", r.breadth)
# print("Area: ", r.area())
# print("Perimeter: ", r.perimeter())

# print("r2")

# r2 = Rectangle3(5, 5)

# print("Length: ", r2.lenght)
# print("Breadth: ", r2.breadth)
# print("Area: ", r2.area())
# print("Perimeter: ", r2.perimeter())

# # Class veriable and class methods

# class test:

#     count = 0           # We declare outside of functions
#     def __init__(self):
#         self.a=10
#         test.count += 1

# t = test()
# t2 = test()
# t3 = test()

# print(t.count)

# class test:

#     count = 0           # We declare outside of functions
#     def __init__(self):
#         self.a=10
#         test.count += 1

#     @classmethod        # We have to write this decorator to call the function where we are returning class variable
#     def get_count(cls):
#         return cls.count

# t = test()
# t2 = test()
# t3 = test()

# print(t.count)
# print(t.get_count())

# Static Method - We call it without creating a object

# class test:
    
#     def __init__(self, l, b):
#         self.length = l
#         self.breadth = b

#     def area(self):
#         return self.length * self.breadth
    
#     @staticmethod
#     def total_area(lenght, breadth):
#         return lenght * breadth
    
# print(test.total_area(10,2))

# Inheritance

class test:
    
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth
    
class test2(test):
    
    def __init__(self, h, l, b):
        self.height = h
        super().__init__(l, b)

    def cube(self):
        return self.height * self.length * self.breadth
    
t2 = test2(3,2,5)

print(t2.cube())


## Testing git projects

print("hello sarang")
print("Git learning")