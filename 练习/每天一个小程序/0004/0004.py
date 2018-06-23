#-*-coding:utf-8-*-
#统计任意文件中的单词数量

import re
#正则表达式

with open('text.txt') as f:
    str = f.read()

# 打开文件，读取内容。值得一提：如果文件过大，则会打开失败（内存不够）。对于安全人员来说最普遍的
#情况是打开日志文件。面试的时候问到过解决方法：使用迭代器
# with '/var/log/file.txt' as f:
#     for line in f:
#         在这里处理
# 这样会自动使用缓存IO和内存管理,这样我们就不需要关注大的文件了



bt = r'[\w\-\']+'
#这个字符是不是数字、大小写字母或者单横线、单引号。是的话继续匹配，直到不是为止。
pattern = re.compile(bt)
#编译之后会加快匹配速度
m = pattern.findall(str)
#字符串中所有匹配成功的结果弄成列表赋给m
print len(m)

