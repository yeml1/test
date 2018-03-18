import sys,os,unittest,BeautifulReport

BASE_PATH=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
sys.path.insert(0,BASE_PATH)
from common.tools import import GetCase
from conf.setting import PY_PATH,REPORT_PATH

def run():
    g=GetCase()
    g.creat_py() # 生存测试文件
    suite=unittest.TestSuite()
    all_case=unittest.defaultTestLoader.discover(PY_PATH,'Test*.py') # 所有的测试用例
    [suite.addTests(case) for case in all_case]
    report_obj=BeautifulReport.BeautifulReport(suite)
    report_obj.report(filename='utp',log_path=REPORT_PATH,description='utp测试报告')

run()
