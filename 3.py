import os
from pathlib import Path
import shutil
import re

def inPut():
    global X
    while (True):
        command = input(r'').split()
        if (len(command) == 2):
            if ((command[0] == 'R' or 'D') and os.path.exists(command[1])):
                all_file(command[1], command[0])
                for PATH in PATH_1:
                    print(PATH)
                X = X + 1
                break
            elif (command[0] == 'N' or command[0] == 'E' or command[0] == 'T' or command[0] == '>' or command[0] == '<'):
                cmd(command[0], F, command[1])
                for PATH in PATH_2:
                    print(PATH)
                X = X + 1
                break
            else:
                print('ERROR')
        elif (len(command) == 1):
            if ((command[0] == 'F' or command[0] == 'D' or (command[0] == 'T' and X==2))):
                cmd(command[0], F)
                break
            elif (command[0] == 'A'):
                cmd(command[0], F)
                for PATH in PATH_2:
                    print(PATH)
                break
            else:
                print('ERROR')
        else:
            print('ERROR')


def all_file(path, letter) -> None:
    if (letter == "D"):
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filenames:
                F.append(name)
                PATH_1.append(os.path.join(dirpath, name))
            break
    if (letter == "R"):
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filenames:
                F.append(name)
                PATH_1.append(os.path.join(dirpath, name))


def cmd(letter, files=True, values=True) -> None:
    i = 0
    if (letter == 'A'):
        for filename in files:
            PATH_2.append(PATH_1[i])
            i = i + 1
    elif (letter == 'N'):
        for filename in files:
            if (values == filename):
                PATH_2.append(PATH_1[i])
                i = i + 1
            else:
                i = i + 1
    elif (letter == 'E'):
        for filename in files:
            (filename, postfix) = os.path.splitext(filename)
            extension = '.' + values
            if (postfix == extension):
                PATH_2.append(PATH_1[i])

                i = i + 1
            else:
                i = i + 1
    elif (letter == 'T' and X==2):
        for PATH in PATH_2:
            os.utime(PATH, None)
    elif (letter == 'T'):
        for filename in files:
            (filename, postfix) = os.path.splitext(filename)
            if (postfix == '.txt'):
                if values in open(PATH_1[i], "r", encoding="utf8").read():
                    PATH_2.append(PATH_1[i])
                i = i + 1
            else:
                #print('ERROR')
                i = i + 1
    elif (letter == '<'):
        x = int(values)
        for file_path in PATH_1:
            file_stats = os.stat(file_path)
            if (file_stats.st_size <= x):
                PATH_2.append(file_path)
    elif (letter == '>'):
        x = int(values)
        for file_path in PATH_1:
            file_stats = os.stat(file_path)
            if (file_stats.st_size >= x):
                PATH_2.append(file_path)
    elif (letter == 'F'):
        for filename in PATH_2:
            #print(filename)
            (filename, postfix) = os.path.splitext(filename)
            if (postfix == '.txt'):
                file = open(PATH_2[i], 'r', encoding="utf8", newline=None)
                txt = file.readlines()
                print(txt[0].strip())
                i = i + 1
            else:
                print("NOT TEXT")
                i = i + 1
    elif (letter == 'D'):
        for PATH in PATH_2:
            shutil.copy(PATH, PATH + ".dup")

def main():
    for i in range(0, 3):
        inPut()


if __name__ == '__main__':
    X = 0
    PATH_1 = []
    PATH_2 = []
    F = []
    main()