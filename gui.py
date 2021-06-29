# -*- coding: utf-8 -*-

# Python program to create color chooser dialog box
 
import tkinter as tk

# importing tkinter module
from tkinter import *
 
# importing the choosecolor package
from tkinter import colorchooser


from tkinter import Tk, Label, Button

# importing motor control python
#from MotorControl import motor1, motor2, motor3, motor4

class ColorPicker:
    def __init__(self, master):
        self.master = master
        master.title('ColorPicker')
        
        master.geometry('500x500')
        
        self.time_var1 = IntVar()
        self.time_var2 = IntVar()
        self.time_var3 = IntVar()
        self.time_var4 = IntVar()
        
        
        self.label = Label(master, text="Please pick a color")
        self.label.pack()
        
        self.color_chosen = 0
        
        self.color_button = Button(master, text="Color", command = self.ColorSpectrum)
        self.color_button.pack()
        
        self.motor1label = Label(master, text="Motor 1")
        self.motor1entry = Entry(master, textvariable = self.time_var1)
        
        self.motor1label.pack()
        self.motor1entry.pack()
        
        self.motor2label = Label(master, text="Motor 2")
        self.motor2entry = Entry(master, textvariable = self.time_var2)
        
        self.motor2label.pack()
        self.motor2entry.pack()
        
        self.motor3label = Label(master, text="Motor 3")
        self.motor3entry = Entry(master, textvariable = self.time_var3)
        
        self.motor3label.pack()
        self.motor3entry.pack()
        
        self.motor4label = Label(master, text="Motor 4")
        self.motor4entry = Entry(master, textvariable = self.time_var4)
        self.sub_btn=tk.Button(master, text = 'Submit', command = self.GetMotorSecs)
    
        
        self.motor4label.pack()
        self.motor4entry.pack()
        self.sub_btn.pack()
        
        self.kill_button = Button(master, text="End", command = master.destroy)
        self.kill_button.pack()
        
        
    def GetMotorSecs(self):
        time1 = self.time_var1.get()
        time2 = self.time_var2.get()
        time3 = self.time_var3.get()
        time4 = self.time_var4.get()

        
        print (time1)
        print (time2)
        print (time3)
        print (time4)
        
    def ColorSpectrum(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        print (color_code)
        self.color_chosen = color_code
        
        
    def PrintColor(self):
        print (self.color_chosen)
        print (self.time_var1)
        print (self.time_var2)
        
        
    def RunMotor1(self, sec):
        return 1
        
def main ():
    
    root = Tk()
    my_gui = ColorPicker(root)
    root.mainloop()

    print (ColorPicker.PrintColor)
    
main()
