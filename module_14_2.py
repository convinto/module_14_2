import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)  
''')

#Заполните её 10 записями:
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# i=-1
# while i < 10:
#     i+=2
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
# i=-2
# while i < 10:
#     i+=3
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))


#######################################################################################################################
#Удалите из базы данных not_telegram.db запись с id = 6.
#cursor.execute("DELETE FROM Users WHERE id = ?", (6,))


#Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]


#Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]


#Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")        #получить средний
avg_balance = cursor.fetchone()[0]
print(avg_balance)

print(all_balances / total_users)   #Вывести в консоль средний баланс всех пользователей (альтернативный вариант)

# connection.commit()
connection.close()