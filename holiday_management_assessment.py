import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field
from datetime import datetime
from datetime import date
import csv

def mainMenu():
    # holidayCount = 0

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
    global holidayInput
    global datestrptime
    
    print("")
    print("Add A Holiday")
    print("==================")
    
    holidayInput = str(input("Please enter the holiday name you would like to add: "))
    dateInput = str(input("Please input the date you would like to add with format YYYY-MM-DD: "))
    datestrptime = datetime.strptime(dateInput,"%Y-%m-%d")
    
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    
    # holidayData = ['holidayInput', 'dateInput']
    
    # with open('Holidays.csv', 'w') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(holidayData)
    
    # addHoliday(holidayObj)
    
def removeAHoliday():
    global holidayInput
    global datestrptime
    
    print("")
    print("Remove A Holiday")
    print("==================")
    holidayInput = str(input("Please enter the name of the holiday you would like to remove: "))
    dateInput = str(input("Please input the date you would like to remove with format YYYY-MM-DD: "))
    datestrptime = datetime.strptime(dateInput,"%Y-%m-%d")
    
    
    
    HolidayList.removeHoliday(HolidayName, Date)
    
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
          
# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

@dataclass
class Holiday:
    name: str
    date: datetime
        
#setup the soup
url = 'https://www.timeanddate.com/holidays/us/2022?hol=33554809'
print(url)

response = requests.get(url)
rawhtml = response.text
#parse the HTML
soup = BeautifulSoup(rawhtml, 'html.parser')

tablerow = soup.find_all('tr',attrs = {'data-mask':'1'})
for row in tablerow:
    anchorlink = row.find('a')
    name = anchorlink.text
    print(name)
    thtag = row.find('th')
    date = "2022 " + thtag.text
    datestrp = datetime.strptime(date, "%Y %b %d" ).date()
    print(datestrp)
    
    holiday = Holiday(name, datestrp)
    holidays.append(holiday)
    
    list_dictionary_holidays = [holidayObj.__dict__ for holidayObj in holidays]

with open("holidaysScraped.json", 'w') as file:
    json.dump(list_dictionary_holidays, file, default=str)
    
print(list_dictionary_holidays)
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(holidayObj):
        global holidayInput
        global datestrptime
        
        print("addHoliday() method will run here")
        # Make sure holidayObj is an Holiday Object by checking the type
        type(holidayObj)
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        print("Success:")
        print("{} ({}) has been added to the holiday list".format(holidayInput, date))

    def findHoliday(HolidayName, Date):
        print("findHoliday() method will run here")
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(HolidayName, Date):
        global holidayInput
        global datestrptime
        
        print("removeHoliday() method will run here")
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        print("Success:")
        print("{} has been removed from the holiday list.".format(holidayInput))

    def read_json(filelocation):
        print("read_json() method will run here")
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(filelocation):
        print("save_to_json() method will run here")
        # Write out json file to selected file.
        
        print("Success:")
        print("Your changes have been saved.".format(holidayInput))
        
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