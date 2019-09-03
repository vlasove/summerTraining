def salary_parser(salary):
    temp = salary.split()
    coef = 1
    converter = {'руб.': 1, 'USD': 65, 'EUR': 72}
    for currency in converter.keys():
        if currency == temp[-1]:
            coef = converter[currency]
    try:
        print((int(temp[0]) + int(temp[1].split('-')[1]))*1000/2*coef)
        return (int(temp[0]) + int(temp[1].split('-')[1]))*1000/2*coef
    except:
        print(int(temp[1])*1000*coef)
        return int(temp[1])*1000*coef
