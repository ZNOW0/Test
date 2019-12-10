import random
import time
from random import randint
from time import perf_counter


state = True
while state:
    print("Enter your passcode of choice")
    try:
        passcode = int(input())
        print("passcode sucsesfully set")
        state = False
    except:
        print("Only numbers are allowed")

def passcode_check():
    State = True
    Passcode_count = 0
    print("Enter auth")
    while State:
        try:
            passcode_input = int(input())
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
        

passcode_check()
