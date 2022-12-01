"""
Created by Roman Sekandari. but honestly who gives a fuck.
"""
"""
The following program is made for OCD people.
It creates a folder for the course you want, and extra folders for the books, exercises, lectures etc.
It's really simple but it takes time to do it manually and fuck doing that.
"""
import os

# Ask user for path
path = input('Enter the path you want to create the folder in: ')

# What is the name of the course?
courseName = input('Enter the name of the course: ')

# Create the folder with name courseName
os.mkdir(os.path.join(path, courseName))

# Create the subfolders you can always add more
os.mkdir(os.path.join(path, courseName, courseName + '_Books'))
os.mkdir(os.path.join(path, courseName, courseName + '_Assignments'))
os.mkdir(os.path.join(path, courseName, courseName + '_Lectures'))
os.mkdir(os.path.join(path, courseName, courseName + '_Exercises'))
os.mkdir(os.path.join(path, courseName, courseName + '_EXAM'))


# Ask user for number of weeks
totalWeeks = int(input('How many weeks is the course?: '))

# Create the folders in the assignments, lectures and exercises subfolders
for i in range(1, totalWeeks+1):
    os.mkdir(os.path.join(path, courseName, courseName + '_Assignments', 'Week'+str(i)+'_Assignment'))
    os.mkdir(os.path.join(path, courseName, courseName + '_Lectures', 'Week'+str(i)+'_Lectures'))
    os.mkdir(os.path.join(path, courseName, courseName + '_Lectures', 'Week' + str(i) + '_Lectures', '0' + str(i) + '_Slides'))
    os.mkdir(os.path.join(path, courseName, courseName + '_Exercises', 'Week'+str(i)+'_Exercises'))

print('xD Cringe, your course folder created. You can now start organizing your course!')