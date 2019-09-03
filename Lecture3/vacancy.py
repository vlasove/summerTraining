import sqlite3

class Vacancy:
    def __init__(self,request, title, company, salary):
        self.request = request
        self.title = title
        self.company = company
        self.salary = salary 

    def save_to_db(self):
        conn = sqlite3.connect('vacancy.db')
        cur = conn.cursor()

        query_create = "CREATE TABLE IF NOT EXISTS vac (request TEXT,title TEXT, company TEXT, salary INT)"
        cur.execute(query_create)

        query_insert = "INSERT INTO vac VALUES(?,?,?,?)"
        data = (self.request, self.title, self.company, self.salary)
        cur.execute(query_insert, data)


        conn.commit()
        conn.close()

    def salaryParse(self):
        try:
            self.salary = int(self.salary.split()[1])*1000
        except:
            text = self.salary.split()
            leftVal = int(text[0])*1000
            rightVal = int(text[1].split('-')[1])*1000
            self.salary =  int((rightVal+leftVal)/2)



