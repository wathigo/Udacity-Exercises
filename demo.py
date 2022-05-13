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

connection.commit()
cursor.close()