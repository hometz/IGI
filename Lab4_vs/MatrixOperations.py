import numpy as np

class MatrixOperations:
    @staticmethod
    def generate_matrix(n, m):
        """
        Генерирует целочисленную матрицу размером n x m с случайными значениями от 0 до 100.
        """
        matrix = np.random.randint(0, 101, size=(n, m))
        return matrix

    @staticmethod
    def find_min_elements(matrix):
        """
        Находит минимальное значение в матрице, его индексы и количество таких элементов.
        """
        min_value = np.min(matrix)
        indices = np.argwhere(matrix == min_value)
        count_min_elements = indices.shape[0]
        return min_value, indices, count_min_elements

    @staticmethod
    def calculate_standard_deviation(matrix):
        """
        Вычисляет стандартное отклонение для всех значений матрицы двумя способами:
        - Используя встроенную функцию numpy.std()
        - Рассчитывая вручную по формуле
        """
        # Стандартное отклонение с использованием numpy
        std_deviation_standard = np.std(matrix)
        
        # Ручной расчет стандартного отклонения
        mean_value = np.mean(matrix)
        variance = np.mean((matrix - mean_value) ** 2)
        std_deviation_manual = np.sqrt(variance)
        
        return round(std_deviation_standard, 2), round(std_deviation_manual, 2)