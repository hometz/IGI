
import Entities
import GeometricLib
import Serializer
import Text_Analysis
import MatrixOperations
import plot

while True:
    
    try:
        func_number = int(input("Enter the number of task you would like to start (0 to finish): "))

        if func_number == 0:
            break

        elif func_number == 1:


            schedule = Entities.VacationSchedule()
            schedule.add_employee(Entities.Employee("Иван", "Иванов", ["15.07", "16.07", "17.07"]))
            schedule.add_employee(Entities.Employee("Петр", "Петров", ["05.07", "10.08", "11.08", "12.08"]))
            schedule.add_employee(Entities.Employee("Мария", "Сидорова", ["01.07", "20.06", "21.06", "22.06", "01.10"]))

            Serializer.create_vacation_schedule(schedule, "output.txt")
            Serializer.create_vacation_schedule_by_pickle(schedule, "output2.txt")

            count, percentage = schedule.count_employees_by_vacation_month()

            print('Месяц -> Количество людей в отуске -> процент от общего количества')
            for (ckey, cvalue), pvalue in zip(count.items(), percentage.values()):
                print(f'{ckey} -> {cvalue} -> {pvalue}')

            print(schedule.find_employee(input('Введите имя или фамилию для поиска: ')))

        elif func_number == 2:
            print(Text_Analysis.analyze_text("text.txt"))

        elif func_number == 3:
            x_value = 1
            n_terms = 10

            analysis = plot.SequenceAnalysis(x_value, n_terms)
            analysis.print_parameters()
            analysis.plot_graphs()

        elif func_number == 4:
            while True:
                try:
                    choice = input("Выберите фигуру (1 - Прямоугольник, 2 - Треугольник): ")
                    if choice == "1":
                        color = input("Введите цвет фигуры: ")
                        width = float(input("Введите ширину прямоугольника: "))
                        height = float(input("Введите высоту прямоугольника: "))
                        if width <= 0 or height <= 0:
                            raise ValueError("Ширина и высота должны быть положительными числами.")
                        rect = GeometricLib.Rectangle(width, height, color)
                        print(rect)
                        GeometricLib.save_to_file(rect)
                        rect.draw()
                    elif choice == "2":
                        color = input("Введите цвет фигуры: ")
                        side_a = float(input("Введите сторону a треугольника: "))
                        side_b = float(input("Введите сторону b треугольника: "))
                        angle_C = float(input("Введите угол C в градусах между сторонами a и b: "))
                        if side_a <= 0 or side_b <= 0 or not (0 < angle_C < 180):
                            raise ValueError("Стороны должны быть положительными, а угол должен быть в диапазоне (0, 180).")
                        tri = GeometricLib.Triangle(side_a, side_b, angle_C, color)
                        print(tri)
                        GeometricLib.save_to_file(tri)
                        tri.draw()
                    else:
                        raise ValueError("Некорректный выбор. Попробуйте снова.")
                    break
                except ValueError as e:
                    print(f"Ошибка ввода: {e}. Попробуйте снова.")
        elif func_number == 5:
            n, m = 5, 4
            matrix_A = MatrixOperations.MatrixOperations.generate_matrix(n, m)
            print("Матрица A:\n", matrix_A)

            min_value, indices, count_min_elements = MatrixOperations.MatrixOperations.find_min_elements(matrix_A)
            print("Минимальное значение в матрице A:", min_value)
            print("Индексы элементов с минимальным значением:\n", indices)
            print("Количество элементов, равных минимальному значению:", count_min_elements)

            std_deviation_standard, std_deviation_manual = MatrixOperations.MatrixOperations.calculate_standard_deviation(matrix_A)
            print("Стандартное отклонение (используя std()):", std_deviation_standard)
            print("Стандартное отклонение (ручной расчет):", std_deviation_manual)

    except ValueError:
        print("Incorrect input")
        continue




