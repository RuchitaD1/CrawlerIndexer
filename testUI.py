import Tkinter




def ui():

    top=Tkinter.Tk()
    E1 = Tkinter.Entry(top, bd =5)
    E1.pack(side = Tkinter.RIGHT)
    def getQuery():
        t1=E1.get()
        return t1

    B = Tkinter.Button(top, text ="Hello", command = getQuery)

    B.pack()
    top.mainloop()
ui()

