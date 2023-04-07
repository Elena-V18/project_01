# Создадим таблицу STUDENT

# import sqlite3
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE STUDENT (
# Student_Id INTEGER NOT NULL PRIMARY KEY,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# Наполним таблицу STUDENT

# import sqlite3
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO STUDENT (Student_Id, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# Написать программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

def get_student(student_id):
  try: 
    # если переменную schol_id не обозначаю, выходит ошибка, если ввожу числа от 1 до 4,
    # т.е. id, то независимо от выбора числа, выводит нормально. Подскажите, как написать правильно!!!
    school_id = 1    
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = """SELECT * FROM Student WHERE Student_Id = ?"""
    cursor.execute(sql_select_query, (student_id,))
    records = cursor.fetchall()
    print ("Студенты из школы", school_name)
    for row in records:
      print ("ID Студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", school_name)
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Вывести список о школе и студенте по ID студента \n")
get_student(203)

