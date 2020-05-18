passcode = "X"
Pass = "X"
PassState = True
CheckState = True


def passcode_set():
    global passcode
    global PassState
    global Pass

    while PassState:
        try:
            Pass = open("password.txt", "w+")
            Pass.write(str(input("Enter passcode of choice:")))
            Pass.close()
            PassState = False
            print("passcode sucsesfully set")
        except:
            print("Only numbers are allowed")

def passcode_check():
    global CheckState
    global passcode
    global Pass


    Pass = open("password.txt", "r+")
    passcode = Pass.read()
    Pass.close()


    CheckState = True
    Passcode_count = 0

    while CheckState:
        try:
            pass = int(input("Enter passcode for auth:"))
        except:
            pass

        if passcode == pass:
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
