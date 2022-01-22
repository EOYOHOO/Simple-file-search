import os


def XUNZHAO(letter, values: str=True, files: list=True) -> None:
    M = 0
    """  
    文件查询功能
    """
    if letter == 'A':
        for filename in ROAD1:
            ROAD2.append(ROAD1[M])
            M = M + 1
    """查询指定文件名的文件"""
    if letter == 'N':
        for filename in files:
            if (values == filename):
                # print(PATHone[n])
                ROAD2.append(ROAD1[M])
            M = M + 1
    """查询指定扩展名的文件"""
    if letter == 'E':
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            ext = '.' + values
            if (extension == ext):
                # print(filename)
                ROAD2.append(ROAD1[M])
            M = M + 1
    """查询指定文件内容的文件"""
    if letter == 'T':
        for filename in files:
            (name, extension) = os.path.splitext(filename)
            if (extension == '.txt'):
                # print(filename)
                if values in open(ROAD1[M], "r", encoding="utf8").read():
                    ROAD2.append(ROAD1[M])
            M = M + 1

    """查询小于指定字节数的文件"""
    if letter == '<':
        x = int(values)
        for file_road in ROAD1:
            file_stats = os.stat(file_road)
            # print(file_stats.st_size)
            if (file_stats.st_size < x):
                ROAD2.append(file_road)
    """查询大于字节数的文件"""
    if letter == '>':
        x = int(values)
        for file_road in ROAD1:
            file_stats = os.stat(file_road)
            # print(file_stats.st_size)
            if (file_stats.st_size > x):
                ROAD2.append(file_road)


def main():

    while (True):
        middle = input().split()
        letter = middle[0]
        if (letter == "R" or letter == "D") and len(middle) == 2:
            path = middle[1]
            if (os.path.exists(path)):
                if (letter == "D"):
                    for A, B, C in os.walk(path):
                        for c in C:
                            names.append(c)
                            ROAD1.append(os.path.join(A, c))
                        break
                if (letter == "R"):
                    for A, B, C in os.walk(path):
                        for c in C:
                            names.append(c)
                            ROAD1.append(os.path.join(A, c))
                break
            else:
                ERROR()
        else:
            ERROR()
    for P in ROAD1:
        print(P)

    while (True):
        middle = input().split()
        letter = middle[0]
        if (letter == "A"):
            XUNZHAO(letter)
            break
        elif ((letter == 'N' or letter == 'E' or letter == 'T' or letter == '>' or letter == '<') and len(middle) == 2):
            path = middle[1]
            XUNZHAO(letter, path, names)
            break
        else:
            ERROR()
    for P in ROAD2:
        print(P)

    while (True):
        letter = input()
        if (letter == "F" or letter == "D" or letter == "T"):
            I = 0
            if letter == 'F':
                for P in ROAD2:
                    (MZ, extension) = os.path.splitext(P)
                    if (extension == '.txt'):
                        file = open(P, 'r', encoding="utf8", newline=None)
                        data = file.readlines()
                        print(data[0].strip())
                    else:
                        print("NOT TEXT")
                    I = I + 1
            if letter == 'D':
                for P in ROAD2:
                    shutil.copy(P, P + ".dup")
            if letter == 'T':
                for P in ROAD2:
                    os.utime(P, None)
            break
        else:
            ERROR()

def ERROR():
    print('ERROR')


if __name__ == '__main__':
    names = []  # 放入文件名
    ROAD1 = []  # 放入第一次筛选的路径
    ROAD2 = []  ##放入第二次筛选的路径
    main()


