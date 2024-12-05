

import time 
def time_it(function):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        total_time = (end - start) * 1000
        print(function.__name__ + f"taken {total_time} mil sec")
        return result
    return wrapper
