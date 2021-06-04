from tkinter import*
from tkinter import ttk
from math import *
from math import exp, expm1
class SimpleCal:
    def __init__(self):
        self.container = Tk()
        self.container.configure(bg='black')      

        self.menuBar = Menu(self.container, tearoff=0)
        self.science = Menu(self.menuBar)
        self.science.add_command(label="Scientific", command=self.scientific)
        self.science.add_command(label="Length", command=self.length)
        self.science.add_command(label="Standard", command=self.standard)
        self.menuBar.add_cascade(label="Menu", menu=self.science)
        self.container.config(menu=self.menuBar)

        self.lbl = Label(self.container, text= "Lenght", font=('arial',10), bg='silver')
        self.lbl.pack(side =TOP, expand = YES, fill = BOTH)

        self.mainFrame = Frame(self.container)
        self.mainFrame.pack()
        self.answer = IntVar()
        self.answerN = IntVar()
        self.length()
        self.container. mainloop()

    def length(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.container)
        self.mainFrame.pack()
        self.lbl.config(text="Length")
        self.screenBm = Frame(self.mainFrame)
        self.screenBm.pack()
        self.answerN = IntVar()
        
        self.screenN =Entry(self.screenBm, textvariable=self.answerN,font=('arial',20), state='normal', background = 'silver')
        self.screenN.pack()

        self.scrnlb = Frame(self.mainFrame)
        self.scrnlb.pack()

        item = ['Nanometers', 'Microns', 'Millimeters', 'Centimeters', "Meters", 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles', 'Nautical Miles']
        self.cob = ttk.Combobox(self.scrnlb, values=(item), width="40")
        self.cob.set('Feet')
        self.cob.grid(row=0, column=0, padx=20, pady=20)

        self.screenFm = Frame(self.mainFrame)
        self.screenFm.pack()
        self.answer = IntVar()
        self.screen = Entry(self.screenFm, textvariable=self.answer, font=('arial',20), state='disabled', background = 'silver')
        self.screen.pack()

        self.scrnlb2 = Frame(self.mainFrame)
        self.scrnlb2.pack()

        item2 = ['Nanometers', 'Microns', 'Millimeters', 'Centimeters', "Meters", 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles', 'Nautical Miles']
        self.cob2 = ttk.Combobox(self.scrnlb2, values=(item2), width="40")
        self.cob2.set('Feet')
        self.cob2.grid(row=0, column=0, padx=20, pady=20)

        self.scrnlb3 = Frame(self.mainFrame)
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

        self.buttonFm = Frame(self.mainFrame)
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



    def getValues(self, value):
        if self.screen.get() != "":
            if self.screen.get() == "0" or self.result =='1':   
                self.answerN.set(value)
            
            self.state = self.cob.get()
            self.state2 = self.cob2.get()
            self.screenValue = self.screen.get()
            
    #             # for feet
    #         if self.state == "Feet" and self.state2 == "Feet":
    #             self.answer.set( self.vavl) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 30.48)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Feet" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl * 304800000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 304800)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 304.8)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.3048)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000305)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 12)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.333333)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000189)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Feet" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.000165)
    #             self.answerN.set( self.vavl)
    #             self.result =1

    #         #for nanometers
             
    #         elif self.state == "Nanometers" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 0.00000000328084) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 0.0000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Nanometers" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 0.001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 0.000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.00000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000000000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 0.000000039370079)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.000000001093613)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000000000000621)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nanometers" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.00000000000054)
    #             self.answerN.set( self.vavl)
    #             self.result =1
            

    # #for Centimeters
             
    #         elif self.state == "Centimeters" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 0.032808) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Centimeters" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl * 10000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 10000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 10)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.01)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.00001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 0.393701)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.010936)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000006)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Centimeters" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.000005)
    #             self.answerN.set( self.vavl)
    #             self.result =1
                 

    #         #for meters
             
    #         elif self.state == "Meters" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 3.28084) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 100)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Meters" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl*1000000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 1000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 39.370079)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 1.093613)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000621)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Meters" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.00054)
    #             self.answerN.set( self.vavl)
    #             self.result =1
                 
    #     # for kilometers
    #         elif self.state == "Kilometers" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 3280.84) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 100000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Kilometers" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl*1000000000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1000000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 1000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 1000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 39370.08)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 1093.613)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.621371)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Kilometers" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.539957)
    #             self.answerN.set( self.vavl)
    #             self.result =1
                 

    #         #for Inches
             
    #         elif self.state == "Inches" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 0.83333) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 2.54)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Inches" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl * 25400000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 25400)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 25.4)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.0254)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000025)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.027778)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Inches" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000016)
    #             self.answerN.set( self.vavl)
    #             self.result =1

    #         #for miles
             
    #         elif self.state == "Miles" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 5280) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 160934.4)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Miles" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl*1609344000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1609344000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 1609344)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 1609.344)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 1.609344)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 63360)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 1760)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Miles" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.868976)
    #             self.answerN.set( self.vavl)
    #             self.result =1
                 
    #     # for yards
    #         elif self.state == "Yards" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 3) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 91.44)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Yards" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl*914400000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 9144000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 914.4)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.9144)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000914)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 36)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000568)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Yards" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl *0.000494)
    #             self.answerN.set( self.vavl)
    #             self.result =1

    #         # for millimeters
    #         elif self.state == "Millimeters" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 0.003281) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 0.1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Millimeters" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl* 1000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.011)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 0.03937)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.001094)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000000621371192)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Millimeters" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.000000539956803)
    #             self.answerN.set( self.vavl)
    #             self.result =1


    #         # for microns
    #         elif self.state == "Microns" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 0.000003) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 0.0001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Microns" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl* 1000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 0.001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 0.000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 0.000000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 0.000039)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 0.000001)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Miles":
    #             self.answer.set( self.vavl * 0.000000000621371)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Microns" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 0.000000000539957)
    #             self.answerN.set( self.vavl)
    #             self.result =1

            
    #         # for microns
    #         elif self.state == "Nautical Miles" and self.state2 == "Feet":
    #             self.answer.set( self.vavl * 6076.115) 
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Centimeters":
    #             self.answer.set( self.vavl * 185200)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #             print(self.state2)
    #         elif self.state == "Nautical Miles" and self.state2 =="Nanometers":
    #             self.answer.set( self.vavl* 1852000000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Microns":
    #             self.answer.set( self.vavl * 1852000000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Millimeters":
    #             self.answer.set( self.vavl * 1852000)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Meters":
    #             self.answer.set( self.vavl * 1852)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Kilometers":
    #             self.answer.set( self.vavl * 1852)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Inches":
    #             self.answer.set( self.vavl * 72913.39)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Yards":
    #             self.answer.set( self.vavl * 2025.372)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Miles":
    #             self.answer.set( self.vavl *1.150779)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         elif self.state == "Nautical Miles" and self.state2 =="Nautical Miles":
    #             self.answer.set( self.vavl * 1)
    #             self.answerN.set( self.vavl)
    #             self.result =1
    #         else:
    #             self.answer.set(self.screen.get() + value)
    #             # self.answerN.set(self.screenN.get() + value)
    #             self.result = 0

    # def clear(self):
    #     if self.screen.get() != " ":
    #         self.answerN.set(0)
    #         self.answer.set(0)

    # def dele(self):
    #     if self.screen.get() != " ":
    #         self.answerN.set('')

    def scientific(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.container)
        self.mainFrame.pack()
        self.lbl.config(text='Scientific')
        self.screenBm = Frame(self.mainFrame)
        self.screenBm.pack()
        self.screenBm.configure(bg='black')
        self.answerN = IntVar()
        self.screenN =Entry(self.screenBm, textvariable=self.answerN, width=14,font=('arial',20), state='normal', background = 'silver',  )
        self.screenN.pack()
        self.screenFm = Frame(self.mainFrame)
        self.screenFm.pack()
        self.screenFm.configure(bg='black')
        self.answer = StringVar()
        self.screen = Entry(self.screenFm, textvariable=self.answer, width=14,font=('arial',20), state='disabled', disabledbackground = 'silver', fg='black')
        self.screen.pack()
        self.buttonFm = Frame(self.mainFrame)
        self.buttonFm.pack()
        self.buttonFm.configure(bg='black')
        Button(self.buttonFm, text='1', width=5, command=lambda: self.getValues2('1')).grid(row=0, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='2', width=5, command=lambda: self.getValues2('2')).grid(row=0, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='3', width=5, command=lambda: self.getValues2('3')).grid(row=0, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='+', width=5, command=lambda: self.operate('+')).grid(row=0, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='4', width=5, command=lambda: self.getValues2('4')).grid(row=1, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='5', width=5, command=lambda: self.getValues2('5')).grid(row=1, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='6', width=5, command=lambda: self.getValues2('6')).grid(row=1, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='-', width=5, command=lambda: self.operate('-')).grid(row=1, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='7', width=5, command=lambda: self.getValues2('7')).grid(row=2, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='8', width=5, command=lambda: self.getValues2('8')).grid(row=2, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='9', width=5, command=lambda: self.getValues2('9')).grid(row=2, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='x', width=5, command=lambda: self.operate('*')).grid(row=2, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='0', width=5, command=lambda: self.getValues2('0')).grid(row=3, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='.', width=5, command=lambda: self.getValues2('.')).grid(row=3, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='c', width=5, command=self.clear).grid(row=3, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='/', width=5, command=lambda: self.operate('/')).grid(row=3, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='=', width=15, command=self.calculate).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.but = Button(self.buttonFm, text='OFF', width=5, command=self.ofon)
        self.but.grid(row=4, column=3, columnspan=2, padx= 5, pady=5)
        Button(self.buttonFm, text='del', width=5, command=self.dele).grid(row=5, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='sqrt', width=5, command=self.sqroot).grid(row=5, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='^', width=5, command=self.pow).grid(row=5, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='sqr', width=5, command=self.sqr).grid(row=5, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='abs', width=5, command=self.abss).grid(row=6, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='log', width=5, command=self.loga).grid(row=6, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='%', width=5, command=lambda: self.operate('%')).grid(row=6, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='!', width=5, command=self.pii).grid(row=6, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='exp', width=5, command=self.expo).grid(row=7, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='cos', width=5, command=self.coso).grid(row=7, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='sin', width=5, command=self.sino).grid(row=7, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='tan', width=5, command=self.tano).grid(row=7, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='rad', width=5, command=self.rada).grid(row=8, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='deg', width=5, command=self.degr).grid(row=8, column=1, padx=5, pady=5)

    def getValues2(self, value):
        if self.screen.get()!="":
            if self.screen.get() == "0" or self.result =='1':
                self.answer.set(value)
                self.answerN.set(self.screenN.get() + value)
            else:
                self.answer.set(self.screen.get() + value)
                self.answerN.set(self.screenN.get() + value)
                self.result = 0

    def operate(self, op):
        if self.screen.get() !="":
            self.operator = op
            self.fval = float(self.screen.get())
            self.answer.set(0)
            # self.answerN.set(0)
            self.answerN.set(self.screenN.get() + op)
           
         


    def clear(self):
        if self.screen.get() != " ":
            self.answerN.set(0)
            self.answer.set(0)

    


    def dele(self):
        if self.screen.get() != " ":
            self.answerN.set('')

   


    def calculate(self):
        
        if self.screen.get()!= " ":
            # self.answer.set(eval(self.screen.get())
            self.sval = float(self.screen.get())
            
            if self.operator == "+":
                self.answer.set(self.fval + self.sval)
                self.result =1
            elif self.operator == "-":
                self.answer.set(self.fval - self.sval)
                self.result = 1
            elif self.operator == "*":
                self.answer.set(self.fval * self.sval)
                self.result = 1
            elif self.operator == "/":
                self.answer.set(self.fval / self.sval)
                self.result = 1
            elif self.operator == "%":
                self.answer.set(self.fval % self.sval)
                self.result = 1

   
    def sqroot(self):
        if self.screen.get()!= " ": 
            self.s = self.screen.get()
            self.answer.set(sqrt(eval(self.s)))
            self.answerN.set('sqrt('+ str(self.ab) +')')
           
    def pow(self):
        if self.screen.get()!=' ':
            self.p = float(self.screen.get())
            self.answer.set(pow(self.p,self.p))
            self.answerN.set('pow('+ str(self.ab) +')')

    def sqr(self):
        if self.screen.get()!=' ':
            self.sq = float(self.screen.get())
            self.answer.set(pow(self.sq,2))
            self.answerN.set('sqr('+ str(self.ab) +')')

    def abss(self):
        self.ab = float(self.screen.get())
        self.answer.set(abs(self.ab))
        self.answerN.set('abs('+ str(self.ab) +')')

    def loga(self):
        self.ab = float(self.screen.get())
        self.answer.set(log10(self.ab))
        self.answerN.set('log('+ str(self.ab) +')')


    def pii(self):
        self.ab = float(self.screen.get(pi/180))
        self.answer.set((self.ab))
        self.answerN.set(pi(self.ab))

    def expo(self):
        self.ab = float(self.screen.get())
        self.answer.set(exp(self.ab))
        self.answerN.set(str(self.ab) +'=')

    def coso(self):
        self.ab = float(self.screen.get())
        self.answer.set(cos(self.ab))
        self.answerN.set('cos('+ str(self.ab) +')')


    def sino(self):
        self.ab = float(self.screen.get())
        self.answer.set(sin(self.ab))
        self.answerN.set('sin('+ str(self.ab) +')')

    def tano(self):
        self.ab = float(self.screen.get())
        self.answer.set(tano(self.ab))
        self.answerN.set('tan('+ str(self.ab) +')')

    def rada(self):
        self.ab = float(self.screen.get())
        self.answer.set(radians(self.ab))
        self.answerN.set('rad('+ str(self.ab) +')')

    def degr(self):
        self.ab = float(self.screen.get())
        self.answer.set(degrees(self.ab))
        self.answerN.set('deg('+ str(self.ab) +')')  
         

    def ofon(self):
        if self.state == "on":
            self.answer.set(0)
            self.answerN.set(0)
            self.state = "off"
            self.but.configure(text="OFF")
        else:
            self.answer.set(" ")
            self.answerN.set(" ")
            self.state = "on"
            self.but.configure(text="ON")

    

    def standard(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.container)
        self.mainFrame.pack()
        self.screenFm = Frame(self.mainFrame)
        self.screenFm.pack()
        self.lbl.config(text='Standard')
        self.answer = StringVar()
        self.screen = Entry(self.screenFm, textvariable=self.answer, width=14,font=('arial',20), state='disabled', disabledbackground = 'white')
        self.screen.pack()
        self.buttonFm = Frame(self.mainFrame)
        self.buttonFm.pack()
        Button(self.buttonFm, text='1', width=5, command=lambda: self.getValues('1')).grid(row=0, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='2', width=5, command=lambda: self.getValues('2')).grid(row=0, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='3', width=5, command=lambda: self.getValues('3')).grid(row=0, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='+', width=5, command=lambda: self.operate('+')).grid(row=0, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='4', width=5, command=lambda: self.getValues('4')).grid(row=1, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='5', width=5, command=lambda: self.getValues('5')).grid(row=1, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='6', width=5, command=lambda: self.getValues('6')).grid(row=1, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='-', width=5, command=lambda: self.operate('-')).grid(row=1, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='7', width=5, command=lambda: self.getValues('7')).grid(row=2, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='8', width=5, command=lambda: self.getValues('8')).grid(row=2, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='9', width=5, command=lambda: self.getValues('9')).grid(row=2, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='x', width=5, command=lambda: self.operate('*')).grid(row=2, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='0', width=5, command=lambda: self.getValues('0')).grid(row=3, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='.', width=5, command=lambda: self.getValues('.')).grid(row=3, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='c', width=5, command=self.clear).grid(row=3, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='/', width=5, command=lambda: self.operate('/')).grid(row=3, column=3, padx=5, pady=5)
        Button(self.buttonFm, text='=', width=15, command=self.calculate).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.but = Button(self.buttonFm, text='OFF', width=5, command=self.ofon)
        self.but.grid(row=4, column=3, columnspan=2, padx= 5, pady=5)
        self.state = 'off'
        self.answer.set(0)
        self.result =  0
        self.container. mainloop()

    def getValues(self, value):
        if self.screen.get()!="":
            if self.screen.get() == "0" or self.result ==1:
                self.answer.set(value)
            else:
                self.answer.set(self.screen.get() + value)
                self.resul = 0

    def operate(self, op):
        if self.screen.get() !="":
            self.operator = op
            self.fval = float(self.screen.get())
            self.answer.set(0)
    
    def clear(self):
        if self.screen.get() != " ":
            self.answer.set(0)

    def calculate(self):
        if self.screen.get()!= " ":
            # self.answe.set(eval(self.screen.get()))
            self.sval = float(self.screen.get())
            if self.operator == "+":
                self.answer.set(self.fval + self.sval)
                self.result =1
            elif self.operator == "-":
                self.answer.set(self.fval - self.sval)
                self.result = 1
            elif self.operator == "*":
                self.answer.set(self.fval * self.sval)
                self.result = 1
            elif self.operator == "/":
                self.answer.set(self.fval / self.sval)
                self.result = 1


        else:
                self.answer.set(self.screen.get() + value)
                self.answerN.set(self.screenN.get() + value)
                self.result = 0


    def ofon(self):
        if self.state == "on":
            self.answer.set(0)
            self.state = "off"
            self.but.configure(text="OFF")
        else:
            self.answer.set(" ")
            self.state = "on"
            self.but.configure(text="ON")
 


sc = SimpleCal()
