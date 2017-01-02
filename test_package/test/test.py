#!/usr/bin/env python

import sys
import unittest
import rospy
import rostest

from my_msgs.msg import MyMessage

class TestPackageTest(unittest.TestCase):

    def setUp(self):

        pass

    def test_something(self):

        self.assertEquals(True, True, "True-True test")


if __name__ == '__main__':

    rostest.run('test_package', 'test_package_test', TestPackageTest, sys.argv)
