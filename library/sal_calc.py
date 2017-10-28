from random import randint
import csv
import pandas

def timeline(salary, age, presults, raise_range, bonus):
    years = 65 - int(age)
    sal_hist = []
    for y in range(0, years):
        raises = randint(0, raise_range) * 0.01 + 1
        bonus = randint(0, bonus) * .01
        nsal = int(salary) * raises
        salary = nsal
        sal_hist.append(salary)
    return(sal_hist)
    if presults == 'y':
        write_to_csv(salary)
    else:
        pass


def write_to_csv(vals):
    with open('sal_sim.csv', 'r') as csv_file:
        rows = csv.writer(csv_file, delimiter = ',')
        for row in vals:
            rows.writerow(vals)



def simulator():
    pass

def debt_calc(debt, payment, bump):
    i = 0
    interest = round((12.99 * 365)/12, 2)
    while debt >= 0:
        i += 1
        if i%12 and i>0:
            bns = bump
            dbump = 2 + i
        else:
            bns = 0
            dbump = 0
        n_interest = (interest - (2.93 + (i * .01) + dbump))
        interest = round(n_interest, 2)
        ndebt = debt + interest - (avg_payment + bns)
        debt = round(ndebt, 2)
        print(i, debt, interest, avg_payment+bns)
        return'{},{},{},{}'.format(i,debt,interest,avg_payment+bns)


inquire = input("Do you want to make this a dynamic simulator\t'y' or 'n'\n\n>")
monte_carlo =
pway = input("Do you want to do 'retirement' or 'salary'?>\n\n>")

if str(inquire.lower()) == 'y' or inquire == 'yes':
    if str(pway.lower()) == 'salary':
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
elif str(pway.lower()) == 'retirement' and str(inquire.lower()) == 'n':
    debt_calc(70000, 1000, 6000)
else:
    debt_calc(70000, 1000, 6000)
    timeline(12000, 31, 'n', 10, 10)


pr = '{} starting salary, {} all output, {} max raise, {} max bonus, {} starting age'.format(salary, presults, raise_range, bonus, age)
headers = pr
timeline(salary, age, pr, raise_range, bonus)
