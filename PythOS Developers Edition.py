print("-------------------------------------------------------------------------PythOS Promt(For Developers)--------------------------------------------------------------------")
print("Welcome to PythOS")
from time import sleep
import random
print("Starting. Please wait...")
sleep(5)
dev_ver = "Indev 2.1.0"
# Below is the setup.
dev_name = "INVALID"
key = "INVALID"
repeat = True
licence =  False
def login():
    print("===========================================================================Log in required================================================================================")
    dev_name = input("Type in your name: ")
    key = input("Type in a valid Product Key in Caps. This has been included with your installation box: ")
    if key == "X56W7-HJS89-S83KD-5KF91":
        repeat = True
        print("WARNING! Never shut this window unless you choose 'Shutdown' in the power options.")
        print()
    else:
        print("Invalid key.")
        login()
    print("=========================================================================================================================================================================")
login()
while repeat == True:
    print()
    print("Please type in your command. You can type:")
    print("ver - tells you about your verion of PythOS Basic.")
    print("power - opens power options, such as Sleep or Shutdown.")
    print("games - opens Games.")
    command_option = input("Type in your command: ")
    if command_option == "ver":
        print("You are runnning:")
        print("PythOS", dev_ver)
        print("Developer's Edition")
        print()
        print("This installation of PythOS Developer's Edition is licenced to: ")
        print("") # Inside, type in the name of your company.
    elif command_option == "power":
        print("POWER OPTIONS")
        print("Here are your power/account options:")
        print("shutdown - Logs out and turns off your installation.")
        print("sleep - Pauses all prosesses and puts it into a low-power mode.")
        print("logout - Ends your session.")
        power_option = input("Please type in your option: ")
        if power_option == "shutdown":
            print("Logging out...")
            sleep(5)
            print("Logged out.")
            print("Exiting PythOS...")
            repeat = False
            sleep(10)
            shutdown_error = random.randint(0,9999)
            if shutdown_error == 0:
                home = input(">>> Python: PythOS could  not shut down. PythOS can be killed and safely closed by pressing ENTER. ")
                if home == "":
                    print(">>> Python: Killed PythOS.")
                else:
                    print(">>> Python: Killed PythOS.")
        elif power_option == "sleep":
            wake_up = input("PythOS is sleep. Press ENTER to wake up. ")
            if wake_up == "":
                print("Returning to PythOS...")
                sleep(2)
            else:
                print("Returning to PythOS...")
                sleep(2)
        elif power_option == "logout":
            print("Logging out...")
            sleep(1)
            print("Logged out.")
            sleep(5)
            login()
