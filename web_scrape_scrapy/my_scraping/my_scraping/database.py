import sqlite3 as sql

conn = sql.connect("my_scraping_database.db")
cursor = conn.cursor()

try:
    cursor.execute("""create table if not exists mydata_tb(id integer primary key, book_title text, book_price float)""")
    conn.commit()

except:
    pass

def insert_record(cursor, title, price):
    cursor.execute("""insert into mydata_tb(book_title,book_price) values (?,?)""", (title,price))
    conn.commit()


if __name__=="__main__":

    insert_record(cursor,"Python book", 3006)

    conn.close()

