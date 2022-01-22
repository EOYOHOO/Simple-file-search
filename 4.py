import os
import re
from pathlib import Path
import shutil
cmd_list = ["D", "R" , "A" , "T" , "N" , "E" , ">" ,"<" , "F" , "D" , "T"]

def cmdin():
    global X
    Flag = True
    while (Flag):
        C = input(r'').split()
        #print(C)
        if((C[0]==cmd_list[0] or C[0]==cmd_list[1]) and (X==0) and len(C)==2):
            if(os.path.exists(C[1])):
                search_file(C[0], C[1])
                X = X + 1
                Flag = False
            else:print('ERROR')
        elif((C[0] == cmd_list[2] or C[0] == cmd_list[3] or C[0] == cmd_list[4] or C[0] == cmd_list[5] or C[0] == cmd_list[6] or C[0] == cmd_list[7]) and (X==1)):
            if(C[0] == cmd_list[2] and len(C)==1):
                command(C[0],F)
                X = X + 1
                Flag = False
            elif(C[0] != cmd_list[2] and len(C)==2 and X==1):
                command(C[0],F,C[1])
                X = X + 1
                Flag = False
            else:print('ERROR')

        elif((C[0] == cmd_list[8] or C[0] == cmd_list[9] or C[0] == cmd_list[10]) and (len(C)==1) and X==2):
            #print('1')
            command(C[0])
            break
        else:
            print("ERROR")



def search_file(letter, path) -> None:
    if (letter == "D"):
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filenames:
                F.append(name)
                P1.append(os.path.join(dirpath, name))
            break
        for P1_path in P1:
            print(P1_path)
    if (letter == "R"):
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filenames:
                F.append(name)
                P1.append(os.path.join(dirpath, name))
        for P1_path in P1:
            print(P1_path)


def command(letter, files=True, values=True) -> None:
    n = 0
    if (letter == 'A'):
        for filename in files:
            P2.append(P1[n])
            n = n + 1
        for P2_path in P2:
            print(P2_path)
    if (letter == 'N'):
        for filename in files:
            if (values == filename):
                P2.append(P1[n])
            n = n + 1
        for P2_path in P2:
            print(P2_path)
    if (letter == 'E'):
        for filename in files:
            (filename, filextension) = os.path.splitext(filename)
            extension = '.' + values
            if (filextension == extension):
                P2.append(P1[n])
            n = n + 1
        for P2_path in P2:
            print(P2_path)
    if (letter == 'T' and X==2):
        for P2_path in P2:
            os.utime(P2_path, None)
    elif (letter == 'T'):
        for filename in files:
            (filename, filextension) = os.path.splitext(filename)
            if (filextension == '.txt'):
                if values in open(P1[n], "r", encoding="utf8").read():
                    P2.append(P1[n])
            else:
                pass
                #print('ERROR')
            n = n + 1
        for P2_path in P2:
            print(P2_path)
    if (letter == '<'):
        SIZE = int(values)
        for file_path in P1:
            file_stats = os.stat(file_path)
            if (file_stats.st_size <= SIZE):
                P2.append(file_path)
        for P2_path in P2:
            print(P2_path)
    if (letter == '>'):
        SIZE = int(values)
        for file_path in P1:
            file_stats = os.stat(file_path)
            if (file_stats.st_size >= SIZE):
                P2.append(file_path)
        for P2_path in P2:
            print(P2_path)
    if (letter == 'F'):
        for filename in P2:
            #print(filename)
            (filename, filextension) = os.path.splitext(filename)
            if (filextension == '.txt'):
                file = open(P2[n], 'r', encoding="utf8", newline=None)
                data = file.readlines()
                print(data[0].strip())
            else:
                print("NOT TEXT")
            n = n + 1
    if (letter == 'D'):
        for P2_path in P2:
            shutil.copy(P2_path, P2_path + ".dup")


def main():
    cmdin()
    cmdin()
    cmdin()

if __name__ == '__main__':
    X = 0
    P1 = []
    P2 = []
    F = []
    main()