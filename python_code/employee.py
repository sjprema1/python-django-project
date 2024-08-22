
from portal import Portal
# Function to check if an employee exists


# Function to add an employee
def add_employee():
    Id = input("Enter Employee Id: ")
    obj = Portal()
    if obj.check_employee(Id):
        print("Employee already exists. Please try again.")
        return

    Name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")

    obj.insert_employee_data(Id,Name,Post,Salary)


# Function to remove an employee
def remove_employee():
    obj = Portal()
    Id = input("Enter Employee Id: ")
    if obj.check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    obj.delete_employee_data(Id)


# Function to promote an employee
def promote_employee():
    obj = Portal()
    Id = input("Enter Employee's Id: ")
    if not obj.check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    try:
        Amount = float(input("Enter increase in Salary: "))
        current_salary = obj.check_current_salary(Id)
        new_salary = current_salary + Amount
        obj.update_new_salary(new_salary,Id)
        print("Employee Promoted Successfully")

    except ValueError as e:
        print(f"Error: {e}")

# Function to display all employees
def display_employees():
    try:
        obj = Portal()
        employees = obj.display_employees()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except Exception as e:
        print(e)


# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")
