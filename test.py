from tkinter import *

#need to declare this to display things later
root=Tk()

#Establishing the variables for added devices
d1=bool()
d2=bool()
d3=bool()
d4=bool()
d5=bool()
d6=bool()
d7=bool()
d8=bool()
d9=bool()
d10=bool()
d11=bool()
d12=bool()
d13=bool()

#Declaring a way to hold the status of a checkbox
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
check6 = IntVar()
check7 = IntVar()
check8 = IntVar()
check9 = IntVar()
check10 = IntVar()
check11 = IntVar()
check12 = IntVar()
check13 = IntVar()

#define onclick functions for checkboxes
def click1():
    global d1
    global check1

    if check1.get() :
        d1 = 1
    else:
        d1 = 0

def click2():
    global d2
    global check2

    if check2.get() :
        d2 = 1
    else:
        d2 = 0

def click3():
    global d3
    global check3

    if check3.get() :
        d3 = 1
    else:
        d3 = 0

def click4():
    global d4
    global check4

    if check4.get() :
        d4 = 1
    else:
        d4 = 0

def click5():
    global d5
    global check5

    if check5.get() :
        d5 = 1
    else:
        d5 = 0

def click6():
    global d6
    global check6

    if check6.get() :
        d6 = 1
    else:
        d6 = 0

def click7():
    global d7
    global check7

    if check7.get() :
        d7 = 1
    else:
        d7 = 0

def click8():
    global d8
    global check8

    if check8.get() :
        d8 = 1
    else:
        d8 = 0

def click9():
    global d9
    global check9

    if check9.get() :
        d9 = 1
    else:
        d9 = 0

def click10():
    global d10
    global check10

    if check10.get() :
        d10 = 1
    else:
        d10 = 0

def click11():
    global d11
    global check11

    if check11.get() :
        d11 = 1
    else:
        d11 = 0

def click12():
    global d12
    global check12

    if check12.get() :
        d12 = 1
    else:
        d12 = 0

def click13():
    global d13
    global check13

    if check13.get() :
        d13 = 1
    else:
        d13 = 0

#establishing the Window class and giving it an exit button
class Window(Frame):

    
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
        self.c1=Checkbutton(root, text="Home virtual assistant (e.g. Alexa, Nest)",
                       variable=check1, onvalue=1, offvalue=0, command=click1)
        self.c1.pack()

        self.c2=Checkbutton(root, text="Bitdefender BOX", variable=check2, onvalue=1,
                       offvalue=0, command=click2)
        self.c2.pack()

        self.c3=Checkbutton(root, text="Smart security cam (e.g. Nest Cam)",
                       variable=check3, onvalue=1, offvalue=0, command=click3)
        self.c3.pack()

        self.c4=Checkbutton(root, text="Smart doorbell", variable=check4, onvalue=1,
                       offvalue=0, command=click4)
        self.c4.pack()

        self.c5=Checkbutton(root, text="Smart lighting (e.g. Hue)", variable=check5,
                       onvalue=1, offvalue=0, command=click5)
        self.c5.pack()

        self.c6=Checkbutton(root, text="Smart fitness aid (e.g. SmartMat)",
                       variable=check6, onvalue=1, offvalue=0, command=click6)
        self.c6.pack()

        self.c7=Checkbutton(root, text="Smart kitchenwear", variable=check7,
                       onvalue=1, offvalue=0, command=click7)
        self.c7.pack()

        self.c8=Checkbutton(root, text="Smart home security locks", variable=check8,
                       onvalue=1, offvalue=0, command=click8)
        self.c8.pack()

        self.c9=Checkbutton(root, text="Amazon Dash button", variable=check9,
                       onvalue=1, offvalue=0, command=click9)
        self.c9.pack()

        self.c10=Checkbutton(root, text="Smart thermostat / air monitor",
                        variable=check10, onvalue=1, offvalue=0, command=click10)
        self.c10.pack()

        self.c11=Checkbutton(root, text="Automated 'smart home' controller",
                        variable=check11, onvalue=1, offvalue=0, command=click11)
        self.c11.pack()

        self.c12=Checkbutton(root, text="Smart sleep tracker", variable=check12,
                        onvalue=1, offvalue=0, command=click12)
        self.c12.pack()

        self.c13=Checkbutton(root, text="Any other smart home devices",
                        variable=check13, onvalue=1, offvalue=0, command=click13)
        self.c13.pack()

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
    def clickNextButton(self):
        if d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0 and d5 == 0 and d6 == 0 and d7 == 0 and d8 == 0 and d9 == 0 and d10 == 0 and d11 == 0 and d12 == 0 and d13 == 0:
            top = Toplevel(root)
            top.geometry("600x80")
            top.title("Uh oh!")
            Label(top, text="Select your devices first!",
                  font=('Geneva 20')).place(x=150, y=10)
        else:
            self.pack_forget()
            self.c1.forget()
            self.c2.forget()
            self.c3.forget()
            self.c4.forget()
            self.c5.forget()
            self.c6.forget()
            self.c7.forget()
            self.c8.forget()
            self.c9.forget()
            self.c10.forget()
            self.c11.forget()
            self.c12.forget()
            self.c13.forget()
            page2()

#Setting out what page 2 is
def page2():

    class Window2(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master=master
            self.pack(fill=BOTH, expand=1)
            
            text1=Label(self, text="Just a few more questions...",
                        font=("Geneva 20"), bg='#996Db6')
            text1.place(x=70,y=10)

            text2=Label(self, text="Tick the boxes if the following apply to you.",
                        font=("Geneva 15"), bg='#996Db6')
            text2.place(x=70, y=50)

            #new checkboxes for mitigating factors

            self.c1=Checkbutton(root,
                                text="I connect my home devices to Wi-Fi networks that aren't my own.")
            self.c1.pack()

            self.c2=Checkbutton(root,
                                text="My online accounts aren't all protected with 2FA where possible.")
            self.c2.pack()

            self.c3=Checkbutton(root,
                                text="My Wi-Fi password is still the default one the router box came with.")
            self.c3.pack()

            self.c4=Checkbutton(root,
                                text="Not all of my passwords have combined capitals and lowercases, numbers, and symbols.")
            self.c4.pack()

            self.c5=Checkbutton(root,
                                text="My voice controlled devices are sometimes in places with thin walls / windows that let sound through.")
            self.c5.pack()

            self.c6=Checkbutton(root,
                                text="I have not opted out of company processing of my voice commands.")
            self.c6.pack()

            self.c7=Checkbutton(root,
                                text="I leave my voice activated devices on when I am not using them, or having other conversations.")
            self.c7.pack()

            self.c8=Checkbutton(root,
                                text="I don't have all my devices updates to the most recent patch.")
            self.c8.pack()

            self.c9=Checkbutton(root,
                                text="I have installed apps or skills from sources I don't recognise or trust.")
            self.c9.pack()

            self.c10=Checkbutton(root,
                                 text="I have home devices from sources I don't recognise or trust.")
            self.c10.pack()

            self.c11=Checkbutton(root,
                                 text="I have a virtual assistant hub registered to my account that other people in my home interact with.")
            self.c11.pack()

            self.c12=Checkbutton(root,
                                 text="My devices aren't set up to generate some arbitrary digital traffic when I'm not home.")
            self.c12.pack()

            self.c13=Checkbutton(root,
                                 text="I haven't opted out of third party data processing or collection where possible in my devices.")
            self.c13.pack()

            self.c14=Checkbutton(root,
                                 text="I didn't fully read the terms of service or processing rules for at least one of my devices.")
            self.c14.pack()
            

    app = Window2(root)
    root.wm_title("My Threat Model")
    root.geometry("875x500")
    app['bg']='#996Db6'


#establishing the root window
app = Window(root)

#naming the window and setting a size
root.wm_title("My Threat Model")
root.geometry("875x500")
app['bg']='#996Db6'

#run
root.mainloop()


