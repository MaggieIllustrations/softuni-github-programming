

 # r - read the information from the file, w - writes, change the file, r+ - read and write, a- add new information
employee_file = open("Employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()

employee_file = open("Employees.txt", "a")
employee_file.write ("\nKelly - Customer Service")

employee_file.close
