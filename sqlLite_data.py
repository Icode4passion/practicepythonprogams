import sqlite3

def create_table():
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER , price REAL)') 
	cur.execute('INSERT INTO store VALUES ("Wine",8,10.25)')
	conn.commit()
	conn.close

def insert(item,quantity,price):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute('INSERT INTO store VALUES (?,?,?)',(item,quantity,price))
	conn.commit()
	conn.close

#insert('Milk',6,7.5)

def view():
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute('SELECT * FROM store')
	rows = cur.fetchall()
	return rows


def delete(item):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	#cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER , price REAL)') 
	#cur.execute('INSERT INTO store VALUES ("Wine",8,10.25)')
	cur.execute("DELETE FROM store WHERE item = ?",(item,))
	conn.commit()
	conn.close


delete('Wine')
print view()
#insert('Tea',28,1.75)