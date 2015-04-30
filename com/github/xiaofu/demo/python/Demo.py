#encoding=utf-8
#@author: fulaihua
import sys,time,os,ClassTest
reload(sys)
sys.setdefaultencoding("utf-8")
path=os.path.join(u"D:\win7 64位系统")
print repr(path)
a=os.listdir(path.decode("utf-8"))
print a
print ClassTest.nick
if __name__ == '__main__':
    pass