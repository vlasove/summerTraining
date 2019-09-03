import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS user (name TEXT, year INT, id INT)"
cur.execute(query_create)

insert_static = "INSERT INTO user VALUES('Evgeny', 23, 81)"
#cur.execute(insert_static)
#conn.commit()

insert_dynamic = "INSERT INTO user VALUES(?, ?, ?)"
params = ('Stas', 45, 1234)
#cur.execute(insert_dynamic, params)
#conn.commit()

query_select = "SELECT * FROM user WHERE year > 32 OR id < 2000"


query_update = "UPDATE user SET name = 'Sergey' WHERE year > 40"
cur.execute(query_update)
conn.commit()



query_delete = "DELETE FROM user WHERE name = 'Sergey'"
cur.execute(query_delete)
conn.commit()

for row in cur.execute(query_select):
    print(row)

conn.close()

