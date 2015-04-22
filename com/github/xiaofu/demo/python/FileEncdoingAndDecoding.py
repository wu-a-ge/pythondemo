#encoding=utf-8
'''
Created on 2015年4月22日

@author: fulaihua
'''
import unittest,codecs,sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Test(unittest.TestCase):
    
    def testBuiltinCodec(self):
        fout = open("test.txt",'r')
    def testCodecs(self):
        content="中国人民大学"
        print repr(content)
        print content.decode("utf-8")
        fout = codecs.open("test.txt", 'w', 'utf-8')
        fout.write(content)
        fout.flush()
        fout.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()