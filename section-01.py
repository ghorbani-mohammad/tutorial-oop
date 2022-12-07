class Employee:
    def __init__(self, name, base_salary, years):
        self.name = name
        self.base_salary = base_salary
        self.years = years

    def salary(self):
        return self.base_salary + (self.years * 1000)


# We have two type of employees: Developer and Manager
# Developers are regular employees
# But managers are higher level employees and get 10 percent more salary
# So how we should implement this situation?


class Developer(Employee):
    """Developers are just regular employees

    Args:
        Employee (Employee): employee
    """

    pass
