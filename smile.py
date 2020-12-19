# 18-Dec-2020
# Hacka-demic
# Team86- Tillandsia 
# Smile.py 
# Our goal is to motivate and make people smile during this pandemic

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder # connects python file with kivy file
import json, glob
from datetime import datetime

# load user interface design
Builder.load_file('uidesign.kv')

class LoginScreen(Screen):
    def sign_up(self):
        # self is object of the LoginScreen class. manager is property of Screen and Current is the attribute of manager
        self.manager.current = "sign_up_screen"  

    def login(self, uname, pwd):
        with open("userdata.json") as file:
            userdata = json.load(file)
        if uname in userdata and userdata[uname]['password'] == pwd:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password"

class SignUpScreen(Screen):
    def add_user(self, uname, pwd):
        with open("userdata.json") as file:
            userdata = json.load(file)
        
        userdata[uname]= {'username': uname, 'password': pwd,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("userdata.json", 'w') as file:
            json.dump(userdata, file)
        self.manager.current = "sign_up_screen_success"  


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen" 


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass


class SmileApp(App):
    def build(self):
        self.title = "Smile"
        return RootWidget()

if __name__ == "__main__":
    SmileApp().run()