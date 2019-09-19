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

#Test Series 1: Testing that all elements on United.com's main page flight search can be selected and values can be entered/manipulated

Test.open_United() #begins test by opening website
Test.book_with_miles_checkbox() #TCID #FS001 - can this checkbox be selected?
time.sleep(2)
Test.book_with_miles_checkbox() #unchecking the checkbox to proceed with the next test in this series
Test.oneway_radio_button() #TCID #FS002
Test.roundtrip_radio_button() #TCID #FS003
Test.calendar_shop_checkbox() #TCID #00009
Test.calendar_shop_checkbox()#unchecking the checkbox to proceed with the next test in this series
Test.departing_airport_input_field()
Test.destination_airport_input_field()
Test.roundtrip_departing_date_field()
Test.roundtrip_calendar_left_scroll_button()
Test.roundtrip_calendar_right_scroll_button()
Test.roundtrip_return_date_field()
Test.main_travelers_input_field()
Test.main_travelers_context_menu_adults_input_field() #entering keystrokes directly into the Adults input field to change the number of Adult travelers rather than manipulating the GUI
Test.main_travelers_context_menu_clear_button() #clearing previous entry of Adult travelers
Test.main_travelers_context_menu_adults_plus_button() #adding Adult travelers by manipulating the GUI
Test.main_travelers_context_menu_adults_plus_button()
Test.main_travelers_context_menu_adults_minus_button() #removing Adult travelers by manipulating the GUI
Test.main_travelers_context_menu_seniors_input_field() #entering keystrokes directly into the Seniors input field to change the number of Senior travelers rather than manipulating the GUI
Test.main_travelers_context_menu_seniors_plus_button() #adding Senior travelers by manipulating the GUI
Test.main_travelers_context_menu_seniors_minus_button() #removing Senior travelers by manipulating the GUI
Test.main_travelers_context_menu_infants_input_field()
Test.main_travelers_context_menu_infants_plus_button()
Test.main_travelers_context_menu_infants_minus_button()

Test.main_travelers_context_menu_close_button()

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