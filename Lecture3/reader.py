import sqlite3
import matplotlib.pyplot as plt 


conn = sqlite3.connect('vacancy.db')
cur = conn.cursor()


query_select = 'SELECT salary FROM vac'

salary_list = []

for row in cur.execute(query_select):
    salary_list.append(row[0])

plt.hist(salary_list, bins = 10, alpha = 0.5, color = "g")
plt.title('Vacancy  Salary Distribution')
plt.xlabel('Salary range')
plt.ylabel('Count Vacancy')
plt.savefig('result.png')
plt.grid(True)
plt.show()