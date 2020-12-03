from functools import reduce

def task_01(r_slope, d_slope):
    with open('in.txt', 'r') as file: 
        data = [ list(x.strip()*3000) for x in file.readlines()]

        x, y = 0, 0

        x += r_slope
        y += d_slope
        cnt = 0

        while(x < len(data[0]) and y < len(data)):

            cnt += 1 if data[y][x] == '#' else 0
            data[y][x] = 'X' if data[y][x] == '#' else '0'

            x += r_slope
            y += d_slope

        return cnt

print('Task 1:')
print(task_01(3, 1))

def task_02():
    return reduce(lambda x, y: x*y, [task_01(s[0], s[1]) for s in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]])

print('Task 2:')
print(task_02())