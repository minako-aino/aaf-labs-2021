from db import *
from parser2 import *


def process():
    while True:
        try:
            command = parse666()
            if command == ".EXIT":
                break
            else:
                if command[0][1] == "T_CREATE":
                    db.create(command[1], command[2])
                elif command[0][1] == "T_INSERT":
                    db.insert(command[1], command[2])
                elif command[0][1] == "T_SELECT":
                    if len(command) == 3:
                        db.select(command[1], command[2])
                    elif len(command) == 4:
                        db.select(command[1], command[2], command[3])
                elif command[0][1] == "T_DELETE":
                    if len(command) == 3:
                        db.delete(command[1], command[2])
                    elif len(command) == 2:
                        db.delete(command[1])
                else:
                    process()
                    print("error")
        except:
            process()


if __name__ == '__main__':
    db = DB()
    process()

# db = DB()
# print(all_parse("create t (a,b,c)"))
# db.create('t', ['a', 'b', 'c'])
# db.insert('t', ['aa','bb', 'cc'])
# db.insert('t', ['aaa','bbb', 'ccc'])
# print(all_parse("select * from t"))
# db.select('t', ["*"])
# print(all_parse("select c, a from t"))
# db.select('t', ['c','a'])

# db.select('t', ["*"])
