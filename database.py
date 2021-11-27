import pyodbc
import pathlib
import eel
import datetime


@eel.expose
def add_new_person(surname, name, departament, start_vac, end_vac, salary, non18child):
    Data("db.accdb").add_new_person(surname, name, departament, start_vac, end_vac, salary, non18child)


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
        print(i.__str__().encode("ascii", 'ignore'))
        if type(i) == datetime.datetime:
            loaded_db.append(i.__str__().split(' ')[0])
        else:
            loaded_db.append(str(i).split('  ')[0])
        '''
        start_vac: datetime.date = i[4]
        end_vac: datetime.date = i[5]
        person = {
            "ID": i[0],
            "Фамилия": i[1],
            "Имя": i[2],
            "Отдел": i[3],
            "Начало отпуска": str(start_vac).split(" ")[0],
            "Конец отпуска": str(end_vac).split(" ")[0],
            "Зарплата": i[6],
            "Дети до 18 лет": i[7]
        }
        loaded_db.append(person)
        '''
    return loaded_db


class Data:
    def __init__(self, name: str):
        self._path = str(pathlib.Path().resolve()) + "\\" + name
        self._connect = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"f"DBQ={self._path};")
        self._cursor = self._connect.cursor()

    def create_new_table(self, name: str = "Main_Table") -> bool:
        if self._connect is not None:
        #    try:
                self._cursor.execute(f'''
                CREATE TABLE {name}(
                    ID COUNTER,
                    "Фамилия" CHAR,
                    "Имя" CHAR,
                    "Отдел" CHAR,
                    "Начало отпуска" DATE,
                    "Конец отпуска" DATE,
                    "Зарплата" INT,
                    "Дети до 18 лет" BIT);
                ''')
                self._cursor.commit()
                return True
 #           except:
  #              print("Ошибка")
   #             return False

    def add_new_person(self, surname:str, name, departament, start_vac, end_vac, salary, non18child):
        self._cursor.execute(f'''
        INSERT INTO Main_Table(
        `Фамилия`,
        `Имя`,
        `Отдел`,
        `Начало отпуска`,
        `Конец отпуска`,
        `Зарплата`,
        `Дети до 18 лет`)
         VALUES(?,?,?,?,?,?,?);''', (surname.encode("utf-16"), name+'\0', departament+'\0', start_vac+'\0', end_vac+'\0', salary, non18child))
        self._cursor.commit()

    def del_from_db(self, id):
        self._cursor.execute(f'''DELETE * FROM Main_Table WHERE ID = {id}''')
        self._cursor.commit()

    def load_db(self):
        return self._cursor.execute('''SELECT * FROM Main_Table''').fetchall()
