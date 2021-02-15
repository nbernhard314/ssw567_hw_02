# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testGreaterThan200(self):
        self.assertEqual(classifyTriangle(2,2,400), 'InvalidInput', '2,2,200 should be invalid input')
        self.assertEqual(classifyTriangle(200,400,400), 'InvalidInput', '200,400,400 should be invalid input')
        self.assertEqual(classifyTriangle(600,400,500), 'InvalidInput', '600,400,500 should be invalid input')

    def testLessThanOrEqualZero(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 should be invalid input')
        self.assertEqual(classifyTriangle(3,0,3), 'InvalidInput', '3,0,3 should be invalid input')
        self.assertEqual(classifyTriangle(2,2,-2), 'InvalidInput', '2,2,-2 should be invalid input')
        self.assertEqual(classifyTriangle(-3,-4,-5), 'InvalidInput', '-3,-4,-5 should be invalid input')

    

    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

