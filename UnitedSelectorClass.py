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