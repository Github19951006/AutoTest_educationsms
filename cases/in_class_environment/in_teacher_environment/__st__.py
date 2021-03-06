"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/28
@File   :__st__.py.py
"""
from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher

# 初始化
def suite_setup():
	
	INFO('添加一个老师')
	cid = GSTORE['id']
	res_add_teacher = gs_teacher.add_teachers('new_teacher', '初始化老师',
	                        SUBJECT_ID_JUNIOR_MATH, str(cid), '13451813456', 'jcysdf@123.com',
	                        '3209251983090987899')

	ret_add_teacher_json = res_add_teacher.json()
	teacher_id = ret_add_teacher_json['id']
	INFO(teacher_id)
	
	# res_list_teacher = gs_teacher.list_teachers()
	# res_list_teacher_json = res_list_teacher.json()
	# INFO(res_list_teacher_json)
	
	# 存储 全局共享 数据
	GSTORE['teacher_id'] = teacher_id
	
# 清除方法
def suite_teardown():
	teacher_id = GSTORE['teacher_id']
	gs_teacher.del_teachers(teacher_id)