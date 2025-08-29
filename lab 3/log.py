import os
import datetime
import pandas as pd

User = os.getlogin()         

def date():
    Date = datetime.datetime.now().strftime('%Y-%m-%d')       
    return Date
def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')      
    return Time
    

def logger(function):
    def wrapper(*args, **kwargs):
        result  = function(*args, **kwargs)
        function_name = function.__name__
        if os.path.isfile("UwU-Stalin-UwU's\lab 3\logs.csv"):
            csv = pd.read_csv("UwU-Stalin-UwU's\lab 3\logs.csv")
            columns = {'': [len(csv)], "Users": [User], "Actions": [function_name], "Date": [date()], "Time":[time()]}
            dataFrame = pd.DataFrame(columns)
            dataFrame.to_csv("UwU-Stalin-UwU's\lab 3\logs.csv", mode = 'a', index = False, header = False)
        else:
            columns = {"Users": [User], "Actions": [function_name], "Date": [date()], "Time":[time()]}
            dataFrame = pd.DataFrame(columns)
            dataFrame.to_csv("UwU-Stalin-UwU's\lab 3\logs.csv")
        return result
    return wrapper
    
@logger
def proga():
    print("damn done")