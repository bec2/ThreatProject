from tkinter import *

#establishing the Window class and giving it an exit button
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.pack(fill=BOTH, expand=1)
        exitButton = Button(self, text="Quit", command=self.clickExitButton)
        exitButton.place(x=0, y=0)
    def clickExitButton(self):
        exit()

#establishing a root window for the software
root = Tk()
app = Window(root)

#naming the window and setting a size
root.wm_title("Testing Text")
root.geometry("320x200")


#run
root.mainloop()


