import re

# add "" support, and ignore ‘ ‘, ‘\t‘, ‘\r‘, ‘\n‘


def many_lines_input():
    contents = []
    while True:
        line = input()

# end with ;
        if line.find(";") != -1:
            line = line[:line.find(";")]
            contents.append(line)
            break
        else:
            contents.append(line)
# spaces del
    str1 = " ".join(contents)
    return " ".join(str1.split())
#
# print(many_lines_input())

# help func to
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""




def read_create(command):
    pattern = "(CREATE|create)\s[A-Za-z_\d]+\s\(([A-Za-z0-9_]+,?(\s(INDEXED|indexed),)?\s?)+\)"
    if re.match(pattern, command):
        table_name = command.split()[1]
        columns_name = find_between(command, "(", ")").split(", ")
        indexation = {}
        for name in columns_name:
            if re.search(r"INDEXED|indexed", name):
                indexation[name] = 1
            else:
                indexation[name] = 0

    else:
        print("invalid syntax")
    return table_name, columns_name, indexation



# _, names, name = read_create("CREATE cats (idgggggg, name, favourite_food indexed)")

# print(read_create("CREATE cats (idgggggg, name, favourite_food indexed)"))
# print(re.sub(r"\([A-Za-z0-9,\s]*\)", ' ', "CREATE dogs (idggggggg, name, favourite_food indexed)"))


def read_insert(command):
    pattern = "(INSERT|insert)\s((INTO|into)\s)?[A-Za-z_\d]+\s\(([\"A-Za-z\d],?\s?)+\)"
    if re.match(pattern, command):
        command_name = command.split()[0]
        insert_data = find_between(command, "(", ")").split(", ")
        for data in range(len(insert_data)):
            insert_data[data] = find_between(insert_data[data], "\"", "\"")
        print("ok")
        return command_name, insert_data
    else:
        print("wrong input")

name, data = read_insert("INSERT cats (\"2\", \"Pushok\", \"Fish\")")

print(name, data)


