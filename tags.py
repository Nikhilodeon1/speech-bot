import tkinter as tk
import tkinter.font as tkFont
from converter import transcript
from result import output, abort
class App:

    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1000
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_60=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=60)
        GLabel_60["font"] = ft
        GLabel_60["fg"] = "#333333"
        GLabel_60["justify"] = "center"
        GLabel_60["text"] = "SpeechBot Pro"
        GLabel_60.place(x=100,y=0,width=607,height=86)

        GListBox_337=tk.Listbox(root)
        GListBox_337["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=10)
        GListBox_337["font"] = ft
        GListBox_337["fg"] = "#333333"
        GListBox_337["justify"] = "center"
        GListBox_337.place(x=10,y=90,width=600,height=0)

        GLabel_173=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        GLabel_173["font"] = ft
        GLabel_173["fg"] = "#333333"
        GLabel_173["justify"] = "center"
        GLabel_173["text"] = "(C) Nikhil 2023"
        GLabel_173.place(x=0,y=610,width=87,height=30)

        GButton_725=tk.Button(root)
        GButton_725["bg"] = "#1e9fff"
        GButton_725["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=40)
        GButton_725["font"] = ft
        GButton_725["fg"] = "#000000"
        GButton_725["justify"] = "center"
        GButton_725["text"] = "Chat"
        GButton_725["relief"] = "ridge"
        GButton_725.place(x=90,y=110,width=420,height=182)
        GButton_725["command"] = self.thingy

        GButton_707=tk.Button(root)
        GButton_707["bg"] = "#ff5656"
        ft = tkFont.Font(family='Times',size=10)
        GButton_707["font"] = ft
        GButton_707["fg"] = "#000000"
        GButton_707["justify"] = "center"
        GButton_707["text"] = "Abort"
        GButton_707.place(x=90,y=300,width=111,height=30)
        GButton_707["command"] = self.abort2

    def abort2(self):
        abort()

    def thingy(self):
        print("here")
        trans = transcript()
        GLabel_571=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=20)
        GLabel_571["font"] = ft
        GLabel_571["fg"] = "#333333"
        GLabel_571["justify"] = "center"
        a = trans.split("|")
        str69 = ""
        for elm in a:
            str69 += elm + " "
        print(str69)
        GLabel_571["text"] = "You Said: {}".format(str69.lower())
        GLabel_571.place(x=10,y=330,width=599,height=43)
        output(trans)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
