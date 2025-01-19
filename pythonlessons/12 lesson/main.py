import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Posts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
userid INTEGER NOT NULL,
post TEXT NOT NULL,
FOREIGN KEY (userid) REFERENCES Users (id)
)""")




def add_to_users(items) :
    cat = "INSERT INTO Users VALUES (null,'" + items[0] + "','" + items[1] + "'," + str(items[2]) + ')'
    cursor.execute(cat)

def add_post(items) :
    cat = "INSERT INTO Posts VALUES (null," + str(items[0]) + ",'" + items[1] + "')"
    cursor.execute(cat)

# add_to_users(("misha1","nmjs@1", 671))
# add_to_users(("misha2","nmjs@2", 672))
# add_to_users(("misha3","nmjs@3", 673))
add_post((1,'wliuytresx'))



# cursor.execute("""
# INSERT INTO Users VALUES (
# 456789,'masha','cat@',46
# )""")

cursor.execute("""
SELECT * FROM Posts WHERE userid = 1
""")

posts = cursor.fetchall()
print(posts)

for x in posts :
    print(x[2])



connection.commit()

connection.close()