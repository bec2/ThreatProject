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
        text1 = Label(self, text="Welcome!", bg="#996Db6", font=("Geneva", 25))
        text1.place(x=70,y=90)

        text2 = Label(self,
                      text="Welcome to My Threat Model. Please select your devices to get started.",
                      bg="#996Db6", font=("Geneva",15))
        text2.place(x=70,y=130)

    #Define what clicking the exit button does
    def clickExitButton(self):
        exit()
        
#establishing a root window for the software
root = Tk()
app = Window(root)


#naming the window and setting a size
root.wm_title("My Threat Model")
root.geometry("1000x500")
app['bg']='#996Db6'

#some tickboxes
c=Checkbutton(root, text="Home Virtual Assistant (e.g. Alexa, Home)")
c.pack()

c2=Checkbutton(root, text="Bitdefender BOX")
c2.pack()

c3=Checkbutton(root, text="Smart security cameras (e.g. Nest Cam)")
c3.pack()

c4=Checkbutton(root, text="Smart doorbell (e.g. Ring)")
c4.pack()

c5=Checkbutton(root, text="Smart lighting (e.g. Hue)")
c5.pack()

c6=Checkbutton(root, text="Smart fitness aids (e.g. SmartMat)")
c6.pack()

c7=Checkbutton(root, text="Smart kitchenwear")
c7.pack()

c8=Checkbutton(root, text="Smart home security locks")
c8.pack()

c9=Checkbutton(root, text="Amazon IoT Dash Button")
c9.pack()

c10=Checkbutton(root, text="Smart thermostats and air monitors")
c10.pack()

c11=Checkbutton(root, text="Automated 'smart home' controller")
c11.pack()

c12=Checkbutton(root, text="Smart sleep tracker")
c12.pack()

c13=Checkbutton(root, text="Any other smart home devices")
c13.pack()



#run
root.mainloop()


