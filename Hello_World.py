# 1
#import os
#need_path = os.path.join('/home', 'user', 'Рабочий стол', 'tstp', 'hello.txt')
#with open(need_path, 'r') as f:
#    print(f.read())
# 2
#with open('ex2.txt', 'w') as f:
#    f.write(input('Введите тектс'))
# 3
import csv
films = [["Звездные войны", "Терминатор", "Искусственный элемент"],
         ["Дурак", "Матильда", "Левиафан"],
         ["Люди в черном", "Я - робот", "Эволюция"]]
with open('ex3.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    for film in films:
        w.writerow(film)
    
