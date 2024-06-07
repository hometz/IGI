from collections import Counter

class Employee:
    def __init__(self, name, surname, vacation):
        self.name = name
        self.surname = surname
        self.vacation = vacation


class VacationSchedule:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee(self, name):
        for employee in self.employees:
            if employee.surname == name or employee.name == name:
                return employee.vacation
        return None

    def sort_employees_by_surname(self):
        self.employees.sort(key=lambda x: x.surname)

    def sort_employees_by_vacation_date(self):
        self.employees.sort(key=lambda x: x.vacation[0])

    def count_employees_by_vacation_month(self):
        month_counter = Counter()

        for employee in self.employees:
            vacation_months = set(date.split('.')[1] for date in employee.vacation)
           
            for month in vacation_months:
                month_counter[month] += 1

        total_employees = len(self.employees)

        vacation_percentages = {}

        for month, count in month_counter.items():
            percentage = (count / total_employees) * 100
            vacation_percentages[month] = round(percentage)

        return month_counter, vacation_percentages