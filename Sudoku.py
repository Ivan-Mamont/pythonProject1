import random
import solver_sudoku

class Grid:
    n = property(lambda self: self.__n)
    table = property(lambda self: self.__table)
    def __init__(self, n=3, print_callback=lambda *args, **kwarg: None):
        self.__print_callback = print_callback
        """Generation of the base table"""
        self.__n = int(n)
        self.__table = [[(int(i * n + i // n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
        self.__print_callback('The base table is ready!')

    def show(self):
        for i in range(self.__n * self.__n):
            print(self.__table[i])

    def transposing(self):
        """ Transposing the whole grid """
        self.__table = list(map(list, zip(*self.__table)))


    def swap_rows_small(self):
        r'''Swap two rows.

    	'''

        # случайные разные строки в пределах района
        line1, line2 = random.sample(range(self.__n), 2)

        # получение случайного района
        area = random.randrange(self.__n)

        # строки для обмена
        N1 = area * self.__n + line1
        N2 = area * self.__n + line2

        self.__table[N1], self.__table[N2] = self.__table[N2], self.__table[N1]


    def swap_rows_area(self):
        r'''Swap two area horizon.
        '''


        # случайные разные районы
        area1, area2 = random.sample(range(self.__n), 2)


        for i in range(self.__n):
            N1, N2 = area1 * self.__n + i, area2 * self.__n + i
            self.__table[N1], self.__table[N2] = self.__table[N2], self.__table[N1]



    def swap_colums_small(self):
        Grid.transposing(self)
        Grid.swap_rows_small(self)
        Grid.transposing(self)

    def swap_colums_area(self):
        Grid.transposing(self)
        Grid.swap_rows_area(self)
        Grid.transposing(self)

    def mix(self, amt=10):
        mix_func = (self.transposing,
                    self.swap_rows_small,
                    self.swap_colums_small,
                    self.swap_rows_area,
                    self.swap_colums_area)
        for i in range(amt):
            random.choice(mix_func)()





example = Grid()
example.mix()


flook = [[0 for j in range(example.n*example.n)] for i in range(example.n*example.n)]
iterator = 0
difficult = example.n ** 4 #Первоначально все элементы на месте

# example.show()
# print("---------------------------")

while iterator < example.n ** 4:
    i,j = random.randrange(0, example.n*example.n ,1), random.randrange(0, example.n*example.n ,1) # Выбираем случайную ячейку
    if flook[i][j] == 0:	#Если её не смотрели
        iterator += 1
        flook[i][j] = 1 	#Посмотрим

        temp = example.table[i][j]	#Сохраним элемент на случай если без него нет решения или их слишком много
        example.table[i][j] = 0
        difficult -= 1 #Усложняем если убрали элемент

        table_solution = []
        for copy_i in range(0, example.n*example.n):
            table_solution.append(example.table[copy_i][:]) #Скопируем в отдельный список


        i_solution = 0
        for solution in solver_sudoku.solve_sudoku((example.n, example.n), table_solution):
            i_solution += 1 #Считаем количество решений

        if i_solution != 1: #Если решение не одинственное вернуть всё обратно
            example.table[i][j] = temp
            difficult += 1 # Облегчаем

example.show()
print("difficult = ", difficult)

