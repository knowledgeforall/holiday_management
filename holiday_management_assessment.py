import datetime
from imghdr import what
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field
from datetime import datetime
from datetime import date
import csv
from config import filelocation

def mainMenu(testHolidayList):
    holidayCount = 0
    holidayCount = testHolidayList.numHolidays()

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
        addAHoliday(testHolidayList)
    elif mainMenuSelect == 2:
        removeAHoliday(testHolidayList)
    elif mainMenuSelect == 3:
        saveHolidayList(testHolidayList)
    elif mainMenuSelect == 4:
        viewHolidays(testHolidayList)
    elif mainMenuSelect == 5:
        exit()

def addAHoliday(testHolidayList):
    
    print("")
    print("Add A Holiday")
    print("==================")
    
    holidayInput = str(input("Please enter the holiday name you would like to add: "))
    dateInput = str(input("Please input the date you would like to add with format YYYY-MM-DD: "))
    dateStrpTime = datetime.strptime(dateInput,"%Y-%m-%d")
    
    #create and populate holidays list
    holiday = Holiday(holidayInput, dateStrpTime)
    testHolidayList.addHoliday(holiday)
    # print to the user that you added a holiday
    print("Success:")
    print("{} has been added to the holiday list".format(holidayObj))
    mainMenu(testHolidayList)
    
def removeAHoliday(testHolidayList):
    
    print("")
    print("Remove A Holiday")
    print("==================")
    
    holidayInput = str(input("Please enter the name of the holiday you would like to remove: "))
    dateInput = str(input("Please input the date you would like to remove with format YYYY-MM-DD: "))
    dateStrpTime = datetime.strptime(dateInput,"%Y-%m-%d")
    
    holiday = Holiday(holidayInput, dateStrpTime)
    
    testHolidayList.removeHoliday(holiday)
    mainMenu(testHolidayList)
    
def saveHolidayList(testHolidayList):
    print("")
    print("Saving Holiday List")
    print("==================")
    saveHoliday = str(input("Are you sure you want to save your changes? [y/n] "))
    if saveHoliday == "y":
        testHolidayList.save_to_json(filelocation)
    elif saveHoliday == "n":
        print("Canceled:")
        print("Holiday list file save canceled.")
        mainMenu(testHolidayList)
            
        
def viewHolidays(testHolidayList):
    wrong_input = True
    
    print("")
    print("View Holidays")
    print("==================")
    
    
    while(wrong_input):
        year = int(input("Which year?: "))
        week = str(input("Which week? #[1-52, Leave blank for the current week]: "))
        if week != "":
            if(int(week) <= 52 and int(week) >= 1):
                week = int(week)
                testHolidayList.displayHolidaysInWeek(year, week)
                wrong_input = False
            else:
                print("Input outside of expected ranges, please try again: ")
        elif week == "":
            week = datetime.now().isocalendar()[1]
            week = int(week)
            testHolidayList.displayHolidaysInWeek(year, week)
            wrong_input = False
    # else:
    mainMenu(testHolidayList)
                
    
def exit():
    print("")
    exit = str(input("Are you sure you want to exit? [y/n]"))
    if exit == "y":
        print("Goodbye!")
        quit()
    elif exit == "n":
        mainMenu(testHolidayList)
          
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
    
    def __str__ (self):
        # String output
        date_format = '%Y-%m-%d'
        date_str = datetime.strftime(self.date, date_format)
        # Holiday output when printed.
        return '%s (%s) ' % (self.name, date_str)
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        
        # Make sure holidayObj is an Holiday Object by checking the type
        if isinstance(holidayObj, Holiday):
        # Use innerHolidays.append(holidayObj) to add holiday
            self.innerHolidays.append(holidayObj)

            #check for and eliminate duplicates
            self.innerHolidays = [i for n, i in enumerate(self.innerHolidays) if i not in self.innerHolidays[n + 1:]]
            
    def findHoliday(HolidayName, Date):
        # Find Holiday in innerHolidays
        # Return Holiday
        self.innerHolidays.__contains__(Holiday(HolidayName,Date))

        for x in self.innerHolidays:
            if x.theHoliday == HolidayName and x.theDate == Date:
                found_holiday = x
        print(found_holiday)
        return(found_holiday)

    def removeHoliday(self, holidayObj):

        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        for i, json in enumerate(self.innerHolidays):
            if json == holidayObj:
                self.innerHolidays.pop(i)
                
        # inform user you deleted the holiday
        print("Success:")
        print("Holiday has been removed from the holiday list.")

    def read_json(self, filelocation):
        with open(filelocation) as file:
            holidayData = json.load(file)
            file.close()
            
        for holiday in holidayData["holidays"]:
            holiday_name = holiday["name"]
            holiday_date = holiday["date"]
            date = datetime.strptime(holiday_date, "%Y-%m-%d" ).date()
            holidayObj = Holiday(holiday_name, date)
            self.addHoliday(holidayObj)

        #removes duplicates in innerHolidays
        self.innerHolidays = [i for n, i in enumerate(self.innerHolidays) if i not in self.innerHolidays[n + 1:]]
        
        return self.innerHolidays
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        jsonHolidays = json.dumps(self.innerHolidays, indent = 4)
        with open(filelocation, 'w') as outfile:
            outfile.write(jsonHolidays)
        
        print("Success:")
        print("Your changes have been saved.")
        
    def scrapeHolidays(self):
        holidays = []
        # Handle any exceptions.
        #setup the soup

         # Remember, 2 previous years, current year, and 2 years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        for i in range(2020,2025):
            url = 'https://www.timeanddate.com/holidays/us/{}?hol=33554809'
            url = url.format(i)
            year = i
            response = requests.get(url)
            rawhtml = response.text
            
            soup = BeautifulSoup(rawhtml, 'html.parser')
            
            tablerow = soup.find_all('tr',attrs = {'class':'showrow'})
            for row in tablerow:
                anchorlink = row.find('a')
                name = anchorlink.text
                thtag = row.find('th')
                date = str(year) + " " + thtag.text
                datestrp = datetime.strptime(date, "%Y %b %d" ).date()

                holiday = Holiday(name, datestrp)
                self.addHoliday(holiday)

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(self, year, week):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        holidays = []
        if(not (isinstance(week, int))):
            raise ValueError()
        
        if(not (isinstance(year, int))):
            raise ValueError()
        
        holidays = list(filter(lambda x : x.date.isocalendar()[0] == year and x.date.isocalendar()[1] == week, self.innerHolidays))
        return holidays
        # self.displayHolidaysInWeek(year, week)

    def displayHolidaysInWeek(self, year, week):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        
        print("These are the holidays for {} week {}".format(year, week))
        
        weekHolidays = self.filter_holidays_by_week(year, week)
        for holidays in weekHolidays:
            print(holidays)

    def getWeather(weekNum):
        print("getWeather() method will run here")
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        pass
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
    testHolidayList = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    testHolidayList.read_json(filelocation)
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    testHolidayList.scrapeHolidays()
    # 3. Create while loop for user to keep adding or working with the Calender
    
    # 4. Display User Menu (Print the menu)
    mainMenu(testHolidayList)
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