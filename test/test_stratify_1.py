#!/usr/bin/env python3
import unittest
import stratify

class TestExclude(unittest.TestCase):

    def test_centre1(self):
        evecs=[[0,0,0],[-1,0,1],[1,0,1],[0,4,0]]
        c1 = stratify.getCentroid(evecs,1,[0,1])
        self.assertEqual(c1,0)

    def test_centre2(self):
        evecs=[[0,0,0],[-1,0,1],[1,0,1],[0,4,0]]
        c1 = stratify.getCentroid(evecs,0,[0,1])
        self.assertEqual(c1,-0.5)

    def test_stddev1(self):
        evecs = [[2,0,0],[2,0,0],[2,0,0],[2,0,0]]
        result = stratify.getSampleStdDev(evecs, 0, [0,1,2,3], 2)
        self.assertEqual(result, 0)

    def test_stddev2(self):
        evecs = [[2,0,0],[4,0,0],[4,0,0],[4,0,0],[5,0,0],
                 [5,0,0],[7,0,0],[9,0,0]]
        ave = stratify.getCentroid(evecs, 0, [0,1,2,3,4,5,6,7])
        result = stratify.getSampleStdDev(evecs, 0, [0,1,2,3,4,5,6,7], ave)
        self.assertAlmostEqual(result, 2.138, places=2)

    def test_no_outliers(self):
        evecs = [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
        result = stratify.remOutliers(evecs, ['a','b','c','d','e'], [0,1,2,3,4])
        self.assertEqual(result, [])

    def test_single_person(self):
        evecs = [[1,0,0]]
        result = stratify.remOutliers(evecs, ['a'], [0])
        self.assertEqual(result, [])

    def test_dummy(self):
        stratify.dummy(5)

if __name__ == '__main__':
    unittest.main()
