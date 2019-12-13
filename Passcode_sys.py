import random
import time
from random import randint
from time import perf_counter

passcode_input = "X"
passcode = "X"
State = True

def passcode_set():
    global passcode
    global State

    State = True

    while State:
        try:
            passcode = int(input("Enter your passcode of choice:"))
            print("passcode sucsesfully set")
            State = False
        except:
            print("Only numbers are allowed")

def passcode_check():
    global passcode_input
    global State

    State = True
    Passcode_count = 0


    while State:
        try:
            passcode_input = int(input("Enter auth:"))
        except:
            pass

        if passcode_input == passcode:
            print("Correct passcode, acces granted")
            State = False
        else:
            print("passcode incorrect")
            Passcode_count += 1
            if Passcode_count == 3:
                print("Too many tries")
                State = False
            else:
                pass
        
passcode_set()
passcode_check()

