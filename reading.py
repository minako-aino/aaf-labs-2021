import re

# add "" support, and ignore ‘ ‘, ‘\t‘, ‘\r‘, ‘\n‘


def many_lines_input():
    contents = []
    while True:
        line = input()

        # if line[-1] == ";":
        #     break
        if line.find(";") != -1:
            line = line[:line.find(";")]
            contents.append(line)
            break
        else:
            contents.append(line)

    str1 = " ".join(contents)
    return " ".join(str1.split())
#
# print(many_lines_input())


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

# how to get token from string(column name, index)


def read_create(command):
    pattern = "(CREATE|create)\s[A-Za-z_\d]*\s\(([A-Za-z0-9_]*,?(\s(INDEXED|indexed),)?\s?)*\)"
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



_, names, name = read_create("CREATE cats (idgggggg, name, favourite_food indexed)")

print(read_create("CREATE cats (idgggggg, name, favourite_food indexed)"))
# print(re.sub(r"\([A-Za-z0-9,\s]*\)", ' ', "CREATE dogs (idggggggg, name, favourite_food indexed)"))
