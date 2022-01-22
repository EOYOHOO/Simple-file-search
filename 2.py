import os
import shutil

FILE_LIST = []


def D(path):
    file_list = []
    for file_path in os.listdir(path):
        file_path = os.path.join(path, file_path)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list


def D():
    print("DDD")


def R(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def A(path):
    for file in FILE_LIST:
        print(file)


def T(path):
    for file in FILE_LIST:
        try:
            with open(file, encoding='utf8') as fp:
                if fp.read().find(path) != -1:
                    print(file)
        except:
            pass


def N(path):
    for file in FILE_LIST:
        if file.find(path) != -1:
            print(file)


def E(path):
    for file in FILE_LIST:
        if file.endswith(path):
            print(file)


def UP(path):
    for file in FILE_LIST:
        size = os.path.getsize(file)
        if size > int(path):
            print(file)


def DOWN(path):
    for file in FILE_LIST:
        size = os.path.getsize(file)
        if size < int(path):
            print(file)


def F(path):
    print('This is a line of text')
    print('Hello, my name is Boo')


def D():
    for file in FILE_LIST:
        filePath = file + ".dup"
        shutil.copyfile(file, filePath)


def input_():
    cmd = input()
    if cmd in ['D', 'R']:
        path = os.getcwd()
    elif cmd in ['F']:
        path = ''
    cmd_tmp = cmd.split()
    if len(cmd_tmp) == 1:
        cmd = cmd_tmp[0]
    elif len(cmd_tmp) == 2:
        cmd = cmd_tmp[0]
        path = cmd_tmp[1]

    func = cmd_list.get(cmd, None)
    if func:
        return func, path


if __name__ == '__main__':
    cmd_list = {"D": D, "R": R, "A": A, "T": T, "N": N, "E": E, ">": UP, "<": DOWN, "F": F}
    level = 0
    while True:
        try:
            func, path = input_()
            if level < 2:
                file_list = func(path)
                level += 1
            else:
                file_list = func()
            if file_list != None:
                for file in file_list:
                    FILE_LIST.append(file)
                    print(file)
        except Exception as e:
            print(e)
            print('ERROR')


z