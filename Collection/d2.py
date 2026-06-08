'''
  customer of bank :-
   id,name,contact,age
'''
customer = {"id": 100, "name": "Atul", "contact": "9009111322","age": 21}

# print(f" Id : {customer.id}") :- Error
print(f" id : {customer["id"]} second way {customer.get("id")}")
print(f" Name : {customer["name"]}")
print(f"Contact : {customer["contact"]}")
print(F"Age : {customer["age"]}")