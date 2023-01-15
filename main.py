import sqlite3
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people(name TEXT, age INTEGER, skills STRING)")
except Exception as e:
    pass

def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True

def insert_db():
    name = input("Name >>")

    if user_is_unique(str(name)):
        age = input("Age >>")
        skills = input("Skills >")

        if name != "" and age != "" and skills != "":
            cursor.execute(f"INSERT INTO people VALUES('{name}', '{age}', '{skills}')")
            connection.commit()
            print(name + "has been added to the database")

        else:
            print("one of the field is empty , try again")
            insert_db()
    else:
        ("name already in database")

def edit_db():
    name = input("type name of person to edit")
    field = input("enter field to edit")
    updated_field = input("enter field to update")

    try:
        cursor.execute(f"UPDATE people SET {field} = ? WHERE name = ?", (updated_field, name))
        connection.commit()
        print("succes to create user")
    except Exception as e:
        print(e)
        
def get_user_info_db():
    target_name = input("who you want to se information")
    rows = cursor.execute("SELECT name, age, skills FROM people WHERE name = ?" (target_name),).fetchall()

    name = rows [0][0]       
    age = rows [0][1]       
    skills = rows [0][2]

    print(f"{name} is {age} years old, and works as a {skills}.")

def delete_db():
    name = input("name person to delete from db")
    if name != "":
        cursor.execute("DELETE FROM people WHERE name = ?", (name,))
        connection.commit()
        print("user deleted")

def display_db():
    rows = cursor.execute("SELECT name, age, skills FROM people ORDER BY name ASC").fetchall()

    print("users: ")
    for user in rows:
        print(f"- {user[0]} - {user[1]} - {user[2]}")


def exit_db():
    cursor.close()
    connection.close()
    sys.exit()

def select_options():
    options = input("""
    --------------------------------
    Type '0' to exit
    Type '1' to insert a new user
    Type '2' to display users
    Type '3' to delete user
    Type '4' to edit user
    Type '5' to get user information
    ----------------------------------
    """) 
    if options == "0":
        exit_db()                              
    if options == "1":
        insert_db()                              
    if options == "2":
        display_db()                              
    if options == "3":
        delete_db()                              
    if options == "4":
        edit_db()                              
    if options == "5":
        get_user_info_db()

while True:
    select_options()                                      
