# This is the beginning of my python program

# Boghos youseef
# 11/10/2021




# This python program will serve as a testing file for my abilities in threading




# import statements


import threading
import time
import random
from datetime import datetime

def operationTimer(func):

    def inner(x, _id):
        start_time = datetime.now() 
        print(f"(Operation: {_id} Started-{datetime.now()})"+"-"*20) 
        func(x, _id)
        elapsed_time = datetime.now() - start_time
        print(f"(Operation: {_id} lasted {elapsed_time})-"+"-"*20)

    return inner

@operationTimer
def myFunc(x, _id):
    
    while x < 10:

        print(f"{_id} = {x}")
        
        x+= random.choice([0.5, 1, 2])
        time.sleep(random.choice([1, 1.5, 2]))

t_start = time.perf_counter()

first_var = 1

second_var = 1

third_var = 1


first_thread = threading.Thread(target=myFunc, args =[first_var, "first thread"])

second_thread = threading.Thread(target=myFunc, args =[second_var,"second thread"])

third_thread = threading.Thread(target=myFunc, args =[second_var,"third thread"])

first_thread.start()
second_thread.start()
third_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()


t_end = time.perf_counter()

print(f"program is finished in {t_end - t_start} seconds")




