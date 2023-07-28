import psycopg2

try:
    con = psycopg2.connect(
        user="sameer",
        password="sameer",
        host="localhost",    # Use "localhost" if the database is on your local machine
        port=5432,    # Usually 5432 is the default port for PostgreSQL
        dbname="practice"
    )
    print("Connected to the PostgreSQL database!")

    cur = con.cursor()

    select_query = "SELECT * FROM employees;"

    insert_query = "INSERT INTO employees (id,name,emp_id,dept) VALUES (21,'Sameer','emp021','it');"

    cur.execute(select_query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    #con.commit()

    #print("Data inserted succesfully!!!")

    cur.close()
    con.close()
        

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)
