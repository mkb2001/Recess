dict = {"name":"name", "course":"course", "Year":"Year", "Grade":"Grade"}
values = dict.values()
print(values)

if(dict.get("name")):
    print("The key exists")
else:
    print("Not found")

extension_dict={"HOD":"HOD"}
dict.update(extension_dict) 

removes = dict.pop("Grade")
print(removes)

for item in dict:
    print(item)

nested_dict = {"Ministry Of Health":
               {
                   "PS":"DR Diana",
                   "Minister":"Dr Acheng"
    
                },
               "Ministry of Ict":
               {
                   "PS":"Mr Chris",
                   "Minister":"Mr Chris"
               },
               "Ministry of Education":
               {
                   "PS":"Mrs Janet",
                   "Minister":"Mr Muyingo"
               }
               
               }
print(nested_dict["Ministry of Education"]["PS"])

#Find Data types

a = 2
b = 2+9j
c = 9.08

print(type(a))
print(type(b))
print(type(c))

#TypeCasting

