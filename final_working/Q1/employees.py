# employees.py

class Employee:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def set_first_name(self, name):
        self.__firstName = name

    def set_last_name(self, name):
        self.__lastName = name

    def print_employee(self):
        print("First Name:", self.get_first_name())
        print("Last Name:", self.get_last_name())


class CommissionEmployee(Employee):
    def __init__(self, firstName, lastName, commission_rate, gross_sales):
        super().__init__(firstName, lastName)
        self.__commission_rate = commission_rate
        self.__gross_sales = gross_sales

    def get_commission_rate(self):
        return self.__commission_rate

    def get_gross_sales(self):
        return self.__gross_sales

    def set_commission_rate(self, rate):
        self.__commission_rate = rate

    def set_gross_sales(self, sales):
        self.__gross_sales = sales

    def print_employee(self):
        super().print_employee()
        print("Comission Rate:", self.get_commission_rate())
        print("Gross Sales:", self.get_gross_sales())

    def earnings(self):
        result = self.get_commission_rate() * self.get_gross_sales()
        print("Earnings:", result)


class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, firstName, lastName, commission_rate, gross_sales, base_salary):
        super().__init__(firstName, lastName, commission_rate, gross_sales)
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    def set_base_salary(self, salary):
        self.__base_salary = salary

    def print_employee(self):
        super().print_employee()
        print("Base Salary:", self.get_base_salary())

    def earnings(self):
        total = self.get_base_salary() + (self.get_commission_rate() * self.get_gross_sales())
        print("Earnings:", total)
