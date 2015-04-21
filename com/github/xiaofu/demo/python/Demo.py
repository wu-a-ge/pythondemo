#encoding=gb18030
#@author: fulaihua
import sys,time,os
reload(sys)
sys.setdefaultencoding("gb18030")
def task():
    print "ok"
def main():
    while True:
        task()
        time.sleep(5)
fileName=r"E:\VIP\spider\dataCrawler\QkParser1.0\QkParser1.0\output\20141428910804\tosqlserver.bat"
try:
    os.system(fileName)
except Exception,e:
    print e
if __name__ == '__main__':
    pass