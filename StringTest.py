'''
Created on 24/ago/2012

@author: fede
'''
import unittest,String

def make_test_init():
    class testInit(unittest.TestCase):
        def setUp(self):
            self.valuesOK   = ['Microsoft','Windows','Skype']
            self.valuesKO   = [14,6,0,123]
        
        def testInitOK(self):
            for i in self.valuesOK:
                result = String.MyString(i)
                self.assertEqual(i,result)
        
        def testInitKO(self):
            for i in self.valuesKO:
                self.assertRaises(String.InvalidArgument, String.MyString,i)
                
        def tearDown(self):
            self.valuesOK = []
            self.valuesKO = []
    return testInit

def make_test_rshift():
    class testRS(unittest.TestCase):
        def setUp(self):
            self.values   = [('Microsoft',2,'crosoftMi'),('Windows',3,'dowsWin'),('Skype',1,'kypeS')]
            self.valuesKO   = [('Microsoft',-2),('Windows',0),('Skype',-5)]
            
        def test_rshift(self):
            for val,shift,check in self.values:
                    result = String.MyString(val) >> shift
                    self.assertEqual(check, result)
                    
        def test_rshiftKO(self):
            for val,shift in self.valuesKO:
                self.assertRaises(String.InvalidShift, String.MyString(val).__rshift__,shift)
        
        
        def tearDown(self):
            self.values = []
            self.valuesKO = []
        
    return testRS

def make_test_multirshift():
    class testMRS(unittest.TestCase):
        def setUp(self):
            self.values   = [('Microsoft',1,1,'crosoftMi'),('Windows',2,1,'dowsWin'),('Skype',1,3,'eSkyp')]
            
        def test_mrshift(self):
            for val,s1,s2,check in self.values:
                    temp = String.MyString(val)
                    temp >> s1
                    result = temp >> s2
                    self.assertEqual(check, result)
        
        def tearDown(self):
            self.values = []
        
    return testMRS

def make_test_lshift():
    class testLS(unittest.TestCase):
        def setUp(self):
            self.values   = [('Microsoft',2,'ftMicroso'),('Windows',3,'owsWind'),('Skype',1,'eSkyp')]
            self.valuesKO   = [('Microsoft',-2),('Windows',0),('Skype',-5)]
            
        def test_lshift(self):
            for val,shift,check in self.values:
                    result = String.MyString(val) << shift
                    self.assertEqual(check, result)
                    
        def test_lshiftKO(self):
            for val,shift in self.valuesKO:
                self.assertRaises(String.InvalidShift, String.MyString(val).__lshift__,shift)
        
        
        def tearDown(self):
            self.values = []
            self.valuesKO = []
        
    return testLS

def make_test_multilshift():
    class testMLS(unittest.TestCase):
        def setUp(self):
            self.values   = [('Microsoft',1,1,'ftMicroso'),('Windows',2,1,'owsWind'),('Skype',1,3,'kypeS')]
            
        def test_mlshift(self):
            for val,s1,s2,check in self.values:
                    temp = String.MyString(val)
                    temp << s1
                    result = temp << s2
                    self.assertEqual(check, result)
        
        def tearDown(self):
            self.values = []
        
    return testMLS

def make_test_equal():
    class testEQ(unittest.TestCase):
        def setUp(self):
            self.values   = [('Microsoft','Microsoft',True),('Windows','owsWind',False),('Skype','kypeS',False)]
            
        def test_eq(self):
            for val1,val2,check in self.values:
                    result = String.MyString(val1) == val2
                    self.assertEqual(check, result)
        
        def tearDown(self):
            self.values = []
        
    return testEQ

test1 = make_test_init()
test2 = make_test_rshift()
test3 = make_test_multirshift()
test4 = make_test_lshift()
test5 = make_test_multilshift()
test6 = make_test_equal()

if __name__ == "__main__": unittest.main()