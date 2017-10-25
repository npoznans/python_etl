from random import randint
import csv
import pandas


def timeline(salary, age, presults, raise_range, bonus):
    years = 65 - int(age)
    for y in range(0, years):
        raises = randint(0, int(raise_range))
        bonus = randint(0, int(bonus))
        print(y)
        nsal = salary * raises
        print(nsal)



salary = input("Enter base salary\n\n>")
presults = input("Would you like to see all of the output\n'y'\tor\t'n'\n\n>")
raise_range = input("Enter most of the raise amount\n\n>")
bonus = input("Enter most amount of bonus amount\n\n>")
age = input("Enter a starting age\n\n>")

if salary == '':
    salary = 100000
else:
    salary
if presults == '':
    presults = 'y'
else:
    presults
if raise_range == '' or int(raise_range) <= 0 or str(raise_range).isalpha:
    raise_range = 10
else:
    raise_range
if bonus == '' or int(bonus) < 0 or str(bonus).isalpha:
    bonus = 10
else:
    bonus
if age == '' or int(age) < 18 or str(age).isalpha:
    age = 18
else:
    age

print(salary, presults, raise_range, bonus, age)

timeline(salary, age, presults, raise_range, bonus)
