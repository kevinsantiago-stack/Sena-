# kevin santiago larrota cuervo
import sqlite3

def main():
    conn = sqlite3.connect('data/database.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)')
    cur.execute('INSERT INTO productos (nombre, precio) VALUES (?,?)', ('Camiseta', 29.99))
    conn.commit()
    cur.execute('SELECT id, nombre, precio FROM productos')
    for row in cur.fetchall():
        print(row)
    conn.close()

if __name__ == '__main__':
    main()
