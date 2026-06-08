'''
  customer of bank :-
   id,name,contact,age
'''
customer = {"id": 100, "name": "Atul", "contact": "9009111322","age": 21}

# customer.keys() ==> ["id","name","contact","age"]
for key in customer.keys():
  print(key," : ",customer[key])

print("Getting values...........")

for value in customer.values():
  print(value)

for key,value in customer.items():
  print(f"{key} : {value}")