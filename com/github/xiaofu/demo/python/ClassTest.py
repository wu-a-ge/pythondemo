'''
 

@author: fulaihua
'''
class A(object):  
    def tell(self):  
        print 'A tell'  
        self.say()  
    def say(self):  
        print 'A say'  
        self.__work()  
  
    def __work(self): # private  
        print 'A work'  
  
          
class B(A):  
    def tell(self):  
        print '\tB tell'  
        self.say()  
        super(B,self).say()  
        A.say(self)  
    def say(self):  
        print '\tB say'  
        self.__work()  
  
    def __work(self): # private  
        print '\tB work'  
        self.__run()  
  
    def __run(self): # private  
        print '\tB run'  
          
b = B()  
b.tell()  
if __name__ == '__main__':
    pass