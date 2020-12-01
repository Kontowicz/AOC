def task_01():
    with open('01_input.txt', 'r') as file:
        data = {int(x.strip()) for x in file.readlines()}
        for v in data:
            if 2020 - v in data:
                return (2020 - v) * v

print(task_01())