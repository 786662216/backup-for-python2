#-*-coding:utf-8-*-

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def openfile(url1):
    with open(url1) as f:
        content = f.read()
    return content

def lines(str1):
    return len(str1.split('\n'))

def main():


if __name__ == '__main__':
    main()
