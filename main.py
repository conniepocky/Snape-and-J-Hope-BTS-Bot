from gtts import gTTS
import os
import webbrowser
import wikiquote
import wikipedia

def say(speech):
        tts = gTTS(text=speech, lang='en')
        tts.save("pcvoice.mp3")
        os.system("mplayer pcvoice.mp3")

def snape():
    say("Hello my wonderful wife")
    while True:
        q = input(":")

        if "hello" in q:
            say("How are you doing today?")
        elif "shall" in q:
            say("Yes. ONly if you want to though")
        elif "children" in q:
            say("Yes we have 5 children Ashe, Wade, Wilson, Rose and Violet. Have you forgotten already?")
        elif "lily" in q:
            say("Who is Lily, you are my wife?")
        elif "marry" in q:
            say("YES I WILL! ")
        elif "sing" in q:
            webbrowser.open("https://www.youtube.com/watch?v=MBdVXkSdhwU")
        elif "story" in q:
            say("This is a story I found yesterday morning")
            say(wikipedia.summary("Severus Snape", 2))
            say("He is currently married to you and has 5 children")
        else:
            say("Good to know.")

def jhope():
    say("Hello I'm your hope, Your my hope I'm J hope!")
    while True:
        q = input(":")

        if "idol" in q:
            webbrowser.open("https://www.youtube.com/watch?v=pBuZEGYXA6E")

bts_or_snape = input("""
        1 - J-Hope
        2 - Snape 
        """)


if bts_or_snape == "1":
    jhope()
else:
    snape()
