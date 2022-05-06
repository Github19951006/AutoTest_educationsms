"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/06
@File   :__st__.py
"""

from hytest import *
from cfg.cfg import *
from lib.api.yjyx_student_api import gs_student
from lib.webUI.yjyx_webui_student_operation import student_operation

# 初始化
def suite_setup():
	
	cid = GSTORE['id']
	result_add_student = gs_student.add_students(
		'student_yuer', '精锐', SENIOR_THREE_GRADE_ID, cid, '13451813456')
	
	GSTORE['student_id'] = result_add_student.json()['id']
	
# 清除方法
def suite_teardown():
	
	gs_student.del_students(GSTORE['student_id'])
	student_operation.close_chrome()