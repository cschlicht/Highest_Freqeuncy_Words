import psycopg2

#TO USE - Run pgAdmin4


# Steps for connecting to a database
# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL Query
# 4. Commit changes 
# 5. Close database connection

def create_table():
    conn = psycopg2.connect("dbname='article_words' user = 'postgres' password = 'database123' host = 'localhost' port = '5432' " )

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS words (word TEXT)")
    

    conn.commit()
    conn.close()

def insert(word): 
    conn = psycopg2.connect("dbname='article_words' user = 'postgres' password = 'database123' host = 'localhost' port = '5432' " )
    cur = conn.cursor()
    cur.execute("INSERT INTO words VALUES (%s)", (word,))
    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect("dbname='article_words' user = 'postgres' password = 'database123' host = 'localhost' port = '5432' " )
    cur = conn.cursor()
    cur.execute("SELECT * FROM words")
    rows = cur.fetchall()
    
    conn.close()
    return rows

def viewOccurences():
    conn = psycopg2.connect("dbname='article_words' user = 'postgres' password = 'database123' host = 'localhost' port = '5432' " )
    cur = conn.cursor()
    cur.execute("SELECT word, COUNT(*) FROM words GROUP BY word")
    rows = cur.fetchall()
    
    conn.close()
    return rows

def deleteAll():
    conn = psycopg2.connect("dbname='article_words' user = 'postgres' password = 'database123' host = 'localhost' port = '5432' " )
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE words")
    conn.commit()
    conn.close()






create_table() #create table, if table already exists, this does nothing
#delete("Glass Bottle")
#updateQuantity(15, "Glass Bottle")
#print(viewOccurences())

#print(deleteAll())s
#print(viewOccurences())