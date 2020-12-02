import re
from collections import Counter

def task_01():
    pattern = re.compile(r'(?P<lower>\d+)-(?P<upper>\d+)\s(?P<character>\w):\s(?P<password>\w+)')
    with open('input.txt', 'r') as file:
        data = [ x.strip() for x in file.readlines()]
        valid_pass = 0
        for line in data:
            m = re.search(pattern, line)

            lower_bound = int(m.group('lower'))
            upper_bound = int(m.group('upper'))
            character = m.group('character')
            password = m.group('password')
            oc = Counter(password)

            if character in oc:
                if lower_bound <= oc[character] and upper_bound >= oc[character]:
                    valid_pass += 1
    return valid_pass 

print(task_01())

def task_02():
    pattern = re.compile(r'(?P<lower>\d+)-(?P<upper>\d+)\s(?P<character>\w):\s(?P<password>\w+)')
    with open('input.txt', 'r') as file:
        data = [ x.strip() for x in file.readlines()]
        valid_pass = 0
        for line in data:
            m = re.search(pattern, line)

            lower_bound = int(m.group('lower'))
            upper_bound = int(m.group('upper'))
            character = m.group('character')
            password = m.group('password')

            if password[lower_bound - 1] != password[upper_bound - 1] and (password[lower_bound - 1] == character or password[upper_bound - 1] == character):
                valid_pass += 1
            
        return valid_pass

print(task_02())