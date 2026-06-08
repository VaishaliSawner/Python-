'''
  if condition:
    statement--1;

  if condition:
    statement--1;
    statement--2;
 
 3. if condition:
      statement--1;
    else:
      statement---2;

 4. if condition:
      statement---1;
    elif condition:
      statement---2;
    else:
      statement---3;                   
    
    '''
print("Press 1 for addtion");
print("Press 2 for subtraction");
print("Press 3 for multiplication");
choice = int(input("enter your choice : "))     
if choice == 1:
    a = int(input("enter 1st number : "))
    b = int(input("enter 2nd number"))
    print(f"Addition : {a+b}")

elif choice == 2:    
    a = int(input("enter 1st number : "))
    b = int(input("enter 2nd number"))
    print(f"Subtraction : {a-b}")

elif choice == 3:
    a = int(input("enter 1st number : "))
    b = int(input("enter 2nd number"))
    print(f"Multiplication : {a*b}")
else:
    print("Invalid choice | Try again..")    