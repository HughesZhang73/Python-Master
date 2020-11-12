# coding=utf-8


import os
import sys


def search(dir, file_list):
    newDir = dir
    if os.path.isfile(dir):
        file_list.append(dir)
    elif os.path.isdir(dir):
        for i in os.listdir(dir):
            newDir = os.path.join(dir, i)
            search(newDir, file_list)
            
    return file_list


if __name__ == '__main__':
    path = 'C:\\Users\\THINKPAD\\Desktop\\untitled'
    
    ll = search(path, [])
    for x in ll:
        (path, name) = os.path.split(x)
        print(name)
        # print(path)
