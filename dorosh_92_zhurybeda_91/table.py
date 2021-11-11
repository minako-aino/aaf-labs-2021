from tabulate import tabulate
# from tree import *


class Table:
    def __init__(self):
        self.table_name = None
        self.col_name = None
        self.value = []

    def create(self, table_name, col_dict):
        self.table_name = table_name
        self.col_name = col_dict
        print(f'Table {self.table_name} has been created')

    def insert(self, value):
        if len(value) == len(self.col_name):
            self.value.append(value)
            print(f'1 row has been inserted into {self.table_name}.')
        else:
            print("insertion failed")

    def select(self):
        print(tabulate(self.value, headers=self.col_name, tablefmt='orgtbl'))

# table = Table()
# table.create(1, ["name","name2","name1"])
# table.insert(["nam","nam2","nam1"])
# table.insert(["namq","namq2","namq1"])
# table.select()
#
# # print(table.value[0][0])
#
#
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(15)
# root.print_tree()
