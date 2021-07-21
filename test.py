from tkinter import *

#need to declare this to display things later
root=Tk()

#Establishing the variables for added devices
d1=IntVar()
d2=IntVar()
d3=IntVar()
d4=IntVar()
d5=IntVar()
d6=IntVar()
d7=IntVar()
d8=IntVar()
d9=IntVar()
d10=IntVar()
d11=IntVar()
d12=IntVar()
d13=IntVar()

def click1():
    d1=1

#establishing the Window class and giving it an exit button
class Window(Frame):

    global d1
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.pack(fill=BOTH, expand=1)

        #adding title and body
        text1 = Label(self, text="Welcome!", bg="#996Db6", font=("Geneva", 25))
        text1.place(x=70,y=10)

        text2 = Label(self,
                      text="Please select your devices to get started.",
                      bg="#996Db6", font=("Geneva",15))
        text2.place(x=70,y=85)

        #device list, toggle status stored in corresponding d intvar
        c1=Checkbutton(root, text="Home virtual assistant (e.g. Alexa, Nest)",
                       command=click1)
        c1.pack()

        c2=Checkbutton(root, text="Bitdefender BOX", variable=d2)
        c2.pack()

        c3=Checkbutton(root, text="Smart security cam (e.g. Nest Cam)",
                       variable=d3)
        c3.pack()

        c4=Checkbutton(root, text="Smart doorbell", variable=d4)
        c4.pack()

        c5=Checkbutton(root, text="Smart lighting (e.g. Hue)", variable=d5)
        c5.pack()

        c6=Checkbutton(root, text="Smart fitness aid (e.g. SmartMat)",
                       variable=d6)
        c6.pack()

        c7=Checkbutton(root, text="Smart kitchenwear", variable=d7)
        c7.pack()

        c8=Checkbutton(root, text="Smart home security locks", variable=d8)
        c8.pack()

        c9=Checkbutton(root, text="Amazon Dash button", variable=d9)
        c9.pack()

        c10=Checkbutton(root, text="Smart thermostat / air monitor",
                        variable=d10)
        c10.pack()

        c11=Checkbutton(root, text="Automated 'smart home' controller",
                        variable=d11)
        c11.pack()

        c12=Checkbutton(root, text="Smart sleep tracker", variable=d12)
        c12.pack()

        c13=Checkbutton(root, text="Any other smart home devices",
                        variable=d13)
        c13.pack()

        #Exit button
        exitButton = Button(self, text="Quit", command=self.clickExitButton)
        exitButton.place(x=70, y=160)

        #Next button
        nextButton = Button(self, text="Next", command=self.clickNextButton)
        nextButton.place(x=750, y=160)                

    #Define what clicking the exit button does
    def clickExitButton(self):
        exit()

    #Define what clicking the next button does
    #NEED TO FIX 
    def clickNextButton(self):
        if self.d1.get() == 0:
            top = Toplevel(root)
            top.geometry("600x80")
            top.title("Uh oh!")
            Label(top, text="Select your devices first!",
                  font=('Geneva 20')).place(x=150, y=10)
        else:
            for widgets in frame.winfo_children():
                widgets.destroy()

        
#establishing the root window
app = Window(root)

#naming the window and setting a size
root.wm_title("My Threat Model")
root.geometry("875x500")
app['bg']='#996Db6'

#run
root.mainloop()


