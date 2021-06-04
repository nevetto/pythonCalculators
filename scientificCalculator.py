from tkinter import*
from math import *
from math import exp, expm1
class SimpleCal:
    def __init__(self):
        self.container = Tk()
        self.screenBm = Frame(self.container)
        self.screenBm.pack()
        self.answerN = IntVar()
        self.screenN =Entry(self.screenBm, textvariable=self.answerN, width=14,font=('arial',20), state='normal', background = 'blue')
        self.screenN.pack()
        self.screenFm = Frame(self.container)
        self.screenFm.pack()
        self.answer = StringVar()
        self.screen = Entry(self.screenFm, textvariable=self.answer, width=14,font=('arial',20), state='disabled', disabledbackground = 'red')
        self.screen.pack()
        self.buttonFm = Frame(self.container)
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

        self.state = 'off'
        self.answer.set(0)
        self.answerN.set("")
        self.result =  0
        self.container. mainloop()

    def getValues(self, value):
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
            self.result = 0

    


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

    # def sqrt(self):
    #     self.answer.set(math.sqrt(x))


    def sqroot(self):
        if self.screen.get()!= " ": 
            self.s = self.screen.get()
#            self.sqroot = sqrt(eval(self.s))
            self.answer.set(sqrt(eval(self.s)))
            self.answerN.set('sqrt('+ str(self.s +')'))
#             # result = sqrt(eval(self.s))
#             self.screen.delete(0, END)
# #            self.display.insert(0, self.sqroot)
#             self.screen.insert(0, self.answer.set())
#         else:
#             self.screen.delete(0, END)
#             self.screen.insert(0, 'Invalid operation')

    def pow(self):
        if self.screen.get()!=' ':
            self.p = float(self.screen.get())
            self.answer.set(pow(self.p,self.p))
            self.answerN.set('pow('+ str(self.p) +')')

    def sqr(self):
        if self.screen.get()!=' ':
            self.sq = float(self.screen.get())
            self.answer.set(pow(self.sq,2))
            self.answerN.set('sqr('+ str(self.sq) +')')

    def abss(self):
        self.ab = float(self.screen.get())
        self.answer.set(abs(self.ab))
        self.answerN.set('abs('+ str(self.ab) +')')

    def loga(self):
        self.ab = float(self.screen.get())
        self.answer.set(log10(self.ab))
        self.answerN.set('log('+ str(self.ab) +')')


    def pii(self):
        self.ab = int(self.screen.get())
        self.answer.set((self.ab))
        self.answerN.set(pi(self.ab))

    def expo(self):
        self.ab = float(self.screen.get())
        self.answer.set(exp(self.ab))
        self.answerN.set('=' +str(self.ab))

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
        self.answer.set(tan(self.ab))
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

    

sc = SimpleCal()