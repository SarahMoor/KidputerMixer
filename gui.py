# -*- coding: utf-8 -*-

# Python program to create color chooser dialog box
 
import tkinter as tk

# importing tkinter module
from tkinter import *
 
# importing the choosecolor package
from tkinter import colorchooser


'''
# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    return(color_code)
 
root = Tk()
button = Button(root, text = "Select color",
                   command = choose_color)
button.pack()
root.geometry("300x300")
root.mainloop()

print (button)
'''

from tkinter import Tk, Label, Button
import MotorControl

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
        
root = Tk()
my_gui = ColorPicker(root)
root.mainloop()

print (ColorPicker.PrintColor)