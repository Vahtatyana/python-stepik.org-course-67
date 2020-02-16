'''Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся

строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой

матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с

противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Hint из комментариев  к задаче: "Проблема, когда индексы выходят за границу списка решается либо в лоб if-elif и вручную подсчетом перехода
границ индексов, либо делением с остатком на длину соответствующего столбца или строки. То есть простыми словами,
когда мы ищем в списке соседа у последнего 3 элемента, он должен быть 4. Но такого в списке нет,
поэтому деление с остатком закольцует список."
'''


matrix = []
res = []
final = []

while (True):
    a = input()
    if a != 'end':
        row = [int(i) for i in a.split()]
        matrix.append(row)
    else:
        matrix.append('end')
        break

for i in range(len(matrix) - 1):
    res.append(matrix[i])

final = [[0 for j in range(len(res[0]))] for i in range(len(res))]

for i in range(len(res)):
    for j in range(len(res[0])):
        final[i][j] = 0
        final[i][j] += res[i % len(res)][(j - 1) % len(res[i])] + \
                       res[i % len(res)][(j + 1) % len(res[i])] + \
                       res[(i - 1) % len(res)][j % len(res[i])] + \
                       res[(i + 1) % len(res)][j % len(res[i])]

for i in final:
    print(*i)






# print(res)
# for i in range(len(matrix)):
#     print( matrix[i])