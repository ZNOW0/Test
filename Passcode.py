passcode = "X"
passcode_input = "X"
PassState = True
CheckState = True


def passcode_set():
    global passcode
    global PassState

    while PassState:
        try:
            passcode = str(input("Enter passcode of choice:"))
            Pass = open("password.txt", "w+")
            Pass.write(passcode)
            Pass.close()
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

passcode_set()



