import unittest,requests
from conf.setting import BASE_URL
from common.db_mysql import db

class TestCj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url=BASE_URL  # 方便后面直接调用
    @classmethod
    def tearDownClass(cls): # 注册过的不能再注册了，删掉它
        db.execute('delete from app_myuser where username="ybq222";')
    def Reg(self):
        url=self.url+'/api/user/user_reg'
        data={
            'username':'ybq222',
            'pwd':'aA123456',
            'cpwd': 'aA123456',
        }
        res=requests.post(url,data=data).text
        self.assertIn('注册成功',res)

    def Login(self):
        self.Reg()
        url='http://api.nnzhp.cn/api/user/login'
        data={'username':'ybq222','passwd':'aA123456'}
        res =requests.post(url,data=data).json()
        user_id=res.get('login_info').get('userId')
        sign=res.get('login_info').get('sign')
        self.assertTrue('userId' in str(res))
        self.assertTrue('sign' in str(res))
        return user_id,sign
    def testCj(self):
        userid,sign =self.Login()
        url='http://api.nnzhp.cn/api/product/choice'
        data={'userid':userid,'sign':sign}
        res=requests.get(url,params=data).text
        print('中间信息。。。',res)
        self.assertTrue('product_name'in res)
        self.assertTrue('imgUrl'in res)

if __name__=='__main__':
        unittest.main()
