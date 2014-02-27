'''

Voting Application to ease voting process for Keystone Boys State

Written by Samuel Ricklin

v1.0

'''

import kivy
kivy.require('1.8.0')

import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainScreen(GridLayout):
    gov_names = dict()
    att_gen_names = dict()
    sup_court_names = dict()
    votes = 0
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        
        
        gov_file = open("gov_names.txt", 'r')
        att_gen_file = open("att_gen_names.txt", 'r')
        sup_court_file = open("sup_court_names.txt", 'r')
        
        v_layout = BoxLayout(padding=10, orientation="vertical")
        v_layout.add_widget(Label(text = 'Governor/Lt. Governor'))

        for line in gov_file:
            line = line.replace('\n', '')
            self.gov_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line), group='gov')
            btn.id = "gov_btn"
                
            v_layout.add_widget(btn)

        v_layout2 = BoxLayout(padding=10, orientation="vertical")
        v_layout2.add_widget(Label(text= 'Attorney General'))

        for line in att_gen_file:
            line = line.replace('\n', '')
            self.att_gen_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line), group='att_gen')
            btn.id = "att_gen_btn"
            
                
            v_layout2.add_widget(btn)

        v_layout3 = BoxLayout(padding=10, orientation="vertical")
        v_layout3.add_widget(Label(text= 'Supreme Court Justice\n       (choose 3)'))

        for line in sup_court_file:
            line = line.replace('\n', '')
            self.sup_court_names[line] = 0
            
            btn = ToggleButton(text = '%s' % (line))
            btn.id = "sup_court_btn"
                
            v_layout3.add_widget(btn)


        h_layout = BoxLayout(padding=20, orientation="horizontal")

        vote_btn = Button(text="Vote")
        vote_btn.bind(on_press=self.vote_clicked)
        h_layout.add_widget(vote_btn)
        
        clear_btn = Button(text="Clear")
        clear_btn.bind(on_press=self.clear_clicked)
        h_layout.add_widget(clear_btn)

        done_btn = Button(text='Print Votes')
        done_btn.bind(on_press=self.exit_event)
        h_layout.add_widget(done_btn)
        
        
        self.add_widget(v_layout)
        self.add_widget(v_layout2)
        self.add_widget(v_layout3)
        self.add_widget(h_layout)

        

    def vote_clicked(self, *args):
        layout = self.children
        for i in range(len(layout)):
            temp = layout[i].children
            for i in range(len(temp)):
                if temp[i].id == 'gov_btn':
                    if temp[i].state == 'down':
                        self.gov_names[temp[i].text] += 1
                if temp[i].id == 'att_gen_btn':
                    if temp[i].state == 'down':
                        self.att_gen_names[temp[i].text] += 1
                if temp[i].id == 'sup_court_btn':
                    if temp[i].state == 'down':
                        self.sup_court_names[temp[i].text] += 1

        for i in range(len(layout)):
            temp = layout[i].children
            for i in range(len(temp)):
                if temp[i].id == 'gov_btn' or temp[i].id == 'att_gen_btn' or temp[i].id == 'sup_court_btn':
                    if temp[i].state == 'down':
                        temp[i].state = 'normal'
                
                        
        print self.gov_names.items()
        print self.att_gen_names.items()
        print self.sup_court_names.items()
        
        self.votes += 1

        

    def clear_clicked(self, *args):
        layout = self.children
        for i in range(len(layout)):
            temp = layout[i].children
            for i in range(len(temp)):
                if temp[i].id == 'gov_btn' or temp[i].id == 'att_gen_btn' or temp[i].id == 'sup_court_btn':
                    if temp[i].state == 'down':
                        temp[i].state = 'normal'

    def exit_event(self, *args):
        f = open('results.txt', 'w')
        f.write('votes: ' + str(self.votes) + '\n')
        for item in self.gov_names.items():
            f.write(str(item) + '\n')
        for item in self.att_gen_names.items():
            f.write(str(item) + '\n')
        for item in self.sup_court_names.items():
            f.write(str(item) + '\n')

        sys.exit()
                
            
        
            

    
        
     

class VoteApp(App):
    
    def build(self):
        return MainScreen()



if __name__ == '__main__':
    VoteApp().run()
