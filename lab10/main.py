import psycopg2
conn= psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                       password="dilnaz", port="5433")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS person(
   id INT PRIMARY KEY,
   name VARCHAR(500),
   phone INT,
   gender CHAR);
   """)
cur.execute("""INSERT INTO person (id, name, phone, gender) VALUES
            (1, 'Dilnaz', 87752, 'f'),
            (2, 'Naz', 87756, 'f'),
            (3, 'Arai', 87773, 'f'),
            (4, 'Ilyas', 877542, 'm'),
            (5, 'Ayan', 87016, 'm')""")
cur.execute("""SELECT * FROM person WHERE gender = 'm'; """)
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()