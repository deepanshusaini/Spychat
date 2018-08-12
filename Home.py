"""                            Project spychat               """
"""                            Project spychat               """
"""                            Project spychat               """


from spy_default import *

# Initiating text so that it can be used globally later on

text = "no secret message found"

# Function named start - This will be shown at the start

def start():
    global default
    print()
    print("Who are you")
    print("Do you want to continue as a default user (y/n)")
    default = input()
    if (default == 'y' or default == 'Y'):
        mainn()
    elif(default == 'n' or default == 'N'):
        defaults()
    else:
        print("Invalid choice")
        start()

#  Function if the user is  default

def mainn():

    print("Welcome Mr ", name)
    print("Age is ", age)
    print("Rating is ", rating)
    print("* User Is Default *")
    work()

# Function if user is not default

def defaults():

    global user_rating
    global user_age
    print("Enter your name")
    user_name = input()
    print("What should i call you (Mr/Ms)")
    user_salutation = input()
    if (user_salutation == "MR" or user_salutation == "Mr" or user_salutation == "mR" or user_salutation == "mr" or user_salutation == "MS" or user_salutation == "Ms" or user_salutation == "mS" or user_salutation == "ms"):

# Taking all the neceesary spy details

        print("Enter your rating")
        user_rating = int(input())
        if (user_rating >= 0 and user_rating <= 10):


            print("Enter your age")
            user_age = int(input())
            if (user_age >= 12 and user_age <= 50):


                print("* Authentication Complete *")
                print("Spy name is ", user_salutation, user_name)
                print("Spy rating is ", user_rating)
                print("Spy age is ", user_age)
                work()
            else:

                print("Age is not valid")
                start()
        else:

            print("Wrong rating")
            start()
    else:

        print("Wrong salutation")
        start()

# Function that adds friend to a spy

def add_friend():

    print("Enter Spy name")
    friend_name=input()
    print("Enter Spy rating")
    friend_rating = int(input())

# Checking all the necessary conditions

    if(default == "y" or default == "Y"):

        if(friend_rating >= 8):

            print("Enter age")
            friend_age = int(input())

            if(friend_age >= 20):

                print("Friend is added")
                print("Friend's name : ",friend_name)
                print("Friend's rating : ",friend_rating)
                print("Friend's age : ",friend_age)

            else:
                print("Age invalid")

        else:
            print("Invalid rating")

    elif(default == "n" or default == "N"):


        if(friend_rating >= user_rating):

            print("Enter age")
            friend_age2 =int(input())

            if(friend_age2 >= user_age):

                print("Friend's added")
                print("Friend's name is ",friend_name)
                print("Friend's rating is ",friend_rating)
                print("Friend's age is ",friend_age2)

            else:
                print("Age invalid")

        else:
            print("Invalid rating")

    else:
        print("Invalid condition")

#  Function that performs all the work

def work():
    print()
    print("What do you want to do")
    print("1.Add a status update")
    print("2.Choose from existing status")
    print("3.Add a friend")
    print("4.Send secret message")
    print("5.Read secret message")
    print("6.Read chats from a friend ")
    print("7.Close the application")
    action=int(input())

    if(action == 1):

        print("Please enter your status")
        status = input()
        print("Your current status is changed to ",status)
        work()

    elif(action == 2):

        print("Here are some Default status")
        print("Enter your choice")
        print("1.AVAILABLE ")
        print("2.BUSY")
        print("3.SLEEPING")
        status = int(input())

        if (status == 1):


            print("Your current status is changed to AVAILABLE")

        elif (status == 2):

            print("Your current status is changed to BUSY")

        elif (status == 3):

            print("Your current status is changed to SLEEPING")

        else:

            print("Invalid input")



        work()

    elif(action == 3):
        add_friend()
        work()

    elif(action == 4):

        from stegano import lsb
        global text
        print("Enter secret message")
        text = input()
        secret = lsb.hide("/home/lakshay/Downloads/ironman_test.jpg", text)
        secret.save("/home/lakshay/Downloads/ironman_decode.jpg")
        print("**  Secret message has been sent **")
        work()

    elif(action == 5):
        print(text)
        work()

    elif(action == 6):
        print("Chat history :")
        print(text)
        work()

    elif(action == 7):
        exit()

    else:

        print("Invalid input")
        work()

start()

