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
        for table in self.tables:
            if table.table_name == table_name:
                if cond:
                    pass
                else:
                    table.select(col_name)
                    break
            else:
                print("table not exist")

    def delete(self, table_name, cond=None):
        if cond:
            pass
        else:
            for table in self.tables:
                if table.table_name == table_name:
                    print(f"table {table.table_name} was dropped")
                    table.value.clear()
                    break

# db = DB()
# db.create("dogs", ['s', 'ff', 'aaa'])
# db.insert("dogs", ["s1", 'ff1', 'aaa1'])
# db.insert("dogs", ["s2", 'ff2', 'aaa2'])
# db.insert("dogs", ["s3", 'ff3', 'aaa3'])
# db.select("dogs", ["*"])
# db.select("dogs", ["aaa", "ff"])
# db.select("dogs", ["aaa", "ff", "ff333"])
# db.delete("dogs")
# db.select("dogs", ["*"])
# create dog(ff,aaa);
# Table dog has been created
# insert into dog("sss","shiba);
# insertion failed
# insert into dog("sss","shiba';
# invalid command
# insert into dog("sss","shiba");
# invalid command