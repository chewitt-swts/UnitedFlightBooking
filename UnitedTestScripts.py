'''
(PROJECTNAME)TestScripts

This is a template class for building test scripts using functionality
from the ItemSelectorClass
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from UnitedSelectorClass import United_Flight_Booking   # import functionality

import time
import random

#class UnitedTestScripts:

Test = United_Flight_Booking()

Test.open_United()
Test.main_travelers_input_field()
time.sleep(1)
Test.main_travelers_context_menu_seniors_plus_button()
time.sleep(1)
Test.main_travelers_context_menu_seniors_plus_button()
time.sleep(1)
Test.main_travelers_context_menu_seniors_plus_button()
time.sleep(1)
Test.main_travelers_context_menu_seniors_minus_button()
time.sleep(1)
Test.main_travelers_context_menu_seniors_input_field()
time.sleep(1)
Test.main_travelers_context_menu_clear_button()
time.sleep(1)
Test.main_travelers_context_menu_close_button()
time.sleep(1)
Test.close_browser()

'''
begin _TestScripts:
    
    define class variables
    (it should just be TestModule defined as ItemSelectorClass)
    
    define initialization(self):
        create a ItemSelectorClass object called TestModule
        
    define Test_A0():
        try:
            using methods from the ItemSelectorClass, program the steps for Test_A0
            print success message
        except:
            print failure/error message
            
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       
    CONTINUE DOING THIS FOR EVERY SINGLE TEST CASE!!!        

'''