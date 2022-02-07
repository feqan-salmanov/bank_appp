import psycopg2

con = psycopg2.connect(
    user="postgres",
    password="feqan3.0",
    database="db_01",
    host="127.0.0.1",
    port="5432"
)
cursor = con.cursor()

update_sql = """update account set name = %s where id =%s returning id"""

cursor.execute(update_sql, ('feqan111', 2))

update_id = cursor.fetchone()[0]

print(update_id)

insert_sql = """insert into account (name, surname, age) values (%s, %s, %s) returning id"""

cursor.execute(insert_sql, ('feqan', 'salmanov', 44))

insert_id = cursor.fetchone()[0]
con.commit()

print(insert_id)

