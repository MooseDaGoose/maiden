import InstaBot
import getpass
import time

#welcome statement
print("\033[1mWelcome to InstaBot, today we will see what scumbags aren't following you back on instagram XD\033[0m")
time.sleep(3)

#discrete user input (hides input) !disclaimer! - getpass only hides user input when run on terminal
username = getpass.getpass("Please enter your username: ")
password = getpass.getpass("please enter your password: ")

#normal user input
#username = input("Please enter your username: ")
#password = input("please enter your password: ")

#main
myBot = InstaBot.InstaBot(username, password)
myBot.get_unfollowers()