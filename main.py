import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        gov_names = dict()
        att_gen_names = dict()
        sup_court_names = dict()
        
        gov_file = open("gov_names.txt", 'r')
        att_gen_file = open("att_gen_names.txt", 'r')
        sup_court_file = open("sup_court_names.txt", 'r')
        
        v_layout = BoxLayout(padding=10, orientation="vertical")
        v_layout.add_widget(Label(text = 'Governor/Lt. Governor'))

        for line in gov_file:
            gov_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line), group='gov')
            btn.id = "btn"
                
            v_layout.add_widget(btn)

        v_layout2 = BoxLayout(padding=10, orientation="vertical")
        v_layout2.add_widget(Label(text= 'Attorney General'))

        for line in att_gen_file:
            att_gen_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line), group='att_gen')
            btn.id = "btn"
            
                
            v_layout2.add_widget(btn)

        v_layout3 = BoxLayout(padding=10, orientation="vertical")
        v_layout3.add_widget(Label(text= 'Supreme Court Justice\n       (choose 3)'))

        for line in sup_court_file:
            sup_court_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line))
            btn.id = "btn"
                
            v_layout3.add_widget(btn)


        h_layout = BoxLayout(padding=20, orientation="horizontal")

        vote_btn = Button(text="Vote")
        vote_btn.bind(on_press=self.vote_clicked)
        h_layout.add_widget(vote_btn)
        
        clear_btn = Button(text="Clear")
        h_layout.add_widget(clear_btn)
        
        
        self.add_widget(v_layout)
        self.add_widget(v_layout2)
        self.add_widget(v_layout3)
        self.add_widget(h_layout)

    

    
        
     

class VoteApp(App):
    
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    VoteApp().run()
