def showDetails(fruitName, fruitColor, friutPrice):
    print("Here are my details", fruitName, fruitColor , friutPrice)
    
    
showDetails("melon", "green", 1200)

import module
print(module.product(1,2))

from math import sqrt, factorial
print(sqrt(25))
print(factorial(3))

W = (2,3,4,5,6,7)
print("current tuple")
print(W)
print(type(W))

E = list(W)
E.append(int(input("Enter new value")))
W = tuple(E)
print("Updated Tuple")
print(W)