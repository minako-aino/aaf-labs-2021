from tabulate import tabulate
from tree import *
import re

class Table:
    def __init__(self):
        self.table_name = None
        self.col_name = None
        self.value = {}
        self.tree = {}
        self.index = {}

    def create(self, table_name, col_dict):
        self.table_name = table_name
        self.col_name = list(col_dict.keys())
        for name in col_dict.keys():
            if col_dict[name] == 1:
                self.tree[name] = Node((None, None))
                self.index[name] = list(col_dict.keys()).index(name)
        print(f'Table {self.table_name} has been created')

    def insert(self, value):
        if len(value) == len(self.col_name):
            length = len(self.value)
            self.value[length] = value
            if self.tree:
                for name in self.tree:
                    self.tree[name].insert((length, list(self.value.items())[length][1][self.index[name]]))
            print(f'1 row has been inserted into {self.table_name}.')
        else:
            print("insertion failed")

    def simple_select(self, col_name):
        if col_name == ['*']:
            print(tabulate(self.value.values(), headers=self.col_name, tablefmt='grid'))
        elif set(self.col_name) >= set(col_name):
            icol = []
            for i in range(len(col_name)):
                for j in range(len(self.col_name)):
                    if self.col_name[j] == col_name[i]:
                        icol.append(j)
            value = []
            # for ind in icol:
            #     temp = []
            #     for i in self.value:
            #         temp.append(i[ind])
            #     value.append(temp)
            # value = list(map(list, zip(*value)))
            for row in self.value.values():
                temp = []
                for i in icol:
                    temp.append(row[i])
                value.append(temp)
            print(tabulate(value, headers=col_name, tablefmt='grid'))
        else:
            print("column not exist")

    def cond_calc(self, cond):
        stack = []
        if cond == 3:
            for i in cond:
                if i in ["<", "=", ">", ">=", "<="]:
                    value = stack.pop()
                    if value in self.index.keys():
                        col_name = stack.pop()
                        stack.append(index_op(self, i, col_name, value))
                    else:
                        col_name = stack.pop()
                        stack.append(apply_arith_op(self, i, col_name, value))
                else:
                    stack.append(i)
        else:
            for i in cond:
                if i in ["<", "=", ">", ">=", "<="]:
                    value = stack.pop()
                    col_name = stack.pop()
                    stack.append(apply_arith_op(self, i, col_name, value))
                elif re.match(r'(?i)or', i) or re.match(r'(?i)and',i):
                    tbl1 = stack.pop()
                    tbl2 = stack.pop()
                    stack.append(apply_set_op(i, tbl1, tbl2))
                else:
                    stack.append(i)
            res_table = stack.pop()
        return res_table

    def cond_select(self, col_name, cond):
        if col_name == ["*"]:
            res_table = self.cond_calc(cond)
            print(tabulate(res_table.values(), headers=self.col_name, tablefmt='grid'))
        elif set(self.col_name) >= set(col_name):
            res_table = self.cond_calc(cond)
            icol = []
            for i in range(len(col_name)):
                for j in range(len(self.col_name)):
                    if self.col_name[j] == col_name[i]:
                        icol.append(j)
            value = []
            for row in res_table.values():
                temp = []
                for i in icol:
                    temp.append(row[i])
                value.append(temp)
            print(tabulate(value, headers=col_name, tablefmt='grid'))
        else:
            print("column not exist")


    def delete_rows(self, cond):
        rows_ind = list(self.cond_calc(cond).keys())
        for ind in rows_ind:
            self.value.pop(ind)
        self.value = {i: v for i, v in enumerate(self.value.values())}
        print(f"{len(rows_ind)} rows have been deleted from the table_name table")

def index_op(table, op, col_name, value):
    if op == '=':
        ind = table.tree[col_name].search(value)
        temp = {}
        for i in ind:
            temp[i] = table.value[i]
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '>':
        temp = {}
        _, _, ind = table.tree[col_name].greater(value)
        for i in ind:
            temp[i] = table.value[i]
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '>=':
        temp = {}
        _, _, ind = table.tree[col_name].greater(value, eq=True)
        for i in ind:
            temp[i] = table.value[i]
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '<':
        temp = {}
        _, _, ind = table.tree[col_name].smaller(value)
        for i in ind:
            temp[i] = table.value[i]
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '<=':
        temp = {}
        _, _, ind = table.tree[col_name].smaller(value, eq=True)
        for i in ind:
            temp[i] = table.value[i]
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp



def apply_arith_op(table, op, col_name, value):
    if op == '=':
        temp = {}
        ind = table.col_name.index(col_name)
        for key, row in table.value.items():
            if row[ind] == value:
                temp[key] = row
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '>':
        temp = {}
        ind = table.col_name.index(col_name)
        for key, row in table.value.items():
            if row[ind] > value:
                temp[key] = row
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '>=':
        temp = {}
        ind = table.col_name.index(col_name)
        for key, row in table.value.items():
            if row[ind] >= value:
                temp[key] = row
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '<':
        temp = {}
        ind = table.col_name.index(col_name)
        for key, row in table.value.items():
            if row[ind] < value:
                temp[key] = row
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp
    elif op == '<=':
        temp = {}
        ind = table.col_name.index(col_name)
        for key, row in table.value.items():
            if row[ind] <= value:
                temp[key] = row
        # print(temp)
        # print(tabulate(list(temp.values()), headers=table.col_name, tablefmt='grid'))
        return temp


def apply_set_op(op, table1, table2):
    if re.match(r'(?i)or', op):
        table1.update(table2)
        res = dict(sorted(table1.items()))
        return res
    elif re.match(r'(?i)and', op):
        res = {}
        unique_key = list(set(table1.keys()) & set(table2.keys()))
        table1.update(table2)
        for key in unique_key:
            res[key] = table1[key]
        res = dict(sorted(res.items()))
        return res

# table = Table()
# table.create("dogs", {'s': 0, 'ff': 1, 'aaa': 1})
# table.insert(["s1", 'ff2', 'aaa1'])
# table.insert(["s2", 'ff2', 'aaa2'])
# table.insert(["nnn1", 'ff2', 'aaa1'])
# table.insert(["s3", 'f', 'aaa3'])
# table.insert(["nnn1", 'fr1', 'aaa1'])
# table.insert(["s3", 'ff2', 'aaa3'])
# table.tree["ff"].PrintTree()
# print(table.index["ff"])
# table.simple_select(["*"])
# table.delete_rows(['aaa', 'aaa1', "="])
# table.simple_select(["*"])
# table.cond_select(["*"], ['ff', 'ff2', "="])
# print(table.cond_calc(['ff', 'ff2', "="]))
# print(table.value)
# print(table.tree)
# print(table.index)
# table1 = apply_arith_op(table, "=", "aaa", "aaa1")
# table2 = apply_arith_op(table, "<", "ff", "ff2")
# print(table1)
# print(table2)
# print(apply_set_op("OR", table1, table2))

# table.apply_set_op("OR", [[1,2,3], [1,2,3], [1,2,3]], [[1,2,2], [1,2,4], [1,2,3]])
# table.simple_select(["aaa", "ff", "ff"])
# db.delete("dogs")
# print(index_op(table, '<', "ff", "ff2"))