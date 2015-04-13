#encoding=utf-8
'''
Created on 2015��4��13��
@author: xiaofu
'''
import unittest
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Test(unittest.TestCase):


    def testEncoding(self):
        #这里是str字节串，用的是文件指定编码utf-8,所有u已经为str类型的字节串了
        u = '汉'
        print repr(u) # '\xe6\xb1\x89'
        #=======================================================================
        #抛异常的原因是u已经是字节串编码，
        #所以需要先转换成unicode字符编码再使用utf-8编码成字节串编码，而由于python系统默认使用的是ascii编码，所以造成在解码的
        #时候失败，在这种情况下需要指定系统的解码sys.setdefaultencoding("utf-8")
        #=======================================================================
        try:
            s = u.encode('UTF-8')
        except Exception,e:
            print e

    def testDecoding(self):
        u="汉"
        print repr(u) # '\xe6\xb1\x89'
        s = u.encode('UTF-8')
        print repr(s) # '\xe6\xb1\x89'
        u2 = s.decode('UTF-8')
        print repr(u2) # u'\u6c49'

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()