import  sqlite3
import pandas as pd

with open("./create_user_table.sql") as f:
    create_table_statement = f.read()

with open("./insert_into_user_table.sql") as f:
    insert_statement = f.read()

print(create_table_statement)
print(insert_statement) 


print("opening connection")

conn = sqlite3.Connection("./data/mydb.sqlite")

print("creating table")
conn.execute(create_table_statement)

print("inserting data into users table")
conn.execute(insert_statement)


print("fetching all users")

df = pd.read_sql(con=conn,
                 sql = "select * from users;")

print(df)

conn.close()



print("connection closed, finished")