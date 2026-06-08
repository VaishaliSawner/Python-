import mysql.connector
con = None
cursor =None

try:
      con = mysql.connector.connect(
       host = "localhost",
       user = "root",
       password="VAISHALI",
       database="pdbcd"
      )
      print("DATABASE CONNECTED")
      if con is not None:
          cursor=con.cursor()
          name=input("Enter the name")
          salary=float(input("Enter the salary"))
          department=input("Enter the department")
          sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
          cursor.execute(sql(name,salary,department))
          con.commit()


except Exception as err:
      if con is not None and con.is_connected():
        con.rollback()
        print(err)
        print("Oops something went wrong")

finally:
    if cursor is not None:
        con.close()
    if con is not None:
        con.close()





