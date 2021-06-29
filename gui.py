# -*- coding: utf-8 -*-

# Python program to create color chooser dialog box
 
import tkinter as tk

# importing tkinter module
from tkinter import *
 
# importing the choosecolor package
from tkinter import colorchooser


from tkinter import Tk, Label, Button

# importing motor control python
from MotorControl import motor1, motor2, motor3, motor4

class ColorPicker:
    def __init__(self, master):
        self.master = master
        master.title('ColorPicker')
        
        master.geometry('300x300')
        
        self.label = Label(master, text="Please pick a color")
        self.label.pack()
        
        self.color_chosen = 0
        
        self.color_button = Button(master, text="Color", command = self.ColorSpectrum)
        self.color_button.pack()
        
        self.kill_button = Button(master, text="kill me", command = master.destroy)
        self.kill_button.pack()
        
        
    def ColorSpectrum(self):
     
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        print (color_code)
        self.color_chosen = color_code
        
        
    def PrintColor(self):
        print (self.color_chosen)
        
        
        
    def RunMotor1(self, sec):
        return 1
        
def main ():
    
    root = Tk()
    my_gui = ColorPicker(root)
    root.mainloop()

    print (ColorPicker.PrintColor)
    
main()
