def passcode_set():
    passcode_save = open("password.txt", "w+")
    passcode = input()
    passcode_save.write(passcode)
    passcode_save.close()

def passcode_check():
    passcode_check = open("password.txt", "r+")
    passcode_read = passcode_check.read()
    check_status = open("status.txt", "w+")
    if input() == passcode_read:
        check_status.write("True")
    else:
        check_status.write("False")

def Pass_reset():
    New_password = input()
    Reset = open("password.txt", "w+")
    Reset.write(New_password)
    Reset.close()
