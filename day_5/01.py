import math

def get_right(lower, upper):
    return [math.ceil(lower + ((upper - lower) / 2)), upper]

def get_left(lower, upper):
    return [lower, math.floor(lower + ((upper - lower)/2))]

def task_01():
    with open('in.txt', 'r') as file:
        data = [ x.strip() for x in file.readlines() ]
        seat_id = []

        for line in data:
            collumn = [0, 7]
            row = [0, 127]
            for ch in line:
                if ch == 'F':
                    row = get_left(row[0], row[1])
                if ch == 'B':
                    row = get_right(row[0], row[1])
                if ch == 'R':
                    collumn = get_right(collumn[0], collumn[1])
                if ch == 'L':
                    collumn = get_left(collumn[0], collumn[1])

            seat_id.append(row[1] * 8 + collumn[1])

        return sorted(seat_id)
        

print('Task 1:')
print(max(task_01()))

def task_02():
    data = task_01()
    for i in range(0, len(data) - 1):
        if data[i] + 1 != data[i+1]:
            return(data[i] + 1)

print('Task 2:')
print(task_02())