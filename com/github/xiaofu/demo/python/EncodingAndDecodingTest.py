#encoding=utf-8
'''
Created on 2015��4��13��
@author: xiaofu
'''
import unittest
import sys
reload(sys)
#sys.setdefaultencoding("utf-8")

class Test(unittest.TestCase):

    #此测试效果需要将sys.setdefaultencoding("utf-8")注释掉
    def testEncoding(self):
        #这里是str字节串，用的是文件指定编码utf-8,所以u已经为str类型的字节串了
        u = '汉'
        print repr(u) # '\xe6\xb1\x89'
        #=======================================================================
        #抛异常的原因是u已经是字节串编码，
        #所以需要先将u使用系统指定的编码进行解码，然后再使用指定的utf-8编码成字节串，而由于python系统默认使用的是ascii编码，所以造成在解码的
        #时候失败，所以在这种情况下需要指定系统的解码sys.setdefaultencoding("utf-8")
        #=======================================================================
        try:
            s = u.encode('UTF-8')
        except Exception,e:
            print e
    #此测试效果需要加上sys.setdefaultencoding("utf-8")
    def testDecoding(self):
        u="汉"
        print repr(u) # '\xe6\xb1\x89'
        #u先使用系统指定的编码进行解码，再使用指定的utf-8编码
        s = u.encode('UTF-8')
        print repr(s) # '\xe6\xb1\x89'
        u2 = s.decode('UTF-8')
        print repr(u2) # u'\u6c49'

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()