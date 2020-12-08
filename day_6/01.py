import string
def task_01():
    with open('in.txt', 'r') as file:
        data = ''.join(file.readlines()).split('\n\n')

        cnt = 0

        for group in data:
            g = len(list(set(''.join([x.strip() for x in group]))))

            cnt += g

        return cnt

# print('Task 1:')
# print(task_01())

def task_02():
    with open('in.txt', 'r') as file:
        data = ''.join([ x for x in file.readlines()]).split('\n\n')
        data = [x.split('\n') for x in data]

        cnt = 0
        for group in data:
            overlap = set(string.ascii_lowercase)
            for answers in group:
                overlap = overlap.intersection(set(answers))
            cnt += len(overlap)

        return cnt


print('Task_2:')
print(task_02())
