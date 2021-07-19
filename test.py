from tkinter import *

#establishing the Window class and giving it an exit button
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.pack(fill=BOTH, expand=1)

        #Our window should have an exit button at all times
        exitButton = Button(self, text="Quit", command=self.clickExitButton)
        exitButton.place(x=900, y=160)

        #adding title and body
        text1 = Label(self, text="Welcome!", bg="#996Db6", font=("Helvetica", 25))
        text1.place(x=70,y=90)

        text2 = Label(self,
                      text="Welcome to My Threat Model. Please select your devices to get started.",
                      bg="#996Db6", font=("Helvetica",15))
        text2.place(x=70,y=130)

    #Define what clicking the exit button does
    def clickExitButton(self):
        exit()

#establishing a root window for the software
root = Tk()
app = Window(root)

#naming the window and setting a size
root.wm_title("My Threat Model")
root.geometry("1000x200")
app['bg']='#996Db6'


#run
root.mainloop()


