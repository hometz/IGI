import statistics
import math
import numpy as np
import matplotlib.pyplot as plt

class SequenceAnalysis:
    def __init__(self, x, n_terms):
        self.x = x
        self.n_terms = n_terms
        self.sequence = [self.taylor_series_term(x, i) for i in range(n_terms)]
        self.calculate_parameters()

    def taylor_series_term(self, x, n):
        return (x ** n) / math.factorial(n)
    
    def taylor_series_sum(self, x):
        return sum(self.taylor_series_term(x, n) for n in range(self.n_terms))
    
    def calculate_parameters(self):
        self.mean = np.mean(self.sequence)
        self.median = np.median(self.sequence)
        try:
            self.mode = statistics.mode(self.sequence)
        except statistics.StatisticsError:
            self.mode = None
        self.variance = np.var(self.sequence)
        self.std_deviation = np.std(self.sequence)

    def print_parameters(self):
        print(f"Среднее арифметическое: {self.mean}")
        print(f"Медиана: {self.median}")
        print(f"Мода: {self.mode}")
        print(f"Дисперсия: {self.variance}")
        print(f"СКО: {self.std_deviation}")

    def plot_graphs(self):
        x_values = np.linspace(0, self.x, 100)
        y_taylor = [self.taylor_series_sum(x) for x in x_values]
        y_exact = [math.exp(x) for x in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_taylor, label='Разложение в ряд', color='blue')
        plt.plot(x_values, y_exact, label='Функция $e^x$', color='red')
        
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        
        plt.legend()
        plt.title('Сравнение разложения функции $e^x$ в ряд Тейлора и функции $e^x$')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.text(0.5, 0.5, 'Разложение функции в ряд и функция $e^x$', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.annotate('Порядок разложения: {}'.format(self.n_terms), xy=(0.7, 0.9), xycoords='axes fraction')
        
        plt.show()