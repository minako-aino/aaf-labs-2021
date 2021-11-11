from db import *
from parser2 import *

def process():
    db = DB()
    try:
        while True:
            command = parse666()
            if command == ".EXIT":
                break
            else:
                if command[0][1] == "T_CREATE":
                    db.create(command[1], command[2].keys())
                elif command[0][1] == "T_INSERT":
                    db.insert(command[1], command[2])
                elif command[0][1] == "T_SELECT":
                    db.select(command[1], command[2])
                elif command[0][1] == "T_DELETE":
                    if len(command) == 3:
                        db.delete(command[1], command[2])
                    elif len(command) == 2:
                        db.delete(command[1])
                else:
                    print("error")
    except:
        process()
if __name__ == '__main__':
    process()



