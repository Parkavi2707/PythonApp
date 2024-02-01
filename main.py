import kivy
print(kivy.__version__)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp,self).__init__()
        self.cols=2
        self.add_widget(Label(text='student Name'))
        self.s_name=TextInput()
        self.add_widget(self.s_name)


        self.add_widget(Label(text='student mark'))
        self.s_mark=TextInput()
        self.add_widget(self.s_mark)
        
        self.add_widget(Label(text='student age'))
        self.s_age=TextInput()
        self.add_widget(self.s_age)

        
        self.add_widget(Label(text='student gender'))
        self.s_gender=TextInput()
        self.add_widget(self.s_gender)

        
        self.add_widget(Label(text='student blood'))
        self.s_blood=TextInput()
        self.add_widget(self.s_blood)
        
        self.press=Button(text='Click me')
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
    def click_me(self,instance):
        print("Name of student is "+self.s_name.text)
        print("Mark of student is "+self.s_mark.text)
        print("Age of student is "+self.s_age.text)
        print("Gender of student is "+self.s_gender.text)
        print("Blood Group of student is "+self.s_blood.text)

        print("")
class studentApp(App):
    def build(self):
        return childApp()
if __name__=='__main__':
    studentApp().run()
