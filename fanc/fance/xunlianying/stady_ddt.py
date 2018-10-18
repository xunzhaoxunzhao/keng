import unittest
import ddt

# @ddt.ddt
# class DoubanTest(unittest.TestCase):
#     @ddt.data(2,3,6)
#     @ddt.unpack
#     def test_normal(self,value1,value2,value3):
#         print(value1,value2,value3)
#
# if __name__=='__main__':
#     unittest.main()
# @ddt.ddt
# class MyTest(unittest.TestCase):
#     @ddt.data((1,2),(2,3))
#     @ddt.unpack
#     def test_tuple(self,value1,value2):
#         print(value1,value2)
#
#     @ddt.data([1,2],[2,3])
#     @ddt.unpack
#     def test_list(self,value1,value2):
#         print(value1,value2)
#     @ddt.data({'one':1,'two':2})
#     @ddt.unpack
#     def test_dict(self,one,two):
#         print(one,two)
#
# if __name__=="__main__":
#     unittest.main()
import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class demotest(unittest.TestCase):
    def setup(self):
        print ("this is the setup")

    @data(2,3)
    def testb(self,value):
        print (value)
        print ("this is test b")

    @data([2,3],[4,5])
    def testa(self,value):
        print (value)
        print ("this is test a")

    @data([2, 3], [4, 5])
    @unpack
    def testc(self, first,second):
        print (first)
        print (second)
        print ("this is test c")

    # @file_data('d:/data_dic.json')
    # # def test_dic(self,value):
    # #     print value
    # #     print 'this is dic'
    #
    # @file_data('d:/data.yml')
    # def test_yml(self, value):
    #     print (value)
    #     print 'this is yml'

    def teardown(self):
        print ("this is the down")

if __name__ == '__main__':
    unittest.main()
    #suite=unittest.TestLoader.getTestCaseNames(demotest)
    #suite = unittest.TestLoader().loadTestsFromTestCase(demotest)
    #unittest.TextTestRunner(verbosity=2).run(suite)