import ddt
import unittest,requests
import BeautifulReport
@ddt.ddt
class MyCase(unittest.TestCase):
    # @ddt.data(1,2,3)
    # def testa(self,num):
    #     self.assertTrue( num > 2)
    #
    # @ddt.data([1,2],[2,3],[3,3]) # 传多个参数的话，用一唯数组来传入
    # @ddt.unpack # 传多个参数的话，就要加上这个unpack,用来自动解包
    # def testb(self,num,num2):
    #     self.assertTrue( num > num2)

    @ddt.file_data('login.yml')
    @ddt.unpack
    def test_run(self,**kwargs): # kwarge 的作用是传不定数的参数时用的
          method = kwargs.get('method')
          url = kwargs.get('url')
          data = kwargs.get('data',{})
          header = kwargs.get('header',{})
          is_json = kwargs.get('is_json',0)
          cookie = kwargs.get('cookie',{})
          check = kwargs.get('check')

          if method=='post':
              if is_json:
                 r=requests.post(url,json=data,headers=header,cookies=cookie)
              else:
                  r = requests.post(url,data=data,headers=header,cookies=cookie)
          else:
               r = requests.get(url,params=data,headers=header,cookies=cookie)
          for c in check:
            self.assertIn(c,r.text)
          # self.assertEqual(check.get('error_code'),r.json().get('error_code'))

if __name__=='__main__':
    unittest.main()
    suite= unittest.TestSuite()
    suite.addTests(unittest.makeSuite(MyCase))
    report_html=BeautifulReport.BeautifulReport(suite)
    report_html.report(filename='my_report',description='用例描述')