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
        self.assertEqual(classifyTriangle(5,12,13), 'Right', '5,12,13 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(13,5,12), 'Right', '13,5,12 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
        self.assertEqual(classifyTriangle(5,13,12), 'Right', '5,13,12 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(199,199,199),'Equilateral','199,199,199 should be equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3,4,4), 'Isosceles', '3,4,4 should be an isosceles triangle')
        self.assertEqual(classifyTriangle(29,65,65), 'Isosceles', '29,65,65 should be an isosceles triangle')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4,3,4), 'Isosceles', '4,3,4 should be an isosceles triangle')
        self.assertEqual(classifyTriangle(65,29,65), 'Isosceles', '65,29,65 should be an isosceles triangle')

    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(4,4,3), 'Isosceles', '4,4,3 should be an isosceles triangle')
        self.assertEqual(classifyTriangle(65,65,29), 'Isosceles', '65,65,29 should be an isosceles triangle')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(2,4,5), 'Scalene', '2,4,5 should be a scalene triangle')
        self.assertEqual(classifyTriangle(29,32,55), 'Scalene', '29,32,55 should be a scalene triangle')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(4,5,2), 'Scalene', '4,2,5 should be a scalene triangle')
        self.assertEqual(classifyTriangle(32,55,29), 'Scalene', '32,55,29 should be a scalene triangle')
        
    def testGreaterThan200(self):
        self.assertEqual(classifyTriangle(2,2,400), 'InvalidInput', '2,2,200 should be invalid input')
        self.assertEqual(classifyTriangle(200,400,400), 'InvalidInput', '200,400,400 should be invalid input')
        self.assertEqual(classifyTriangle(600,400,500), 'InvalidInput', '600,400,500 should be invalid input')

    def testLessThanOrEqualZero(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 should be invalid input')
        self.assertEqual(classifyTriangle(3,0,3), 'InvalidInput', '3,0,3 should be invalid input')
        self.assertEqual(classifyTriangle(2,2,-2), 'InvalidInput', '2,2,-2 should be invalid input')
        self.assertEqual(classifyTriangle(-3,-4,-5), 'InvalidInput', '-3,-4,-5 should be invalid input')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle', '1,2,3 is not a triangle')
        self.assertEqual(classifyTriangle(100,150,25), 'NotATriangle', '100,150,25 is not a triangle')

    def testFloats(self):
        self.assertEqual(classifyTriangle(1.5,2.3,3), 'InvalidInput', '1.5,2.3,3 should be invalid input')
        self.assertEqual(classifyTriangle(1.5,2,3), 'InvalidInput', '1.5,2,3 should be invalid input')
        self.assertEqual(classifyTriangle(15.7,23.5,30.1), 'InvalidInput', '15.7,23.5,30.1 should be invalid input')
        self.assertEqual(classifyTriangle(2,2,3.3), 'InvalidInput', '2,2,3.3 should be invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

