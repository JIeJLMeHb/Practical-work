from datetime import datetime
import os
import pandas as pd


def logging(func):                                               #Decorator
    def wrapper(*args, **kwargs):
        user_func = func
        orig = func(*args, **kwargs)
        user_func_name = str(user_func.__name__)
        user_name = os.getlogin()
        time_act = str(datetime.now().time())
        day_act =  str(datetime.now().date())
        logs = 'logs.csv'
        if os.path.isfile(logs):                                                                                          #If csv file exists
            file_df = pd.read_csv(logs)
            data = {'': [len(file_df)], 'User': [user_name], 'Func': [user_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv',header=False, index=False, mode='a')
        else:                                                                                                             #If csv file doesn't exist
            data = {'User': [user_name], 'Func': [user_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv')
        return orig
    return wrapper

@logging
def hi():                                                                                                              #Test func
    print('hello')

def main():
    #for i in range(200):
        #pr()
    hi()

if __name__ == "__main__":
    main()