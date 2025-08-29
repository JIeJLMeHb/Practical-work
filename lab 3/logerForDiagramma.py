def logger(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper