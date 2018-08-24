#The Magic 8 Ball
import time
from random import randint
 
replies =["Yes","No","Possibly", "Ask again later", "IDK"]
 
def question():
        print ("What is your question?")
        question = input()
        print ("Thinking...")
        time.sleep(3)
        print (replies [randint(0,4)])
        end()
 
def end():
        print ("Thanks for playing! Do you want to try again?")
        user_reply = input()
        if user_reply == "yes":
                question()
 
 
print ("Welcome to the magic 8-ball")
question()