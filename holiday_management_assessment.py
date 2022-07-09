import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field
from datetime import date

def mainMenu():
    holidayCount = 0

    print("Holiday Management")
    print("==================")
    print("There are {} holidays stored in the system.".format(holidayCount))
    print("")
    print("Holiday Menu")
    print("==================")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")

    mainMenuSelect = int(input("Enter your selection: "))
    if mainMenuSelect == 1:
        addAHoliday()
    elif mainMenuSelect == 2:
        removeAHoliday()
    elif mainMenuSelect == 3:
        saveHolidayList()
    elif mainMenuSelect == 4:
        viewHolidays()
    elif mainMenuSelect == 5:
        exit()

def addAHoliday():
    print("")
    print("Add A Holiday")
    print("==================")
    holidayInput = str(input("Please enter the holiday name you would like to add: "))
    dateInput = date(input("Please input the date you would like to add with format MM/DD/YY: "))
    
def removeAHoliday():
    print("")
    print("Remove A Holiday")
    print("==================")
    removeHoliday = str(input("Please enter the name of the holiday you would like to remove: "))
    
def saveHolidayList():
    print("")
    print("Saving Holiday List")
    print("==================")
    saveHoliday = str(input("Are you sure you want to save your changes? [y/n] "))
    # if saveHoliday == "y":
        
def viewHolidays():
    print("")
    print("View Holidays")
    print("==================")
    whichYear = str(input("Which year?"))
    whichWeek = str(input("Which week?"))
    
def exit():
    print("")
    exit = str(input("Are you sure you want to exit? [y/n]"))
    # if 
    # if exit == "y":
    #     print("Goodbye!")
    #     quit()
    # elif exit == "n":
        

    # if mainMenuSelect == "1":
    #     # HolidayList.addHoliday()
    # elif mainMenuSelect == "2":
    #     # HolidayList.removeHoliday()
    # elif mainMenuSelect == "3":
    #     # HolidayList.save_to_json()
    # elif mainMenuSelect == "4":
    #     # do something else
    # elif (or else?) mainMenuSelect == "5":
    #     # do something else
          
# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

@dataclass
class Holiday:
    name: str
    date: date
    
# class Holiday:
      
#     def __init__(self,name, date):
#         """Holiday class"""
#         self._name = name
#         self._date = date
        
#     # @property
#     # def name(self):
#     #     return self._name
    
#     # @property
#     # def date(self):
#     # return self._date

#     # @name.setter
#     # def name(self, new_name):
#     #     self.__name = new_name
        
#     # @date.setter
#     # def date(self, new_date):
#     #     self.__date = new_date
    
#     def __str__ (self):
#         # String output
#         return self._name
#         return self._date
#         # Holiday output when printed.
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(holidayObj):
        print("addHoliday() method will run here")
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

    def findHoliday(HolidayName, Date):
        print("findHoliday() method will run here")
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(HolidayName, Date):
        print("removeHoliday() method will run here")
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(filelocation):
        print("read_json() method will run here")
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(filelocation):
        print("save_to_json() method will run here")
        # Write out json file to selected file.
        
    def scrapeHolidays():
        print("scrapeHoliday() method will run here")
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays():
        print("numHoliday() method will run here")
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(year, week_number):
        print("filter_holidays_by_week() method will run here")
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        print("displayHolidaysInWeek() method will run here")
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        print("getWeather() method will run here")
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        print("viewCurrentWeek() method will run here")
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



def main():
    print("main() function running")
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    mainMenu()
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.