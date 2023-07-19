from tkinter import *

from _decimal import Decimal


class InterfaceMain():
    operation = ""
    lastOperation = ""
    comparation = ""
    result = 0
    firsEntronce = True

    def ejctMain(self):

        # ------------------- Main -------------------------------
        tkRoot = Tk()
        tkRoot.title("Calculadora")
        tkRoot.iconbitmap("C:/Users/valen/OneDrive/Fotos/Saved Pictures/calculator-icon_34473.ico")
        tkRoot.config(bg="#191919", highlightcolor="#191919", highlightbackground="#191919", background="#191919")
        tkRoot.resizable(0, 0)
        tkRoot.geometry("250x200")
        frameMain = Frame(tkRoot, bg="#191919")
        frameMain.pack()
        frameMain.config(width="200", height="400")

        # ------------------- Windows -------------------------------
        numWin = StringVar()

        entryWindows = Entry(frameMain, textvariable=numWin)
        entryWindows.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
        entryWindows.config(bg="#191919", fg="#00ff00", justify="right")
        entryWindows.insert(0, "0")

        # ------------------- File buttons1 -------------------------------
        button7 = Button(frameMain, text="7", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("7"))
        button7.grid(row=2, column=1, pady=1, padx=1)
        button8 = Button(frameMain, text="8", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("8"))
        button8.grid(row=2, column=2, pady=1, padx=1)
        button9 = Button(frameMain, text="9", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("9"))
        button9.grid(row=2, column=3, pady=1, padx=1)
        buttonDiv = Button(frameMain, text="/", width=4, bg="#777777", fg="#ffffff",
                           command=lambda: div(numWin.get()))
        buttonDiv.grid(row=2, column=4, pady=1, padx=1)

        # ------------------- File buttons2 -------------------------------
        button4 = Button(frameMain, text="4", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("4"))
        button4.grid(row=3, column=1, pady=1, padx=1)
        button5 = Button(frameMain, text="5", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("5"))
        button5.grid(row=3, column=2, pady=1, padx=1)
        button6 = Button(frameMain, text="6", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("6"))
        button6.grid(row=3, column=3, pady=1, padx=1)
        buttonMulti = Button(frameMain, text="x", width=4, bg="#777777", fg="#ffffff",
                             command=lambda: multi(numWin.get()))
        buttonMulti.grid(row=3, column=4)

        # ------------------- File buttons3 -------------------------------
        button1 = Button(frameMain, text="1", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("1"))
        button1.grid(row=4, column=1, pady=1, padx=1)
        button2 = Button(frameMain, text="2", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("2"))
        button2.grid(row=4, column=2, pady=1, padx=1)
        button3 = Button(frameMain, text="3", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("3"))
        button3.grid(row=4, column=3, pady=1, padx=1)
        buttonRest = Button(frameMain, text="-", width=4, bg="#777777", fg="#ffffff",
                            command=lambda: resta(numWin.get()))
        buttonRest.grid(row=4, column=4, pady=1, padx=1)

        # ------------------- File buttons4 -------------------------------
        buttonCom = Button(frameMain, text=".", width=4, bg="#777777", fg="#ffffff",
                           command=lambda: actionButtonPress("."))
        buttonCom.grid(row=5, column=1, pady=1, padx=1)
        button0 = Button(frameMain, text="0", width=4, bg="#777777", fg="#ffffff",
                         command=lambda: actionButtonPress("0"))
        button0.grid(row=5, column=2, pady=1, padx=1)
        buttonEqual = Button(frameMain, text="=", width=4, bg="#777777", fg="#ffffff",
                             command=lambda: theResult())
        buttonEqual.grid(row=5, column=3, pady=1, padx=1)
        buttonPlus = Button(frameMain, text="+", width=4, bg="#777777", fg="#ffffff",
                            command=lambda: suma(numWin.get()))
        buttonPlus.grid(row=5, column=4, pady=1, padx=1)

        # ------------------- File buttons5 -------------------------------

        buttonClear = Button(frameMain, text="Clear", width=8, bg="#777777", fg="#ffffff",
                             command=lambda: actionButtonClear(True))
        buttonClear.grid(row=6, column=1, pady=1, columnspan=4, rowspan=4, sticky="w")

        # ------------------- Method action buttons -------------------------------
        def actionButtonPress(num):
            if (self.operation == ""):
                if numWin.get() == "0" and num != ".":
                    numWin.set(num)
                elif (numWin.get().endswith(',') and num == ",") or \
                        (numWin.get().__contains__(".") and num == "."):
                    numWin.set(numWin.get())
                else:
                    numWin.set(numWin.get() + num)


            else:
                numWin.set(num)
                self.operation = ""

        def actionButtonClear(clear):
            if clear:
                numWin.set("0")
                self.result = 0
                self.lastOperation = ""
                self.operation = ""
                self.comparation=""
                self.firsEntronce = True

        def suma(num):
            a = False
            self.operation = "suma"
            self.lastOperation = "suma"
            if (self.comparation != "" and self.lastOperation != "" and self.comparation != self.lastOperation):
                theResultComparation()
                a=True
                self.comparation = ""

            if a!=True:
                self.result += Decimal(num)
                numWin.set(self.result)
                self.comparation = "suma"

        def resta(num):
            a = False
            self.operation = "resta"
            self.lastOperation = "resta"
            if (self.comparation != "" and self.lastOperation != "" and self.comparation != self.lastOperation):
                theResultComparation()
                a=True
                self.comparation = ""

            if(a!=True):
                self.comparation = "resta"
                if (self.result == 0):
                    self.result = Decimal(num) - self.result
                    numWin.set(self.result)
                elif (self.result > Decimal(num)):
                    self.result = self.result - Decimal(num)
                    numWin.set(self.result)
                else:
                    self.result = Decimal(num) - self.result
                    numWin.set(self.result)


        def multi(num):
            a = False
            self.operation = "multi"
            self.lastOperation = "multi"
            if (numWin.get() != 0 and self.result == 0):
                self.result = 1
            if (self.comparation != "" and self.lastOperation != "" and self.comparation != self.lastOperation):
                theResultComparation()
                a=True
                self.comparation = ""
            if(a!=True):
                self.result *= Decimal(num)
                numWin.set(self.result)
                self.comparation = "multi"


        def div(num):
            a = False
            self.operation = "div"
            self.lastOperation = "div"
            if (numWin.get() != 0 and self.result == 0):
                self.result = 1
                self.firsEntronce = False
            if (self.comparation != "" and self.lastOperation != "" and self.comparation != self.lastOperation):
                theResultComparation()
                a = True
                self.comparation = ""

            if(a!=True):
                self.result *= Decimal(num) / self.result
                numWin.set(self.result)
                self.comparation = "div"


        def theResult():
            if (self.lastOperation == "suma"):
                numWin.set(self.result + Decimal(numWin.get()))
                self.result = 0
                self.lastOperation = ""
                self.comparation = ""
            elif (self.lastOperation == "resta"):
                if (self.result == 0):
                    numWin.set(self.result - Decimal(numWin.get()))
                elif (self.result > Decimal(numWin.get())):
                    numWin.set(self.result - Decimal(numWin.get()))
                else:
                    numWin.set(Decimal(numWin.get()) - self.result)
                self.result = 0
                self.lastOperation = ""
                self.comparation = ""
            elif (self.lastOperation == "multi"):
                numWin.set(self.result * Decimal(numWin.get()))
                self.result = 0
                self.lastOperation = ""
                self.comparation = ""
            elif (self.lastOperation == "div"):
                numWin.set(self.result / Decimal(numWin.get()))
                self.result = 0
                self.lastOperation = ""
                self.comparation = ""
            else:
                self.lastOperation = ""
                self.comparation = ""
                self.result = 0

        def theResultComparation():
            if (self.comparation == "suma"):
                numWin.set(self.result + Decimal(numWin.get()))
                self.result = Decimal(numWin.get())
            elif (self.comparation == "resta"):
                if (self.result == 0):
                    numWin.set(self.result - Decimal(numWin.get()))
                elif (self.result > Decimal(numWin.get())):
                    numWin.set(self.result - Decimal(numWin.get()))
                else:
                    numWin.set(Decimal(numWin.get()) - self.result)
                self.result =  Decimal(numWin.get())
            elif (self.comparation == "multi"):
                numWin.set(self.result * Decimal(numWin.get()))
                self.result =  Decimal(numWin.get())
            elif (self.comparation == "div"):
                numWin.set(self.result / Decimal(numWin.get()))
                self.result =  Decimal(numWin.get())
            else:
                self.lastOperation = ""
                self.result = 0

        tkRoot.mainloop()
