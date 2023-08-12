#Matching and Searching
#regex re.match(), re.search() and re.findall()

import re
text = "Hello, world!"
match = "hello"
search_match = re.search(r"^\w+$", text)
print(search_match)
if search_match:
    print("matched")

matches = re.findall(r"\d+", text)
print("Matches:", matches)
print(re.match(match, text))

#Validate Email
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern,email):
        return "Correct Email"
    else:
        return "false email"
email = "kevin@example.com"
email1 = "validate_email(email"

print(validate_email(email))
print(validate_email(email1))

#Generators and iterators
# 'yeild' generator
# iterator '__iter__' generator
# 

# def factorial(n):
 
#     if n == 0:
#         yield 1
   
#     yield n * factorial(n-1)

# for item in factorial(10):
#     print(item)
       

# def generator(n,m):        
#     for generator_item in range(n, m):
#         print(factorial(generator_item))
# print(generator(1,10))

#Decorators use @my_decorator

def mydecorator(func):
    def inner_func():
        print("this is the decorator")
        func()
    return inner_func

@mydecorator
def outer_func():
    print("this is the outer function")
    
outer_func()