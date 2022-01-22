import os
import re
import shutil
from pathlib import Path

def search_allfile(path: str, ZIMU: str) -> None:
    """
    文件显示
    """
    """只查看当前文件夹下的所有文件"""
    if (ZIMU == "D"):
        for root, dirs, files in os.walk(path):
            for file in files:
                f.append(file)
                #print(os.path.join(root, file))
                PATHone.append(os.path.join(root, file))
            # print(PATH)
            break
    """递归查看所有文件夹下的所有文件"""
    if (ZIMU == "R"):  # 重新编写
        """一、先查看当前目录下文件"""
        """二、递归当前目录的子目录文件"""
        for root, dirs, files in os.walk(path):
            for file in files:
                f.append(file)
                #print(os.path.join(root, file))
                PATHone.append(os.path.join(root, file))
        # print(PATH)

def search_file(files: list, ZIMU: str, path: str=True) -> None:
    n = 0
    """
    文件查询功能
    """
    if (ZIMU == 'A'):
        for filename in files:
            PATHtow.append(PATHone[n])
            n = n + 1
    """查询指定文件名的文件"""
    if (ZIMU == 'N'):
        for filename in files:
            if (path == filename):
                #print(PATHone[n])
                PATHtow.append(PATHone[n])
                n = n + 1
            else:
                n = n + 1
    """查询指定扩展名的文件"""
    if (ZIMU == 'E'):
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            ext = '.' + path
            if (extension == ext):
                #print(filename)
                PATHtow.append(PATHone[n])
                n = n + 1
            else:
                n = n + 1
    """查询指定文件内容的文件"""
    if (ZIMU == 'T'):
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            if (extension == '.txt'):
                #print(filename)
                if path in open(PATHone[n], "r", encoding="utf8").read():
                    PATHtow.append(PATHone[n])
                n = n + 1
            else:
                n = n + 1

    """查询小于指定字节数的文件"""
    if (ZIMU == '<'):
        x = int(path)
        for file_path in PATHone:
            file_stats = os.stat(file_path)
            #print(file_stats.st_size)
            if(file_stats.st_size<x):
                PATHtow.append(file_path)
    """查询大于字节数的文件"""
    if (ZIMU == '>'):
        x = int(path)
        for file_path in PATHone:
            file_stats = os.stat(file_path)
            #print(file_stats.st_size)
            if(file_stats.st_size>x):
                PATHtow.append(file_path)



def cmd(files: list, ZIMU:str):
    n = 0
    if (ZIMU == 'F'):
        for filename in files:
            #print(filename)
            (name, extension) = os.path.splitext(filename)
            if (extension == '.txt'):
                #print(PATHtow[n])
                file = open(PATHtow[n], 'r', encoding="utf8",newline=None)
                data = file.readlines()
                print(data[0].strip())
                n = n + 1
            else:
                print("NOT TEXT")
                n = n + 1
    if (ZIMU == 'D'):
        for PATH in PATHtow:
            #print(PATH)
            shutil.copy(PATH,PATH+".dup")
    if (ZIMU == 'T'):
        for PATH in PATHtow:
            #print(PATH)
            os.utime(PATH, None)



if __name__ == '__main__':
    """
            程序执行流程：
            """
    PATHone = []
    PATHtow = []
    f = []
    flag = True
    while (flag):
        mid = input(r'').split()
        if ((len(mid) == 2) and (mid[0] == 'R' or 'D') and (os.path.exists(mid[1]))):
            search_allfile(mid[1], mid[0])
            # P = mid[1]
            flag = False
        else:
            print('ERROR')

    # print(f)
    for PATH in PATHone:
        print(PATH)
    # print(f)

    flag = True
    while (flag):
        mid = input().split()
        if ((len(mid) == 2) and (mid[0] == 'N' or mid[0] == 'E' or mid[0] == 'T' or mid[0] == '>' or mid[0] == '<')):
            search_file(f, mid[0], mid[1])
            flag = False
        elif ((len(mid) == 1) and (mid[0] == 'A')):
            search_file(f, mid[0])
            flag = False
        else:
            print("ERROR")
    for PATH in PATHtow:
        print(PATH)
    flag = True
    while (flag):
        letter = input('')
        if (letter == 'D' or letter == 'T' or letter == 'F'):
            cmd(PATHtow, letter)
            flag = False
        else:
            print('ERROR')
    # print(f)