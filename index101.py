#Running python scripts

print("Hello Python")
name = "Kevin"
profession = "student"
age = 25
print("My name is " + name + " I am a """
      + profession+ " and I am """
      + str(age)+ " years old.")

""" 
Control Flow 
"""
age = 11
if age<12:
      print("You are underage")
elif age>13 and age<18:
      print("You are a teenager but still underage")
else:
      print("you are an adult")

"""
while and for loops
"""
dict = {"course": "Bsse", "semester": "recess", "period":"10Weeks"}
while True:
      i = 0
      print(dict[i])
      i += 1
      if(i==2):
            continue

"""Exception Handling"""
password = ""
