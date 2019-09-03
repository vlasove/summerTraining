def parseSalary(text):
    #от 150 000 руб. / до 150 000 руб.
    #60 000-150 000 руб.


    try:
        text = int(text.split()[1])*1000
        return text 
    except:
        text = text.split()
        leftVal = int(text[0])*1000
        rightVal = int(text[1].split('-')[1])*1000
        return int((rightVal+leftVal)/2)

