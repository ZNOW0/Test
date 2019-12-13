import random
import time
from random import randint
from time import perf_counter


passcode = "X"
PassState = True
CheckState = True

def passcode_set():
    global passcode
    global state

    while PassState:
        print("Enter your passcode of choice")
        try:
            passcode = int(input())
            print("passcode sucsesfully set")
            PassState = False
        except:
            print("Only numbers are allowed")

def passcode_check():
    global CheckState

    CheckState = True
    Passcode_count = 0

    print("Enter auth")

    while CheckState:
        try:
            passcode_input = int(input())
        except:
            pass

        if passcode_input == passcode:
            print("Correct passcode, acces granted")
            CheckState = False
        else:
            print("passcode incorrect")
            Passcode_count += 1
            if Passcode_count == 3:
                print("Too many tries")
                CheckState = False
            else:
                pass
        
passcode_set()
passcode_check()
