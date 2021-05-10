task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
print(id(task_list))

def concat():
    task_list.insert(i, '"')
    task_list.insert(i + 2, '"')
    task_list[i] = task_list[i] + task_list[i + 1] + task_list[i + 2]
    task_list.pop(i + 1)
    task_list.pop(i + 1)

while i < len(task_list):
    if not task_list[i].isalpha() and len(task_list[i]) < 2 and not task_list[i].count("+"):
        #number = '"' + task_list[i].zfill(2) + '"' - мне такой вариант больше нравится, так как не нужно потом массив пересчитывать
        number = task_list[i].zfill(2)
        task_list[i] = number
        concat()
    elif not task_list[i].isalpha() and not task_list[i].count("+"):
        number = task_list[i]
        task_list[i] = number
        concat()
    elif task_list[i].count("+"):
        number = task_list[i].zfill(3)
        task_list[i] = number
        concat()
    task_print = ' '.join(task_list)
    i += 1
print(id(task_list))
print(task_print)

