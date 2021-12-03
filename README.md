# ICT2101-2201-Team-Project

## Team Members
- Ong Sheng Wei Kenrick (2000909)
- Png Han Zheng (2000970)
- Chong Fu Min (2002039)
- Fashshila Yasmin D/o Mohammed Yunoos (2001301)
- Lee Yen Ning (2001775)

## Getting Started (for windows)
- Make sure you have at least Python 3.8.5 and Visual Studio Code

## Setup
**Clone the Project Repo**
1. Open a shell and navigate to desired directory to save the project folder
2. Execute the git clone command
**Setting up the Project Environment**
1. Create and activate a virtual environment named .venv
(py -3 -m venv .venv
.venv\scripts\activate)
2. Open the Command Palette and select interprete in your project folder that starts with ./.venv or .\.venv
3. Execute the command python -m pip install --upgrade pip and python -m pip install flask

**How to run**
1. Navigate to the root directory of the project (where app.py is)
2. Start the debugger by selecting the Run > Start Debugging 
3. Open Google chrome and navigate to http://127.0.0.1:5000/

## Work Distribution
**Branch Management**

## Black Box Testing
**System State Diagram**

**System Test Cases**

![test case ss1](https://user-images.githubusercontent.com/73540954/144647626-88e5e8a5-705b-48cc-b492-e6ee54313cdb.JPG)
![test case ss2](https://user-images.githubusercontent.com/73540954/144647630-4a2c0978-8941-45fe-b4a0-4e3cb9a4263d.JPG)
**System Test Video**
## White Box Testing
**Selected Class for White Box Testing**

**Car controller class**

We have chosen car controller class as we feel that it is the most important and interesting class. The backend logic of the connection from the robotic car and the website is located inside this car controller class. One of the functions "Send Data" is used for sending the difficulty level for the car to read its movement instructions from. One other function "Read Data" is used by our website to display the data of the car onto our dashboard.

**Test Cases**

We have implemented 3 different test cases for statement coverage testing. The 3 test cases are as follow:
1. The first test case is to check when there are no obstacles and the car is not connected

**White Box Testing Video**
