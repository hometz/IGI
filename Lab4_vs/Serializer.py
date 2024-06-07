import csv
import pickle

def create_vacation_schedule(vacation_schedule, filename):

    vacation_schedule.sort_employees_by_surname()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Дни отпуска"])

        for employee in vacation_schedule.employees:
            writer.writerow([employee.surname, employee.vacation])

def create_vacation_schedule_by_pickle(vacation_schedule, filename):

    vacation_schedule.sort_employees_by_surname()

    with open(filename, 'wb') as file:
        pickle.dump(vacation_schedule, file)