tasks = ["Помыть посуду", "Сходить в магазин",
         "Сделать ДЗ", "Позвонить кому-то"]
done = [False, True, False, True]

for i in range(len(tasks)):
    print(f'[{'x' if done[i] == True else ' '}] {tasks[i]}')

print()

tasks = [
    ["Помыть посуду", False],
    ["Сходить в магазин", True],
    ["Сделать ДЗ", False],
    ["Позвонить кому-то", True]
]

for i in range(len(tasks)):
    print(f'[{'x' if tasks[i][1] == True else ' '}] {tasks[i][0]}')
