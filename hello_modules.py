# -*- coding:utf-8 -*-
'a chuan test module'

__author__ = 'Chuan Rao'

import  sys

def test():
    args = sys.argv
    if len(args) == 1:
        print ("Hello,World")
    elif len(args) == 2:
        print ('hello, %s' % args[1])
    else:
        print ("too more")


if __name__ == '__main__':
    test()
