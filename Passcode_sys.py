import random
import time
from random import randint
from time import perf_counter


passcode = "X"
passcode_input = "X"
PassState = True
CheckState = True

def passcode_set():
    global passcode
    global PassState


    while PassState:
        try:
            passcode = int(input("Enter passcode of choice:"))
            PassState = False
            print("passcode sucsesfully set")
        except:
            print("Only numbers are allowed")

def passcode_check():
    global CheckState
    global passcode_input

    CheckState = True
    Passcode_count = 0


    while CheckState:
        try:
            passcode_input = int(input("Enter passcode for auth:"))
        except:
            pass

        if passcode_input == passcode:
            print("Correct passcode, acces granted")
            CheckState = False
        else:
            print("passcode incorrect")
            Passcode_count += 1
            if Passcode_count == 3:
                CheckState = False
                print("Too many tries")
            else:
                pass
        

def pass_save():
    Pass = open("password.txt", "w+")
    Pass.write(str(passcode_input))
    Pass.close()

passcode_set()
passcode_check()
