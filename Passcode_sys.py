
Status_create = open("Status.txt", "a+")
Status_create.close()


passcode = "X"
Pass = "X"
status = "X"
Granted = "X"
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
            Status_write = open("Status.txt", "w+")
            Status_write.write("1")
            Status_write.close()
            PassState = False
            print("passcode sucsesfully set")
        except:
            print("Try again")

def passcode_check():
    global CheckState
    global passcode
    global Pass
    global Granted



    Pass = open("password.txt", "r+")
    passcode = Pass.read()
    Pass.close()


    CheckState = True
    Passcode_count = 0

    while CheckState:
        try:
            Pass = str(input("Enter passcode for auth:"))
        except:
            pass

        if passcode == Pass:
            print("Correct passcode, access  granted")
            CheckState = False
            Granted = True
        else:
            print("passcode incorrect")
            Passcode_count += 1
            if Passcode_count == 3:
                CheckState = False
                print("Too many tries")
            else:
                pass

def Pass_reset():
    New_password = str(input("Enter new password: "))
    Reset = open("password.txt", "w+")
    Reset.write(New_password)
    Reset.close()

Status_read = open("Status.txt", "r+")
status = Status_read.read()
Status_read.close()

if status == "1":
    passcode_check()
else:
    passcode_set()

if CheckState == False:
    print("""Choose an option from the menu
    1: Reset password
    2: log out""")
    menu = str(input("Choose: "))
    if menu == "1":
        Pass_reset()
    else:
        print("Logging out")
        pass
