# This is the beginning of my python program

# Boghos youseef
# 11/10/2021




# This python program will serve as a testing file for my abilities in threading




# import statements


import threading


def myFunc(x):
    print(x)


first_var = "񬠜"

second_var = "ᨊ"


first_thread = threading.Thread(myFunc, [first_var])

first_thread = threading.Thread(myFunc, [second_var])

first_thread.run()
second_thread.run()


