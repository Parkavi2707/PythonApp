import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyFirstApp(App):
    def build(self):
        return Button(text="Welcome to My APP!")

if __name__=='__main__':
    MyFirstApp().run()
