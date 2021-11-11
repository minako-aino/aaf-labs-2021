from table import *


class DB:

    def __init__(self):
        self.tables = []

    def create(self, table_name, col_dict):
        if col_dict:
            for i in self.tables:
                if i.table_name == table_name:
                    print("table already exist")
                    break
            else:
                table = Table()
                table.create(table_name, col_dict)
                self.tables.append(table)
        else:
            print("give a column name")

    def insert(self, table_name, value):
        for table in self.tables:
            if table.table_name == table_name:
                table.insert(value)
                break
            else:
                print("table not exist")

    def select(self, table_name, col_name, cond=None):
        if cond:
            pass
        else:
            if col_name == ["*"]:
                for table in self.tables:
                    if table.table_name == table_name:
                        table.select()
                        break

    def delete(self, table_name, cond=None):
        if cond:
            pass
        else:
            for table in self.tables:
                if table.table_name == table_name:
                    print(f"table {table.table_name} was dropped")
                    self.tables.pop(self.tables.index(table))
                    break

# db = DB()
# db.create("create dog(ff,aaa)")
# db.insert("dogs", ["s",'ff'])
# db.insert("dogs", ["s",'ff'])
# db.insert("dogs", ["s",'ff'])
# db.select("dogs", ["*"], )
# db.delete("dogs")

# create dog(ff,aaa);
# Table dog has been created
# insert into dog("sss","shiba);
# insertion failed
# insert into dog("sss","shiba';
# invalid command
# insert into dog("sss","shiba");
# invalid command