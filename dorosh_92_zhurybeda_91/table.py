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

    def select(self, col_name):
        if col_name == ['*']:
            print(tabulate(self.value, headers=self.col_name, tablefmt='grid'))
        elif set(self.col_name) >= set(col_name):
            icol = []
            for i in range(len(col_name)):
                for j in range(len(self.col_name)):
                    if self.col_name[j] == col_name[i]:
                        icol.append(j)
            value = []
            for ind in icol:
                temp = []
                for i in self.value:
                    temp.append(i[ind])
                value.append(temp)
            value = list(map(list, zip(*value)))
            print(tabulate(value, headers=col_name, tablefmt='grid'))
        else:
            print("column not exist")


# table = Table()
# table.create("dogs", ['s', 'ff', 'aaa'])
# table.insert(["s1", 'ff1', 'aaa1'])
# table.insert(["s2", 'ff2', 'aaa2'])
# table.insert(["s3", 'ff3', 'aaa3'])
# table.select(["*"])
# table.select(["aaa", "ff"])
# db.delete("dogs")



