first_value = int(input("enter 1st value : "))
second_value = int(input("enter 2nd value : "))
third_value = int(input("enter 3rd value : "))

# expression-1 if condition else expression-2
#print(f"Max:  {first_value}") if first_value > second_value else print(f"Max: {second_value}")

print(f"Max : {first_value}") if first_value > second_value and first_value > third_value else print(f"Max : {second_value}") if second_value > third_value else print(f"Max : {third_value}")