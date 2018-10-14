"""Main module that runs the app. It's a simple command-line app for now"""

import os

from parse_input import parse
from crud import init, clean, insert, read_all, query


# === Defining Global Variables ===
db_name = "papercup_database.db"
session = init()


# === FUNCTIONS ====

def check_for_db(db):
    if not os.path.isfile(db):
        os.system("python create_database.py")
        print("Database created")
    else:
        print("Database file exists.")


def implement(name):

    if name == "init":
        clean(session)
        print("New database prepared.")

    elif name == "scan":
        print("Scan fuction TBD")

    elif name == "query":
        q = input("Title? ")
        content = query(session, q)
        if content:
            print(content["title"])
            print(content["content"])
            print("=====================")
        else:
            print("File not found.")

    elif name == "delete":
        print("Delete function TBD")

    elif name == "list_titles":
        print("list_titles function TBD")

    elif name == "show_all":
        read_all(session)

    elif name == "show":
        print("show function TBD")


def repl():

    ex = False

    while not ex:

        print("command> ", end="")
        cmd = input()
        tasks = parse(cmd)
        for t in tasks:
            if t == "exit":
                ex = True
            else:
                implement(t)

    print("Done")


# ==== RUN APP ===
repl()











