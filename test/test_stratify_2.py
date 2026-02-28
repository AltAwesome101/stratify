#!/usr/bin/env python3
import unittest
import os
import stratify

this_dir = os.path.dirname(__file__)

class TestExclude(unittest.TestCase):

    def setUp(self):
        self.test_data = stratify.inputData(os.path.join(this_dir,"sample.evec"))
        self.evecs = self.test_data[0]
        self.pop   = self.test_data[1]
        self.pids  = self.test_data[2]

    def test_centre1(self):
        c1 = stratify.getCentroid(self.evecs, 1, self.pop["KS3"])
        self.assertAlmostEqual(c1, -0.014050000000)

    def test_populations_loaded(self):
        # check that expected populations exist in the data
        self.assertIn("Baganda_quad", self.pop)
        self.assertIn("YRI", self.pop)
        self.assertIn("CEU", self.pop)

    def test_person_count(self):
        # check total number of people loaded
        self.assertEqual(len(self.evecs), len(self.pids))

    def test_baganda_outlier(self):
        # from running the program we know person index 17
        # is an outlier in Baganda_quad
        excludes = stratify.remOutliers(self.evecs, self.pids,
                                        self.pop["Baganda_quad"])
        self.assertIn(17, excludes)

    def test_yri_outliers(self):
        # YRI population should have outliers at 564 and 602
        excludes = stratify.remOutliers(self.evecs, self.pids,
                                        self.pop["YRI"])
        self.assertIn(564, excludes)
        self.assertIn(602, excludes)

    def test_zulu_octo_no_outliers(self):
        # Zulu_octo should have no outliers
        excludes = stratify.remOutliers(self.evecs, self.pids,
                                        self.pop["Zulu_octo"])
        self.assertEqual(excludes, [])

if __name__ == '__main__':
    unittest.main()
