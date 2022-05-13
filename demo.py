import psycopg2

connection = psycopg2.connect('dbname=darkmode')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
CREATE TABLE  table1(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
);
''')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);', (1, True))

query = 'INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 2,
    'completed': False
}
cursor.execute(query, data)
cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);', (3, True))

cursor.execute('SELECT * FROM table1')

results1 = cursor.fetchmany(2)
print('fetchmany(2)', results1)

results2 = cursor.fetchone()
print('fetchone()', results2)

results3 = cursor.fetchone()
print('fetchone()', results3)

cursor.execute('SELECT * FROM table1')

results4 = cursor.fetchone()
print('fetchone()', results4)

connection.commit()
cursor.close()