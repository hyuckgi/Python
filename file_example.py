# -*- coding: utf-8 -*-

fh = open('log.txt', 'r')
# count = 0
# for line in fh:
#     print line.strip()
#     count = count + 1
#
# print "Line = ", count


fh = open('log.txt', 'a')
fh.write("hello world\n")

fh.close();
