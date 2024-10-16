class MyClass:
    pass

my_obj = MyClass()

# Myclass ---> It is a class
# my_obj ---> It is instance

print(type(my_obj).__name__)
print(isinstance(my_obj, MyClass))