class Employee:
    def __init__(self, empid, name, basicpay, ta, da):
        self.empid = empid
        self.name = name
        self.basicpay = basicpay
        self.ta = ta
        self.da = da
        self.grosspay = 0
    def calc(self):
        self.grosspay = self.basicpay + (0.10 * (0.40 * self.da))
    def disp(self):
        print("\nEmployee Details")
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basicpay)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.grosspay)      
    def __del__(self):
        print("\nEmployee object destroyed. Memory released.")
empid = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
basicpay = float(input("Enter Basic Pay: "))
ta = float(input("Enter TA: "))
da = float(input("Enter DA: "))
emp = Employee(empid, name, basicpay, ta, da)
emp.calc()
emp.disp()                                        