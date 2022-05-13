import psycopg2

connection = psycopg2.connect('dbname=darkmode')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE  table1(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
);
''')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (1, true);')

connection.commit()
cursor.close()