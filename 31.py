class Employee:
    emp_id = 1
    name = ""
    base_salary = 0
    def __init__(self,eid,n,bs):
        self.emp_id = eid
        self.name = n
        self.base_salary = bs
    def display_employee(self):
        print("Employee ID",self.emp_id)
        print("Name: ",self.name)
        print("Base salary: ",self.base_salary)