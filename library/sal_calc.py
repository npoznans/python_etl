from random import randint
import csv
import pandas


def timeline(salary, age, presults, raise_range, bonus):
    years = 65 - int(age)
    if presults == 'n':
        pass
    else:
        print(presults)
    for y in range(0, years):
        raises = randint(0, int(raise_range)) * 0.01 + 1
        bonus = randint(0, int(bonus)) * .01
        print(y)
        nsal = int(salary) * raises
        salary = nsal
        print(salary)
        # write_to_csv(salary)


def write_to_csv(vals):
    with open('sal_sim.csv', 'r') as csv_file:
        rows = csv.writer(csv_file, delimiter = ',')
        for row in vals:
            rows.writerow(vals)


inquire = input("Do you want to make this a dynamic simulator\t'y' or 'n'\n\n>")

if str(inquire.lower()) == 'y' or inquire == 'yes':
    salary = input("Enter base salary\n\n>")
    presults = input("Would you like to see all of the output\n'y'\tor\t'n'\n\n>")
    raise_range = input("Enter most of the raise amount\n\n>")
    bonus = input("Enter most amount of bonus amount\n\n>")
    age = input("Enter a starting age\n\n>")
    if salary == '' or int(salary) <= 0 or str(salary).isalpha():
        salary = 100000
    else:
        pass
    if presults == '' or str(salary).isdigit():
        presults = 'y'
    else:
        pass
    if raise_range == '' or int(raise_range) <= 0 or str(raise_range).isalpha():
        raise_range = 10
    else:
        pass
    if bonus == '' or int(bonus) < 0 or str(bonus).isalpha():
        bonus = 10
    else:
        pass
    if age == '' or int(age) < 18 or str(age).isalpha():
        age = 18
    else:
        pass
else:
    salary = 100000
    presults = 'n'
    raise_range = 5
    bonus = 10
    age = 18

pr = '{} starting salary, {} all output, {} max raise, {} max bonus, {} starting age'.format(salary, presults, raise_range, bonus, age)

timeline(salary, age, pr, raise_range, bonus)
