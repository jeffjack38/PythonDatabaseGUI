from assignment2 import create_db
from assignment2 import write_db
import tkinter

def create_steudent_and_person_table():
    create_db.create_tables('gui-db.db')

def insert_person():
    #TODO: how to get user input for first name, last name

    #end TODO
    conn = write_db.create_connection("gui-db.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = create_person(conn, person)

write_db.create_person(conn, person)
m = tkinter.Tk()

m.title('Students and persons database')
label = tkinter.Label
label.grid

