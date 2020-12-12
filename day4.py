import re

fields = '''
byr
iyr
eyr
hgt
hcl
ecl
pid'''.strip().splitlines()



with open('inputs/day4', 'r') as f:
    input_ = f.read().strip().split('\n\n')

# input_ = '''
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

# '''.strip().split('\n\n')

# for w in input_:
#     # print(w)
#     # print('\n' in w)
#     if '\n' in w:
#         nw = w.split('\n')[1]
#         input_.append(nw)

valid = 0
fields = sorted(fields)
for i, passport in enumerate(input_):
    invalid = False
    print(passport)
    p_fields = list()
    p_lines = passport.split('\n')
    # print(len(p_lines))
    for line in p_lines:
        
        p_fields.extend(line.split(' '))
    
    # print(p_fields)
    # break
    # for p_f in p_fields:
    #     if '\n' in p_f:
    #         p_fields.remove(p_f)
    #         p_fields.extend(p_f.split('\n'))
    p_fields = [ p_field.split(':') for p_field in p_fields ]
    p_fields_ids = [ p_field[0].strip() for p_field in p_fields ]
    p_fields_vals = [ p_f[1].strip() for p_f in p_fields ]
    p_fields_ids = sorted(p_fields_ids)
    # print('present:', p_fields_ids)
    # print('required:', fields)

    # print(p_fields_vals)

    for field in fields:
        if field not in p_fields_ids:
            invalid = True

    for f in p_fields:
        f_id = f[0]
        f_val = f[1]
        print(f_id, f_val)
        try:
            if f_id == 'byr':
                if len(f_val) != 4:
                    invalid = True
                    print(' byr len')
                if not (1920 <= int(f_val) <= 2002):
                    invalid = True
                    # print(' byr val')

            if f_id == 'iyr':
                if not (2010 <= int(f_val) <= 2020):
                    # print(' iyr year')
                    invalid = True
            if f_id == 'eyr':
                if not (2020 <= int(f_val) <= 2030):
                    invalid = True
            if f_id == 'hgt':
                units = f_val[-2:]
                f_val = f_val[:-2]
                if units == 'cm':
                    if not (150 <= int(f_val) <= 193):
                        invalid = True
                elif units == 'in':
                    if not (59 <= int(f_val) <= 76):
                        invalid = True
                else:
                    invalid = True

            if f_id == 'hcl':
                if f_val[0] != '#': invalid = True
                if len(f_val) != 7: invalid = True
                for c in f_val[1:]:
                    if c not in 'abcdef0123456789':
                        invalid = True

            if f_id == 'ecl':
                if f_val not in 'amb blu brn gry grn hzl oth'.split(' '):
                    invalid = True
                    
            if f_id == 'pid':
                f_val_t = int(f_val)
                if len(f_val) != 9:
                    invalid = True
 
        except ValueError:
            invalid = True
        


    if invalid:
        print('invalid')
        print('---\n\n')
        continue
    print('valid')
    valid += 1
    print('---\n\n')

    # print(p_fileds)

print(valid)