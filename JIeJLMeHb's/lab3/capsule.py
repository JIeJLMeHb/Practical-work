from datetime import datetime
import os
import pandas as pd


def logging(func):
    def wrapper(*args, **kwargs):
        user_func = func
        orig = func(*args, **kwargs)
        user_func_name = str(user_func.__name__)
        user_name = os.getlogin()
        time_act = str(datetime.now().time())
        day_act =  str(datetime.now().date())
        logs = "JIeJLMeHb's/lab3/logs.csv"
        if os.path.isfile(logs):
            file_df = pd.read_csv(logs)
            data = {'': [len(file_df)], 'User': [user_name], 'Func': [user_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv("JIeJLMeHb's/lab3/logs.csv",header=False, index=False, mode='a')
        else:
            data = {'User': [user_name], 'Func': [user_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv("JIeJLMeHb's/lab3/logs.csv")
        return orig
    return wrapper

@logging
def hello():                                                                                                              
    print('hello')

def main():
    hello()

if __name__ == "__main__":
    main()
    