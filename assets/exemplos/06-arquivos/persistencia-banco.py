import sqlite3

def persistir():
    conn = sqlite3.connect('banco.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS pessoa
                 (id int, nome text, idade int)''')

    c.execute("INSERT INTO pessoa VALUES (2,'Diego',30)")

    conn.commit()
    conn.close()

def ler():
    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    id = '2'
    c.execute('SELECT * FROM pessoa WHERE id=?', id)
    print(c.fetchone())

ler()



