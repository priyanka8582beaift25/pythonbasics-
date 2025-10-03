# Write a python program to convert celsius to fahrenheit using map()

celsius=[0,20,37,100]
fahrenheit=list(map( c for c in celsius if c*(9/5)+32))
print(fahrenheit)

