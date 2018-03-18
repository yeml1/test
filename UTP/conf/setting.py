import os

BASE_PATH=os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)) # 取上级目录

CASE_PATH=os.path.join(BASE_PATH,'data') # 用例的目录
LOG_PATH=os.path.join(BASE_PATH,'logs') # 用例的目录
REPORT_PATH=os.path.join(BASE_PATH,'report') # 报告的目录
CASE_EG=os.path.join(BASE_PATH,'conf','base_case.eg') # 用例模版对路径

BASE_URL='http://api.nnzhp.cn/'
