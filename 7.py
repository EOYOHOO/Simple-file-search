import os
import re
from pathlib import Path
import shutil
list = ["D", "R" , "A" , "T" , "N" , "E" , ">" ,"<" , "F" , "D" , "T"]
H = 0

R1 = []
R2 = []
FILE=[]

def D(path):

    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            FILE.append(name)
            R1.append(os.path.join(dirpath, name))
        break
    for R1_path in R1:
        print(R1_path)
def R(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            FILE.append(name)
            R1.append(os.path.join(dirpath, name))
    for R1_path in R1:
        print(R1_path)
def A(files):
    n = 0
    for filename in files:
        R2.append(R1[n])
        n = n + 1
    for R2_path in R2:
        print(R2_path)
def T1(path):
    n = 0
    for filename in FILE:
        (filename, postfix) = os.path.splitext(filename)
        if (postfix == '.txt'):
            if path in open(R1[n], "r", encoding="utf8").read():
                R2.append(R1[n])
            n = n + 1
        else:
            # print('ERROR')
            n = n + 1
def T2():
    for P in R2:
        os.utime(P, None)
def E(values):
    n = 0
    for filename in FILE:
        (filename, filextension) = os.path.splitext(filename)
        extension = '.' + values
        if (filextension == extension):
            R2.append(R1[n])
        n = n + 1
def N(values):
    n = 0
    for filename in FILE:
        if (values == filename):
            R2.append(R1[n])
        n = n + 1
def high(values):
    SIZE = int(values)
    for file_path in R1:
        file_stats = os.stat(file_path)
        if (file_stats.st_size >= SIZE):
            R2.append(file_path)
def low(values):
    SIZE = int(values)
    for file_path in R1:
        file_stats = os.stat(file_path)
        if (file_stats.st_size <= SIZE):
            R2.append(file_path)
def F():
    n = 0
    for filename in R2:
        (filename, filextension) = os.path.splitext(filename)
        if (filextension == '.txt'):
            file = open(R2[n], 'r', encoding="utf8", newline=None)
            data = file.readlines()
            print(data[0].strip())
        else:
            print("NOT TEXT")
        n = n + 1
def D():
    for P in R2:
        shutil.copy(P, P + ".dup")
def inPut():
    global H
    while(True):
        cmd = input(r'').split()
        if len(cmd)==2 and cmd[0] in ['D','R'] and  H == 0:
            if(os.path.exists(cmd[1])):
                path = cmd[1]
                if cmd[0]=='D':
                    D(path)
                    H = H + 1
                    break
                elif cmd[0]=='R':
                    R(path)
                    H = H + 1
                    break
            else:print('ERROR')
        elif cmd[0] in ['A'] and len(cmd)==1 and H == 1:
            A(FILE)
            H = H + 1
            break
        elif cmd[0] in ['T','E','N','>','<'] and len(cmd)==2 and H == 1:
            path = cmd[1]
            H = H + 1
            if cmd[0]=='T':
                T1(path)
                break
            elif cmd[0]=='E':
                E(path)
                break
            elif cmd[0]=='N':
                N(path)
                break
            elif cmd[0]=='>':
                high(path)
                break
            elif cmd[0]=='<':
                low(path)
                break
        elif cmd[0] in ['F' , 'D' , 'T'] and len(cmd)==1 and H == 2:
            if cmd[0]=='F':
                F()
                break
            elif cmd[0]=='D':
                D()
                break
            elif cmd[0]=='T':
                T2()
                break
        else:
            print('ERROR')



def main():

    inPut()
    for P in R1:
        print(P)
    inPut()
    for P in R2:
        print(P)
    inPut()
if __name__ == '__main__':
    main()