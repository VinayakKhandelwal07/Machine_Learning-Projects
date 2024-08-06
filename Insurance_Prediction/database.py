import sqlite3
conn = sqlite3.connect("userdata.db")

create_table_query = """
create table User_record (age integer,bmi ,child integer,gender integer,smoker integer,northwest integer,
                        southeast integer,southwest integer,predictation integer,date varchar(15),time varchar(15))
"""

cur = conn.cursor() # temprory memory
cur.execute(create_table_query)
print("Table created !")
cur.close()
conn.close()