from django.test import TestCase
import unittest

from .models import StlInfo


class UserTestCase(TestCase): 
    def setUp(self): 
        pass

    def test_creating_stlinfo(self):
        file_path ='lib/testfiles/Octocat-v1.stl'
        obj = StlInfo.objects.create(name = file_path.split('/')[-1], stl_file=file_path)
        self.assertEqual(obj.id, 1)
        qs = StlInfo.objects.all()
        self.assertEqual(qs.count(),1)
   
    @unittest.expectedFailure
    def test_creating_empty_stlinfo(self):
        obj = StlInfo.objects.create(name = None, stl_file=None)
        self.assertEqual(obj.id, )
        qs = StlInfo.objects.all()
        self.assertEqual(qs.count(),1)
    