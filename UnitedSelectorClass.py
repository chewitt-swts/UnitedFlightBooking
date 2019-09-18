'''
(PROJECTNAME)ItemSelectorClass Template

This is a template class for accessing and selecting elements on a web page.

METHOD ASSUMPTIONS:

THERE IS A TRY/EXCEPT CLAUSE FOR EVERY SINGLE METHOD!! THIS IS NOT SHOWN FOR EVERY ONE
BUT IT IS IMPLIED! A single function failure should not mean the whole class fails.

Confirmation messages are also implied

The methods are organized into how (I feel) they should be designed based on the element we are interacting with
(button, select, radio button, etc.)
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random

class United_Flight_Booking:
    chrome_options = webdriver.ChromeOptions

    driver = webdriver
    wait = WebDriverWait

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)

    def loadtime(self):
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        # Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s" % backendPerformance_calc)
        print("Front End: %s" % frontendPerformance_calc)
        return

    def close_browser(self):
        self.driver.quit()

    def open_United(self):
        self.driver.get('http://www.united.com')

#The below methods are to select the search elements contained on the United.com home page.
    #This method is to select the radio button labeled "Roundtrip" on the United.com home page.
    def roundtrip_radio_button(self):
        try:
            RoundtripRadioButton = self.driver.find_element_by_id('roundtrip')
            RoundtripRadioButton.click()
            print('Roundtrip Radio Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def oneway_radio_button(self):
        try:
            OnewayRadioButton = self.driver.find_element_by_id('oneway')
            OnewayRadioButton.click()
            print('Oneway Radio Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def book_with_miles_checkbox(self):
        try:
            BookWithMilesCheckbox = self.driver.find_element_by_id('award')
            BookWithMilesCheckbox.click()
            print('Book With Miles Checkbox has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def calendar_shop_checkbox(self):
        try:
            CalendarShopCheckbox = self.driver.find_element_by_id('flexDatesLabel')
            CalendarShopCheckbox.click()
            print('Calendar Shop Checkbox has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def departing_airport_input_field(self):
        try:
            DepartingAirportInputField = self.driver.find_element_by_id('bookFlightOriginInput')
            DepartingAirportInputField.click()
            print('Departing Airport Input Field has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def destination_airport_input_field(self):
        try:
            DestinationAirportInputField = self.driver.find_element_by_id('bookFlightDestinationInput')
            DestinationAirportInputField.click()
            print('Destination Airport Input Field has been clicked successfully.')
        except Exception as err:
            print(str(err))
#TODO figure out how to select each element in the calendar context menu, particularly individual date selection -- and randomizing selecting a date from the menu, as opposed to hardcoding it by sending keys to the input field/dialogue box.

    def roundtrip_departing_date_field(self):
        try:
            RoundtripDepartingDateField = self.driver.find_element_by_id('DepartDate')
            RoundtripDepartingDateField.click()
            print('Roundtrip Departing Date Field has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def roundtrip_return_date_field(self):
        try:
            RoundtripReturnDateField = self.driver.find_element_by_id('ReturnDate')
            RoundtripReturnDateField.click()
            print('Roundtrip Return Date Field has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def roundtrip_calendar_left_scroll_button(self):
        try:
            CalendarLeftScrollButton = self.driver.find_element_by_xpath("//button[@aria-label='Move backward to switch to the previous month.']")
            CalendarLeftScrollButton.click()
            print('Calendar Left Scroll Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def roundtrip_calendar_right_scroll_button(self):
        try:
            CalendarRightScrollButton = self.driver.find_element_by_xpath("//button[@aria-label='Move forward to switch to the next month.']")
            CalendarRightScrollButton.click()
            print('Calendar Right Scroll Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def main_travelers_input_field(self):
        try:
            MainTravelersInputField = self.driver.find_element_by_id('bookFlightModel.passengers')
            MainTravelersInputField.click()
            print('Main Page Travelers Input Field has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_close_button(self):
        try:
            MainTravelersContextMenuCloseButton = self.driver.find_element_by_id('passengersCloseBtn')
            MainTravelersContextMenuCloseButton.click()
            print('Main Page Travelers Context Menu Close Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_clear_button(self):
        try:
            MainTravelersContextMenuClearButton = self.driver.find_element_by_id('clearPassengers')
            MainTravelersContextMenuClearButton.click()
            print('Main Page Travelers Context Menu Clear Button has been clicked successfully.')
        except Exception as err:
            print(str(err))
#TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging.
    #this method is does not work when assembled in an action chain; you must click the input field element first and then give a separate command to send_keys in order to change the input value from 1(default) to 3(or randomized)
    def main_travelers_context_menu_adults_input_field(self):
        try:
            MainTravelersContextMenuAdultsInputField = self.driver.find_element_by_id('NumOfAdults')
            MainTravelersContextMenuAdultsInputField.click()
            MainTravelersContextMenuAdultsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Adults Input Field has successfully received input to assign the number of Adult Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Adults in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Adult Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_adults_plus_button(self):
        try:
            MainTravelersContextMenuAdultsPlusButton = self.driver.find_element_by_id('NumOfAdults plusBtn')
            MainTravelersContextMenuAdultsPlusButton.click()
            print('The number of Adult Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Adults in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Adult Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_adults_minus_button(self):
        try:
            MainTravelersContextMenuAdultsMinusButton = self.driver.find_element_by_id('NumOfAdults minusBtn')
            MainTravelersContextMenuAdultsMinusButton.click()
            print('The number of Adult Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging.
    def main_travelers_context_menu_seniors_input_field(self):
        try:
            MainTravelersContextMenuSeniorsInputField = self.driver.find_element_by_id('NumOfSeniors')
            MainTravelersContextMenuSeniorsInputField.click()
            MainTravelersContextMenuSeniorsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Seniors Input Field has successfully received input to assign the number of Senior Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Seniors in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Senior Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_seniors_plus_button(self):
        try:
            MainTravelersContextMenuSeniorsPlusButton = self.driver.find_element_by_id('NumOfSeniors plusBtn')
            MainTravelersContextMenuSeniorsPlusButton.click()
            print('The number of Seniors Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Seniors in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Seniors Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_seniors_minus_button(self):
        try:
            MainTravelersContextMenuSeniorsMinusButton = self.driver.find_element_by_id('NumOfSeniors minusBtn')
            MainTravelersContextMenuSeniorsMinusButton.click()
            print('The number of Seniors Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infants_input_field(self):
        try:
            MainTravelersContextMenuInfantsInputField = self.driver.find_element_by_id('NumOfInfants')
            MainTravelersContextMenuInfantsInputField.click()
            MainTravelersContextMenuInfantsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Infants Under 2 Input Field has successfully received input to assign the number of Infant Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Infants Under 2 in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Infant Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infants_plus_button(self):
        try:
            MainTravelersContextMenuInfantsPlusButton = self.driver.find_element_by_id('NumOfInfants plusBtn')
            MainTravelersContextMenuInfantsPlusButton.click()
            print('The number of Infant Under 2 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Infants in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Infant Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_infants_minus_button(self):
        try:
            MainTravelersContextMenuInfantsMinusButton = self.driver.find_element_by_id('NumOfInfants minusBtn')
            MainTravelersContextMenuInfantsMinusButton.click()
            print('The number of Infant Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infantsonlap_input_field(self):
        try:
            MainTravelersContextMenuInfantsOnLapInputField = self.driver.find_element_by_id('NumOfLapInfants')
            MainTravelersContextMenuInfantsOnLapInputField.click()
            MainTravelersContextMenuInfantsOnLapInputField.send_keys('3')
            print('Main Page Travelers Context Menu Infants On Lap Input Field has successfully received input to assign the number of Infant On Lap Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Infants On Lap in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Infant On Lap Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infantsonlap_plus_button(self):
        try:
            MainTravelersContextMenuInfantsOnLapPlusButton = self.driver.find_element_by_id('NumOfLapInfants plusBtn')
            MainTravelersContextMenuInfantsOnLapPlusButton.click()
            print('The number of Infant On Lap Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Infants On Lap in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Infants On Lap Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_infantsonlap_minus_button(self):
        try:
            MainTravelersContextMenuInfantsOnLapMinusButton = self.driver.find_element_by_id('NumOfLapInfants minusBtn')
            MainTravelersContextMenuInfantsOnLapMinusButton.click()
            print('The number of Infant On Lap Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))
'''
begin _ItemSelectorClass:

    define class variables here
    ex: driver = webdriver, wait = WebDriverWait
    
    define initialization method(self):
        initialize class variables
        ex. self.driver = webdriver.Chrome(chromepath)
    
    define ItemSelection BUTTON method(self):
        TRY:
            use explicit wait to find the element
            then click using an action chain
            print success message
        EXCEPT:
            print error message
        
    define ItemSelection SELECT method(self, index): < index arg lets you select a choice from outside the class
        try:
            use explicit wait to find the element
            select the index that is passed as an argument
            print success message
        except:
            print error message
            
    define ItemSelection RADIO method(self, index)
        try:
            create an if-else statement that selects the radio button based on the index (case-switch works too, probably better)
            i.e.
            if index == 0
                choose radio button option 0 (you will likely need to find this element via label)
                explicit wait doesnt always work here, might have to use a time.sleep
            else if index == 1
                same thing but next label
            else if index == 2
                same thing but next label
            
            print success message
        except:
            print error message
            
    define ItemSelection INPUT method(self, text)
        try:
            use explicit wait to find the input element
            use an action chain to click the element, then sendkeys "text"
            print success message
        except:
            print error message
'''