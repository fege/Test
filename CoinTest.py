'''
Created on 24/ago/2012

@author: fede
'''
import unittest, Coin

class Test(unittest.TestCase):
    know_values = ((2,[1,1]),(135,[100,20,10,5]),(5,[5]),(3,[1,1,1]),(343,[100,100,100,20,20,1,1,1]))
    def testNegativeValue(self):
        for value in range(-1,-1000,-1):
            self.assertRaises(Coin.InvalidAmount, Coin.MakeChange,value)
    
    def testZeroValue(self):
        value=0
        self.assertRaises(Coin.InvalidAmount, Coin.MakeChange,value)
    
    def testPositiveValue(self):
        for num, expected in self.know_values:
            result = Coin.MakeChange(num)
            self.assertEqual(expected, result)

if __name__ == "__main__": unittest.main()