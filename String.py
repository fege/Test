'''
Created on 24/ago/2012

@author: fede
'''
class InvalidArgument(ValueError): pass
class InvalidShift(ValueError): pass
class MyString(str):
    
    def __init__(self,val):
        if type(val) is not type('a'):
            raise InvalidArgument('argument must be string!')
        self.str=val

    def __str__(self):
        return self.str
    
    def __rshift__(self,a):
        if a <=0:
            raise InvalidShift('shift must be positive!')
        self.str=self.str[a:]+self.str[:a]
        return self.str
    
    def __lshift__(self,a):
        if a <=0:
            raise InvalidShift('shift must be positive!')
        self.str=self.str[-a:]+self.str[:-a]
        return self.str

    def __eq__(self,a):
        return self.str is a
