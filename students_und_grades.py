#создаю list
grades = [[5, 4, 5, 4], [4, 5, 5, 5], [3, 5, 4, 3], [3, 3, 3, 4], [5, 5, 5, 5]]
#создаю set
students = {'David', 'Xborg', 'Nataly', 'Curt', 'Roberto'}
#присваиваем каждому ученику его оценки
for index, (number, extra) in enumerate(zip(students, grades)) : 
    print(f"{index} : {number}, {extra}")
    


