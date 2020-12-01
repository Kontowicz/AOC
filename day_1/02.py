def task_02():
    with open('01_input.txt', 'r') as file:
        data = {int(x.strip()) for x in file.readlines()}

        for v in data:
            for z in data:
                if 2020 - v - z in data:
                    return z * v * (2020 - v - z)

print(task_02())