import sqlite3

conn=sqlite3.connect("sherlock.db")
cursor=conn.cursor()

query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path varchar(1000))"
cursor.execute(query)

query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url varchar(1000))"
cursor.execute(query)



# query="INSERT INTO sys_command VALUES(null,'obs','C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe')"
# cursor.execute(query)
# conn.commit()

# query="INSERT INTO web_command VALUES(null,'whatsapp web','https://web.whatsapp.com/')"
# cursor.execute(query)
# conn.commit()

# query="DELETE FROM web_command WHERE name='Whatsapp web'"
# cursor.execute(query)
# conn.commit()

# app_name="obs"
# cursor.execute('SELECT path FROM sys_command WHERE name IN(?)',(app_name,))
# results=cursor.fetchall()
# print(results[0][0])



