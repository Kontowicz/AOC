import re

def task_01():
    with open('in.txt', 'r') as file:
        data = ''.join(file.readlines()).split('\n\n')
        cnt = 0
        for batch in data:
            data = batch.replace('\n', ' ')
            data = data.split(' ')
            required = {'ecl' : False, 'pid' : False, 'eyr' : False, 
            'hcl' : False, 'byr' : False, 'iyr' : False, 'hgt' : False }
            for item in data:
                field, _ = item.split(':')
                if field == 'cid':
                    continue
                required[field] = True

            if list(required.values()) == [True for i in range(0, 7)]:
                cnt += 1
        return cnt

print('Task 01:')
print(task_01())

def task_02():
    with open('in.txt', 'r') as file:
        data = ''.join(file.readlines()).split('\n\n')

        cnt = 0

        byr_pat = re.compile(r'byr:(\d+)')
        iyr_pat = re.compile(r'iyr:(\d+)')
        eyr_pat = re.compile(r'eyr:(\d+)')
        hgt_pat = re.compile(r'hgt:(\d+)(cm|in)')
        hcl_pat = re.compile(r'hcl:#([\d|\w]+)')
        ecl_pat = re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)')
        pid_pat = re.compile(r'pid:(\d+)')

        for batch in data:
            f_cnt = 0

            m = re.search(byr_pat, batch)
            if m:
                birth = m.group(1)
                if len(birth) == 4:
                    if int(birth) >= 1920 and int(birth) <= 2002:
                        f_cnt += 1


            m = re.search(iyr_pat, batch)
            if m:
                issue = m.group(1)
                if len(issue) == 4:
                    if int(issue) >= 2010 and int(issue) <= 2030:
                        f_cnt += 1

            m = re.search(eyr_pat, batch)
            if m:
                exp = m.group(1)
                if len(exp) == 4:
                    if int(exp) >= 2020 and int(exp) <= 2030:
                        f_cnt += 1
                        
            m = re.search(hgt_pat, batch)

            if m:
                val = m.group(1)
                x = m.group(2)
                if x == 'cm':
                    if int(val) >= 150 and int(val) <= 193:
                        f_cnt += 1
                elif x == 'in':
                    if int(val) >= 59 and int(val) <= 76:
                        f_cnt += 1

            m = re.search(hcl_pat, batch)

            if m:
                hcl = m.group(1)
                if len(hcl) == 6:
                    p = re.compile(r'([0-9a-f]{6})')
                    if re.search(p, hcl):
                        f_cnt += 1

            m = re.search(ecl_pat, batch)
            if m:
                f_cnt += 1

            m = re.search(pid_pat, batch)
            if m:
                pid = m.group(1)
                if len(pid) == 9:
                    f_cnt += 1


            if f_cnt == 7:
                cnt += 1

        return cnt



print('Task 02:')
print(task_02())