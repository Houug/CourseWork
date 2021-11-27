import pyodbc
import pathlib
import eel
import datetime


@eel.expose
def add_new_person(surname, name, departament, start_vac, end_vac, salary, non18child):
    Data("db.accdb").add_new_person(surname + '\0',
                                    name + '\0',
                                    departament + '\0',
                                    start_vac,
                                    end_vac,
                                    salary,
                                    non18child)


@eel.expose
def create_new_table(name):
    Data("db.accdb").create_new_table(name)


@eel.expose
def del_from_db(id):
    Data("db.accdb").del_from_db(id)


@eel.expose
def load_db():
    loaded_db = list()
    for i in Data("db.accdb").load_db():

        temp = list(i)

        temp[4] = str(temp[4]).split(' ')[0]
        temp[5] = str(temp[5]).split(' ')[0]

        if temp[7]:
            temp[7] = "Есть"
        else:
            temp[7] = "Нет"

        loaded_db.append(temp)

    return loaded_db


class Data:
    def __init__(self, name: str):
        self._path = str(pathlib.Path().resolve()) + "\\" + name
        self._connect = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"f"DBQ={self._path};")
        self._cursor = self._connect.cursor()

    def create_new_table(self, name: str = "Main_Table") -> bool:
        if self._connect is not None:
            try:
                self._cursor.execute(f'''
                CREATE TABLE {name}(
                    ID COUNTER,
                    "Фамилия" CHAR(30),
                    "Имя" CHAR(30),
                    "Отдел" CHAR(30),
                    "Начало отпуска" DATE,
                    "Конец отпуска" DATE,
                    "Зарплата" INT,
                    "Дети до 18 лет" BIT);
                ''')
                self._cursor.commit()
                return True
            except:
                # print("Ошибка")
                return False

    def add_new_person(self, surname: str, name: str, departament: str, start_vac, end_vac, salary, non18child):
        self._cursor.execute(f'''
        INSERT INTO Main_Table(
        `Фамилия`,
        `Имя`,
        `Отдел`,
        `Начало отпуска`,
        `Конец отпуска`,
        `Зарплата`,
        `Дети до 18 лет`)
        VALUES(?,?,?,?,?,?,?);''', (surname.encode("utf-16"), name.encode("utf-16"), departament.encode("utf-16"), start_vac, end_vac, salary, non18child))
        self._cursor.commit()

    def del_from_db(self, id):
        self._cursor.execute(f'''DELETE * FROM Main_Table WHERE ID = {id}''')
        self._cursor.commit()

    def load_db(self):
        return self._cursor.execute('''SELECT * FROM Main_Table''').fetchall()
