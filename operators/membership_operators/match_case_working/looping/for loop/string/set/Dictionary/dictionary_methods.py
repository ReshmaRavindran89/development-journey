
"""
class dict:
    def keys(self): -> return all keys.
    def values(self): -> return all values.
    def get(self,key): ->  when key is invalid  return none .
    def pop(self,key):->remove key
    []  -> if key is invalid return error.
"""
#  return keys #

employee = {"id":101,"name":"hari","salary":54000,"dept":"qa"}
for keys in employee.keys():
    print(keys)

# return values #

for val in employee.values():
    print(val)

#  return keys and values  #

for k,v in employee.items():
    print(k,v)
#   get()  #

print(employee.get("name"))
print(employee.get("email","dummy@gmail.com")) 

employee.pop("dept")
print(employee)

#  Adding #

employee["bonus"]=5000
print(employee)

#  Updating #

employee["salary"]+=10000
print(employee)