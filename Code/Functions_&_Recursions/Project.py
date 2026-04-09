# Rule Based AI Python ChatBot
import datetime
import time

name = input("Swagat h, enter your name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning, ", name)
elif 11 <= presentHour <= 15:
    print("Good Afternoon, ", name)
elif 15 <= presentHour <= 20:
    print("Good Evening, ", name)
else:
    print("Good night, ", name)
    
print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'byt' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses]
resposnes = {
    "hello": "Hi, welcome. How can I help you",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better",
    "happy": "Great to hert that",
    "functions kya hota hai": "jakar chapter 7 padho"
}

# Method/Function to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for var in resposnes:
        if var in  userQuestion:
            return resposnes[var]
        
    return "I am not able to tell that yet. I am still in learning mode"
    
# Take user input
while True:
    userInput = input("please ask your question: ")
    reply=getResponseOfBot(userInput)
    print("Bot Response: ", reply)
    
    if "bye" in userInput.lower(): 
        break 