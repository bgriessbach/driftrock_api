## Installation instructions
Please download or clone this repository.   
Please consider using a virtual enviroment to install all dependencies and avoid dependency conflicts in other apps. (see http://docs.python-guide.org/en/latest/dev/virtualenvs/).  
This app was created using Python 3. Please install Python 3 as needed.  
This app also uses the requests library. In Python 3, requests needs to be installed via "pip install requests".  

## Usage
(This app was created and tested only in Windows 10)   
Please navigate to the root folder of the app.  
Start the virtual environment as needed.  
Run "python3 COMMAND [EMAIL]".  
The available commands are:  
* most_sold: What is the name of the most sold item?
* total_spend [EMAIL]: What is the total spend of the user with this email address [EMAIL]?
* most_loyal: What is the email address of the most loyal user (most purchases)?

## Test
This package contains 2 unit tests.  
Navigate to the root folder of this app.  
Run "python3 unit_test.py" .  
Two functions are tested in isolation with predetermined datasets. 
Each test has the same 3 checks:    
1. Outcome if input data is empty
2. Outcome with small input dataset. 
3. Outcome with inconclusive dataset (Not just 1 item as solution).  

Per function, the tests print out the input data, expected and received answer. When all 3 tests ran, there is a print summary of Pass/Fails in an array structure. 

