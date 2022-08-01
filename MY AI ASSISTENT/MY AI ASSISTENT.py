import pyttsx3 as p
import datetime as d
import speech_recognition as s
import os
import subprocess
import webbrowser as w
import wikipedia


# todo speed up down
a=p.init()
r=a.getProperty("rate")
a.setProperty("rate",180)

# todo function for voice
def voice(v):
    a = p.init()
    b = a.getProperty("voices")
    a.setProperty("voice", b[1].id)
    a.say(v)
    a.runAndWait()

# todo function for wish
def wish():
    h=int(d.datetime.now().hour)
    if h>=0 and h<12:
        voice("Good Morning Prince Singh,i am your Assistant,how can i help you")
    elif h>=12 and h<18:
        voice("Good after noon Prince Singh,i am your Assistant,how can i help you")
    else:
        voice("Good evining Prince Singh,i am your Assistant,how can i help you")

wish()

# todo function for speek
def speek():
    a = s.Recognizer()
    a.energy_threshold=20000
    with s.Microphone() as m:
        audio = a.listen(m)
        q = a.recognize_google(audio, language='eng-in')
        q = str(q)
        q = q.lower()
        print(q)
        return q

fun=speek()

# todo for shutdown
if "shut down" in fun:
    x="are you sure to shut down your pc"
    voice(x)
    x1 = speek()
    if "yes" in x1:
        g="thank you,for your confirmation , now i am goining to shut down your pc"
        voice(g)
    # todo shut down
        os.system('shutdown /s /t 1')
    else:
        voice("thank you,for your confirmation , now i am rejected your command")

# todo for restart
elif "restart" in fun:
    x = "are you sure to restart your pc"
    voice(x)
    x1 = speek()
    if "yes" in x1:
        g = "thank you,for your confirmation , now i am goining to restart your pc"
        voice(g)
        # todo shut down
        os.system('shutdown /r /t 1')
    else:
        voice("thank you,for your confirmation , now i am rejected your command")


# todo file open
elif "open file" in fun:
    g = "thank you,for your confirmation , now i am goining to open your File mannager"
    voice(g)
    subprocess.Popen("explorer")

elif "open installation area" in fun:
    g = "thank you,for your confirmation , now i am goining to open your installation area "
    voice(g)
    os.startfile("E:\\")

elif "open coding world" in fun:
    g = "thank you,for your confirmation , now i am goining to open your coding world"
    voice(g)
    os.startfile("F:\\")

elif "open college world" in fun:
    g = "thank you,for your confirmation , now i am goining to open your college world"
    voice(g)
    os.startfile("G:\\")

# todo webbrowser or internet
elif "open youtube" in fun:
    g = "thank you,let's enjoy , now i am goining to open youtube"
    voice(g)
    w.open("http://youtube.com")

elif "open google" in fun:
    g = "thank you,let's go and explore , now i am goining to Google"
    voice(g)
    w.open("http://google.com")

elif "open gmail" in fun:
    g = "thank you,for your confirmation , now i am goining to open Gmail"
    voice(g)
    w.open("http://gmail.com")

# todo searching or playing

elif 'play and search' in fun:
    voice("where you want to search, Google or Youtube")
    f = speek()
    if f == 'google':
        voice("what you want to search, on googel")
        a = speek()
        voice("ok, i am searching on google" + a)
        w.open("http://google.com/search?q=" + a)
    elif f == 'youtube':
        voice("ok, what you want searching or playining on youtube")
        b = speek()
        if b == "searching":
            voice("ok, what you want to searching")
            a = speek()
            w.open("http://youtube.com/results?search_query=" + a)
        elif b == "playing":
            voice("ok, what you want to playing")
            a = speek()
            p.playonyt(a)

# todo command for system application

elif 'open vs code' in fun:
    g = "thank you,for your confirmation , now i am goining to open your vs code"
    voice(g)
    path = "C:/Users/hp/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    os.startfile(path)

elif 'open pycharm' in fun:
    g = "thank you,for your confirmation , now i am goining to open your pycharm IDE"
    voice(g)
    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
    os.startfile(path)

elif 'open firefox' in fun:
    g = "thank you,for your confirmation , now i am goining to open firefox"
    voice(g)
    path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    os.startfile(path)

elif 'open chrome' in fun:
    g = "thank you,for your confirmation , now i am goining to open chrome"
    voice(g)
    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(path)

elif 'open paint' in fun:
    g = "thank you,for your confirmation , now i am goining to open paint"
    voice(g)
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk"
    os.startfile(path)

elif 'open notepad' in fun:
    g = "thank you,for your confirmation , now i am goining to open notepad"
    voice(g)
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
    os.startfile(path)

elif 'open python' in fun:
    g = "thank you,for your confirmation , now i am goining to open your python IDE"
    voice(g)
    path = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnk"
    os.startfile(path)

elif 'open any disc' in fun:
    g = "thank you,for your confirmation , now i am goining to open anydisk"
    voice(g)
    path = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
    os.startfile(path)

elif 'open java' in fun:
    g = "thank you,for your confirmation , now i am goining to open IntelliJ Java"
    voice(g)
    path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3\\bin\\idea64.exe"
    os.startfile(path)

# todo command promt
elif 'command line' in fun:
    g = "thank you,for your confirmation , now i am goining to open command line"
    voice(g)
    path = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
    os.startfile(path)

# todo send whatsaap msg
elif 'whatsapp' in fun:
    g = "are you sure to open WhatsApp"
    voice(g)
    a=speek()
    if a=="yes":
        voice("please enter your security password")
        password = input("Password = ")
        if password == str(5550):
            g = "thank you,for your confirmation , now i am goining to open your WhatsApp"
            voice(g)
            w.open("https://web.whatsapp.com/")
        else:
            voice("Sorry Your Password is wrong please try after some time,Thankyou")
    else:
        voice("thank you,for your confirmation , now i am rejected your command")

# todo search in wikipedia
elif 'wikipedia' in fun:
    voice("Searching Wikipidea......")
    cmd = speek()
    quary = fun.replace("wikipedia", "")
    result = wikipedia.summary(cmd, sentences=2)
    voice("According to wekipidea")
    print(result)
    voice(result)

else:
    g = "sorry,I'm not able to reconize your command"
    voice(g)

