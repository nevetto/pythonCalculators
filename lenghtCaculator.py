from tkinter import *
from math import *
import tkinter.ttk as ttk
from tkinter.messagebox import *

class LenghtCal():
    def __init__(self):
        self.container = Tk()
        self.container.title('Lenght')
        self.container.configure(bg='silver')
        self.lbl = Label(self.container, text= "Lenght", font=('arial',10), bg='silver')
        self.lbl.pack(side =TOP, expand = YES, fill = BOTH)
        self.screenBm = Frame(self.container)
        self.screenBm.pack()
        self.answerN = IntVar()
        
        self.screenN =Entry(self.screenBm, textvariable=self.answerN,font=('arial',20), state='normal', background = 'silver')
        self.screenN.pack()

        self.scrnlb = Frame(self.container)
        self.scrnlb.pack()

        item = ['Nanometers', 'Microns', 'Millimeters', 'Centimeters', "Meters", 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles', 'Nautical Miles']
        self.cob = ttk.Combobox(self.scrnlb, values=(item), width="40")
        self.cob.set('Feet')
        self.cob.grid(row=0, column=0, padx=20, pady=20)

        self.screenFm = Frame(self.container)
        self.screenFm.pack()
        self.answer = IntVar()
        self.screen = Entry(self.screenFm, textvariable=self.answer, font=('arial',20), state='disabled', background = 'silver')
        self.screen.pack()

        self.scrnlb2 = Frame(self.container)
        self.scrnlb2.pack()

        item2 = ['Nanometers', 'Microns', 'Millimeters', 'Centimeters', "Meters", 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles', 'Nautical Miles']
        self.cob2 = ttk.Combobox(self.scrnlb2, values=(item2), width="40")
        self.cob2.set('Feet')
        self.cob2.grid(row=0, column=0, padx=20, pady=20)

        self.scrnlb3 = Frame(self.container)
        self.scrnlb3.pack()

        self.lb = Label(self.scrnlb3, text="About equal to")

        self.ft = Label(self.scrnlb3, textvariable=self.answer, width=14,font=('arial',8), state='disabled', background = 'silver')
        self.ft.pack(side='left')

        self.inch = Label(self.scrnlb3, textvariable=self.answer, width=14,font=('arial',8), state='disabled', background = 'silver')
        self.inch.pack(side='left')

        self.yard = Label(self.scrnlb3, textvariable=self.answer, width=14,font=('arial',8), state='disabled', background = 'silver')
        self.yard.pack(side='left')

        self.miles = Label(self.scrnlb3, textvariable=self.answer, width=14,font=('arial',8), state='disabled', background = 'silver')
        self.miles.pack(side='left')

        self.buttonFm = Frame(self.container)
        self.buttonFm.pack()

        Button(self.buttonFm, text='CE', width=5, command=self.clear).grid(row=3, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='del', width=5, command=self.dele).grid(row=5, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='1', width=5, command=lambda: self.getValues('1')).grid(row=0, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='2', width=5, command=lambda: self.getValues('2')).grid(row=0, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='3', width=5, command=lambda: self.getValues('3')).grid(row=0, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='4', width=5, command=lambda: self.getValues('4')).grid(row=1, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='5', width=5, command=lambda: self.getValues('5')).grid(row=1, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='6', width=5, command=lambda: self.getValues('6')).grid(row=1, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='7', width=5, command=lambda: self.getValues('7')).grid(row=2, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='8', width=5, command=lambda: self.getValues('8')).grid(row=2, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='9', width=5, command=lambda: self.getValues('9')).grid(row=2, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='0', width=5, command=lambda: self.getValues('0')).grid(row=3, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='.', width=5, command=lambda: self.getValues('.')).grid(row=3, column=1, padx=5, pady=5)

        
        self.answer.set(0)
        self.answerN.set(0)
        self.result =  0
        self.container. mainloop()


    def getValues(self, value):
        self.state = self.cob.get()
        self.state2 = self.cob2.get()
        if self.screen.get()!="":
            if self.screen.get() == "0" or self.result =='1':
                self.answer.set(value)
                self.answerN.set(self.screenN.get() + value)
                self.vavl = int(self.screenN.get())
                # for feet
            if self.state == "Feet" and self.state2 == "Feet":
                self.answer.set( self.vavl) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 30.48)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Feet" and self.state2 =="Nanometers":
                self.answer.set( self.vavl * 304800000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Microns":
                self.answer.set( self.vavl * 304800)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 304.8)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.3048)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000305)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Inches":
                self.answer.set( self.vavl * 12)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.333333)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000189)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Feet" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.000165)
                self.answerN.set( self.vavl)
                self.result =1

            #for nanometers
             
            elif self.state == "Nanometers" and self.state2 == "Feet":
                self.answer.set( self.vavl * 0.00000000328084) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 0.0000001)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Nanometers" and self.state2 =="Nanometers":
                self.answer.set( self.vavl)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Microns":
                self.answer.set( self.vavl * 0.001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 0.000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.00000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000000000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Inches":
                self.answer.set( self.vavl * 0.000000039370079)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.000000001093613)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000000000000621)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nanometers" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.00000000000054)
                self.answerN.set( self.vavl)
                self.result =1
                 

            

    #for Centimeters
             
            elif self.state == "Centimeters" and self.state2 == "Feet":
                self.answer.set( self.vavl * 0.032808) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Centimeters" and self.state2 =="Nanometers":
                self.answer.set( self.vavl * 10000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Microns":
                self.answer.set( self.vavl * 10000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 10)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.01)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.00001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Inches":
                self.answer.set( self.vavl * 0.393701)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.010936)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000006)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Centimeters" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.000005)
                self.answerN.set( self.vavl)
                self.result =1
                 

            #for meters
             
            elif self.state == "Meters" and self.state2 == "Feet":
                self.answer.set( self.vavl * 3.28084) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 100)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Meters" and self.state2 =="Nanometers":
                self.answer.set( self.vavl*1000000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 1000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Meters":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Inches":
                self.answer.set( self.vavl * 39.370079)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Yards":
                self.answer.set( self.vavl * 1.093613)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000621)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Meters" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.00054)
                self.answerN.set( self.vavl)
                self.result =1
                 
        # for kilometers
            elif self.state == "Kilometers" and self.state2 == "Feet":
                self.answer.set( self.vavl * 3280.84) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 100000)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Kilometers" and self.state2 =="Nanometers":
                self.answer.set( self.vavl*1000000000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1000000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 1000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Meters":
                self.answer.set( self.vavl * 1000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Inches":
                self.answer.set( self.vavl * 39370.08)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Yards":
                self.answer.set( self.vavl * 1093.613)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.621371)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Kilometers" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.539957)
                self.answerN.set( self.vavl)
                self.result =1
                 

            #for Inches
             
            elif self.state == "Inches" and self.state2 == "Feet":
                self.answer.set( self.vavl * 0.83333) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 2.54)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Inches" and self.state2 =="Nanometers":
                self.answer.set( self.vavl * 25400000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Microns":
                self.answer.set( self.vavl * 25400)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 25.4)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.0254)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000025)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Inches":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.027778)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Inches" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000016)
                self.answerN.set( self.vavl)
                self.result =1

            #for miles
             
            elif self.state == "Miles" and self.state2 == "Feet":
                self.answer.set( self.vavl * 5280) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 160934.4)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Miles" and self.state2 =="Nanometers":
                self.answer.set( self.vavl*1609344000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1609344000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 1609344)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Meters":
                self.answer.set( self.vavl * 1609.344)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 1.609344)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Inches":
                self.answer.set( self.vavl * 63360)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Yards":
                self.answer.set( self.vavl * 1760)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Miles":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Miles" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.868976)
                self.answerN.set( self.vavl)
                self.result =1
                 
        # for yards
            elif self.state == "Yards" and self.state2 == "Feet":
                self.answer.set( self.vavl * 3) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 91.44)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Yards" and self.state2 =="Nanometers":
                self.answer.set( self.vavl*914400000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Microns":
                self.answer.set( self.vavl * 9144000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 914.4)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.9144)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000914)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Inches":
                self.answer.set( self.vavl * 36)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Yards":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000568)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Yards" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl *0.000494)
                self.answerN.set( self.vavl)
                self.result =1

            # for millimeters
            elif self.state == "Millimeters" and self.state2 == "Feet":
                self.answer.set( self.vavl * 0.003281) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 0.1)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Millimeters" and self.state2 =="Nanometers":
                self.answer.set( self.vavl* 1000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.011)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Inches":
                self.answer.set( self.vavl * 0.03937)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.001094)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000000621371192)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Millimeters" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.000000539956803)
                self.answerN.set( self.vavl)
                self.result =1


            # for microns
            elif self.state == "Microns" and self.state2 == "Feet":
                self.answer.set( self.vavl * 0.000003) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 0.0001)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Microns" and self.state2 =="Nanometers":
                self.answer.set( self.vavl* 1000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 0.001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Meters":
                self.answer.set( self.vavl * 0.000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 0.000000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Inches":
                self.answer.set( self.vavl * 0.000039)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Yards":
                self.answer.set( self.vavl * 0.000001)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Miles":
                self.answer.set( self.vavl * 0.000000000621371)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Microns" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 0.000000000539957)
                self.answerN.set( self.vavl)
                self.result =1

            
            # for Nautical miles
            elif self.state == "Nautical Miles" and self.state2 == "Feet":
                self.answer.set( self.vavl * 6076.115) 
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Centimeters":
                self.answer.set( self.vavl * 185200)
                self.answerN.set( self.vavl)
                self.result =1
                print(self.state2)
            elif self.state == "Nautical Miles" and self.state2 =="Nanometers":
                self.answer.set( self.vavl* 1852000000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Microns":
                self.answer.set( self.vavl * 1852000000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Millimeters":
                self.answer.set( self.vavl * 1852000)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Meters":
                self.answer.set( self.vavl * 1852)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Kilometers":
                self.answer.set( self.vavl * 1852)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Inches":
                self.answer.set( self.vavl * 72913.39)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Yards":
                self.answer.set( self.vavl * 2025.372)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Miles":
                self.answer.set( self.vavl *1.150779)
                self.answerN.set( self.vavl)
                self.result =1
            elif self.state == "Nautical Miles" and self.state2 =="Nautical Miles":
                self.answer.set( self.vavl * 1)
                self.answerN.set( self.vavl)
                self.result =1
            else:
                self.answer.set(self.screen.get() + value)
                # self.answerN.set(self.screenN.get() + value)
                self.result = 0

             



    def clear(self):
        if self.screen.get() != " ":
            self.answerN.set(0)
            self.answer.set(0)

    


    def dele(self):
        if self.screen.get() != " ":
            self.answerN.set('')

   

    # def getValues(self, value):        
    #     self.state = self.cob.get()
        # # if self.screen.get() == "0":
        # self.answer.set(value)
        # self.answerN.set(self.screenN.get() + value)
        # if self.state == 'Feet' and self.answer.set(value) == '1':
        #     # self.answer.set(value) 
        #     self.answer.set(1 * 5)


        # if self.screen.set()!="":
        # if self.state == 'Feet':
        #     self.answer.set(value)
        #     self.ft.configure(text=value * 8)
            # self.answer.set(self.screen.set() + value)
            # self.answer.set(self.ft)
            # else:
            #     self.answer.set(self.screen.get() + value)
            #     self.answerN.set(self.screenN.get() + value)
            #     self.result = 0      

        # else:
        #     self.answer.set(self.screen.get() + value)
        #     self.answerN.set(self.screenN.get() + value)
        #     self.result = 0

    
        

lt = LenghtCal()


# from tkinter import *
# import tkinter.ttk as ttk
# from tkinter.messagebox import *

# class FormExample():
#     def __init__(self):
#         self.root = Tk()
#         self.root.geometry("800x500")
#         self.root.iconbitmap("ball.ico")
#         self.root.title('Lenght')
#         self.mainFrame = Frame(self.root)
#         self.mainFrame.pack(side =TOP, expand = YES, fill = BOTH)
#         self.mainFrame.grid_propagate(0)
#         self.status = StringVar()
#         Label(self.mainFrame, text= "Lenght", font=('arial',10), bg='blue').grid(row= 0, column = 1, pady = 5)
#         self.screenBm = Frame(self.root)
#         self.screenBm.pack()
#         self.screenBm.configure(bg='red')
#         self.answerN = IntVar()
#         self.screenN =Entry(self.screenBm, textvariable=self.answerN, width=14,font=('arial',20), state='normal', background = 'blue', fg='yellow')
#         self.screenN.pack()

#         self.item = ['Nanometers', 'Microns', 'melimeters', 'Centimeters', "Meters", 'Kilometers', 'Inches', 'Feet', 'Yard', 'Nautical Miles']
#         self.cob = ttk.Combobox(self.screenBm, values=(self.item))
#         self.cob.set('Feet')
#         self.cob.grid(row=1, column=0)
        # self.item.bind("<<ListboxSelect>>", self.register())

        
        # Label(self.mainFrame, text="Password", font=('arial', 20)).grid(row=2, column =4)
        # self.Password = Entry(self.mainFrame, show="*", width=10, bd=5, insertwidth=4, justify='left', font=('arial', 20, 'bold'))
        # self.Password.grid(row=2, column=5, pady=7)
        # Radiobutton(self.mainFrame, variable= self.status, text = 'Student', value= 'student', tristatevalue= 0).grid(row=3, column=4, columnspan=4, pady=5)
        # Radiobutton(self.mainFrame, variable= self.status, text = 'Staff', value= 'staff', tristatevalue= 0).grid(row=3, column=5, pady=5)
        # Label(self.mainFrame, text="Choose your courses", font=('arial',20)).grid(row=4, column=4)
        # self.python = BooleanVar()
        # self.csharp = BooleanVar()
        # self.web = BooleanVar()
        # self.java = BooleanVar()
 
        # Checkbutton(self.mainFrame, text="python", variable=self.python).grid(row=4, column=5)
        # Checkbutton(self.mainFrame, text="C#", variable=self.csharp).grid(row=4, column=6)
        # Checkbutton(self.mainFrame, text="web", variable=self.web).grid(row=4, column=7)
        # Checkbutton(self.mainFrame, text="java", variable=self.java).grid(row=4, column=8)
        # itemsforlistbox=['11-20','21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
        # self.mylistbox = Listbox(self.mainFrame, font=('times',13), selectmode='browse')
        # for items in itemsforlistbox:
        #     self.mylistbox.insert(END,items)
        # self.mylistbox.grid(row=5, column=4, columnspan=3)
        # self.mylistbox.bind("<<ListboxSelect>>", self.myselection)
        # item = ['Oyo', 'Ekiti', 'Ondo', 'Benue', "Kano", 'Rivers', 'Enugu']
        # self.cob = ttk.Combobox(self.mainFrame, values=(item))
        # self.cob.set('States')
        # self.cob.grid(row=5, column=5)
        # Button(self.mainFrame, width = 10, text= 'Register', command = self.register).grid(row=6, column=5, pady=5)
        # self.label = Label(self.mainFrame, text= " ", font=('arial',20))
        # self.label.grid(row=6, column=6)
        # self.answer.set(0)
    #     self.answerN.set("")
    #     self.result =  0

    #     self.root.mainloop()

    # def register(self):
        # if self.python.get()==True:
        #     self.python = "Python"
        # if self.java.get()==True:
        #     self.java = "Java"
        # if self.web.get()==True:
        #     self.web = "Web"
        # if self.csharp.get()==True:
        #     self.csharp = "C#"
        # self.lenghtcon = self.cob.get()
        # value = self.cob.get()
        # if self.lenghtcon=="Nanometers":
        #     self.answerN.set(self.screenN.get() + value)
        # if self.java.get()==True:
        #     self.java = "Java"
        # if self.web.get()==True:
        #     self.web = "Web"
        # if self.csharp.get()==True:
        #     self.csharp = "C#"
        # self.name = self.username.get()
        # self.passwd = self.Password.get()
        # self.gender = self.status.get()
        # self.age = self.mylistbox.get(END)
        # print(self.name, self.passwd, self.gender, self.python, self.java, self.web, self.csharp, self.state, self.age)

    # def myselection(self, event):
    #     showinfo("My selection", str(self.mylistbox.get(self.mylistbox.curselection())))
# if __name__ == "__main__":

# fe = FormExample()