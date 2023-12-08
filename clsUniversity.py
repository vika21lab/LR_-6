import sqlite3


# создание класса БД
class University:
    # конструктор класса
    def __init__(self):

                # Подключение к БД
                self.con = sqlite3.connect("University.db")
                # Создание курсора
                self.cur = self.con.cursor()
                # Создание таблицы БД
                self.cur.execute(
                "CREATE TABLE IF NOT EXISTS University_s "
                "(ID INTEGER PRIMARY KEY,"
                "name_of_the_teacher TEXT,"
                "name_of_the_item TEXT,"
                "number_of_hours INTEGER,"
                "type_of_final_certification TEXT,"
                "audience_number INTEGER,"
                "date_of INTEGER,"
                "lessons  TEXT,"
                "group  TEXT)"

                )
               self.con.commit()

def __del__(self):
  # отключение от БД
  self.con.close()

def view(self):
  # просмотр всех записей в таблице БД
  self.cur.execute("SELECT * FROM University_s")
  # список всех записей из таблицы
  rows = self.cur.fetchall()
  return rows

def insert(self, name_of_the_teacher, name_of_the_item, number_of_hours,type_of_final_certification,audience_number,date_of,lessons,group ):
  # добавить запись
  self.cur.execute("INSERT INTO University_s "
                  "VALUES (NULL, ?, ?, ?,?,?,?,?,?)",
                  (name_of_the_teacher, name_of_the_item, number_of_hours,type_of_final_certification,audience_number,date_of,lessons,group ,))
  self.con.commit()

def update(self, id, name_of_the_teacher, name_of_the_item, number_of_hours,type_of_final_certification,audience_number,date_of,lessons,group ):
    # редактирование записи
    self.cur.execute("UPDATE University_s SET "
                    "name_of_the_teacher=?, name_of_the_item=?, number_of_hours=?,type_of_final_certification=?,audience_number=?,date_of=?,lessons =? ,group=? "
                    "WHERE ID = ?",
                    (name_of_the_teacher, name_of_the_item,
                    number_of_hours,type_of_final_certification,audience_number,date_of,lessons ,group, id,))
    self.con.commit()

def delete(self, id):
    # удаление записи
    self.cur.execute("DELETE FROM University_s "
                    "WHERE ID=?", (id,))
    self.con.commit()

def search(self, name_of_the_teacher):
    self.cur.execute("SELECT name_of_the_item, number_of_hours,type_of_final_certification,audience_number,date_of,lessons,group  FROM University_s "
                    "WHERE name_of_the_teacher=?", (name_of_the_teacher,))
    rows = self.cur.fetchall()
    return rows
