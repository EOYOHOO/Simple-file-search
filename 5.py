import os
import re
from pathlib import Path
import shutil
PATHone = []
PATHtow = []
f = []
def get_input(i:int)->str :
    """
    获得不同部分的输入信息
    """
    """
    第一步：查询
    1、以空格为间隔录入命令
    2、首字母必须是R和D
    3、路径信息正确
    """
    if i==1:
        while(True):
            middle = input().split()
            letter = middle[0]
            if((letter=="R" or letter=="D") and len(middle)==2):
                path = middle[1]
                if(os.path.exists(path)):
                    all_file(path, letter)
                    break
                else:
                    ERROR()
            else:ERROR()
    """
    第二步：条件查询
    1、单字母命令：必须是A
    2、字母+条件命令：必须是 N E T < > 
    """
    if i == 2:
        while (True):
            middle = input().split()
            letter = middle[0]
            if (letter == "A"):
                searchAllFile(letter)
                break
            elif ((letter == 'N' or letter == 'E' or letter == 'T' or letter == '>' or letter == '<') and len(middle)==2):
                path = middle[1]
                searchAllFile(letter, path, f)
                break
            else:ERROR()
    """第三步：修改
       1、单字母命令：F D T
    """
    if i == 3:
        while (True):
            letter = input()
            if (letter == "F" or letter == "D" or letter == "T"):
                cmd(letter)
                break
            else:
                ERROR()
def all_file(path: str, letter: str) -> None:
    """
    文件显示
    """
    """只查看当前文件夹下的所有文件"""
    if letter == "D":
        for root, dirs, files in os.walk(path):
            for file in files:
                f.append(file)
                #print(os.path.join(root, file))
                PATHone.append(os.path.join(root, file))
            # print(PATH)
            break
    """递归查看所有文件夹下的所有文件"""
    if letter == "R":  # 重新编写
        """一、先查看当前目录下文件"""
        """二、递归当前目录的子目录文件"""
        for root, dirs, files in os.walk(path):
            for file in files:
                f.append(file)
                #print(os.path.join(root, file))
                PATHone.append(os.path.join(root, file))
        # print(PATH)

def searchAllFile(letter, values: str=True, files: list=True) -> None:
    s = 0
    """  
    文件查询功能
    """
    if letter == 'A':
        for filename in PATHone:
            PATHtow.append(PATHone[s])
            s = s + 1
    """查询指定文件名的文件"""
    if letter == 'N':
        for filename in files:
            if (values == filename):
                #print(PATHone[n])
                PATHtow.append(PATHone[s])
            s = s + 1
    """查询指定扩展名的文件"""
    if letter == 'E':
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            ext = '.' + values
            if (extension == ext):
                #print(filename)
                PATHtow.append(PATHone[s])
            s = s + 1
    """查询指定文件内容的文件"""
    if letter == 'T':
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            if (extension == '.txt'):
                #print(filename)
                if values in open(PATHone[s], "r", encoding="utf8").read():
                    PATHtow.append(PATHone[s])
            s = s + 1


    """查询小于指定字节数的文件"""
    if letter == '<':
        x = int(values)
        for file_path in PATHone:
            file_stats = os.stat(file_path)
            #print(file_stats.st_size)
            if(file_stats.st_size<x):
                PATHtow.append(file_path)
    """查询大于字节数的文件"""
    if letter == '>':
        x = int(values)
        for file_path in PATHone:
            file_stats = os.stat(file_path)
            #print(file_stats.st_size)
            if(file_stats.st_size>x):
                PATHtow.append(file_path)



def cmd(letter:str):
    s = 0
    if letter == 'F':
        for PATHtow_path in PATHtow:
            (name, suffix) = os.path.splitext(PATHtow_path)
            if (suffix == '.txt'):
                #print(PATHtow[n])
                file = open(PATHtow_path, 'r', encoding="utf8",newline=None)
                text = file.readlines()
                print(text[0].strip())
            else:
                print("NOT TEXT")
            s = s + 1
    if letter == 'D':
        for PATH in PATHtow:
            #print(PATH)
            shutil.copy(PATH,PATH+".dup")
    if letter == 'T':
        for PATH in PATHtow:
            #print(PATH)
            os.utime(PATH, None)

def ERROR():
    print('ERROR')
def main():
    """
        程序执行流程：
        """
    get_input(1)
    for PATH in PATHone:
        print(PATH)
    get_input(2)
    for PATH in PATHtow:
        print(PATH)
    get_input(3)
if __name__ == '__main__':
    main()