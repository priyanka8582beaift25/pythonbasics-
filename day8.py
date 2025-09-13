# def factorial(n):
#     if n==0 or n==1 :
#         return 1
#     return  n*factorial(n-1)
# print("factorial of 5 is",factorial(5))


# def greet() :
#     print("Hello! welcome to python")
# greet()
    

# def add(a,b):
#     return a+b 
# res=add(5,6)
# print("Sum=",res)
    

#Passing arguments 
# def greet (name,age):
#     print(f"Hello {name},You are {age} years old")
# greet("Priyanka",18)


# def greet(name="Guest"):
#     print(f"Hello {name}!")
# greet()
# greet("Alice")
# greet("Spiderman")


# Yield: yield is like a return, but instead of returning once ,it returns a sequence of values one by one 
def simple_generator() :
    yield 1
    yield 2
    yield 3
for value in simple_generator():
    print(value)