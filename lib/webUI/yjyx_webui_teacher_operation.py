"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/03
@File   :yjyx_webui_teacher_operation.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from cfg.cfg import *
import time
from hytest import *
from selenium.webdriver.common.action_chains import ActionChains

teacher_operation = TeacherOperation()
if __name__ == '__main__':
	teacher_operation.teacher_login('jcyrss','sdfsdf5%')
	time.sleep(2)
	teacher_operation.get_class_student_info()
	