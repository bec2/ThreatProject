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

#device tickboxes, the toggle status is stored in the corresponding d intvar
d1=IntVar()
c1=Checkbutton(root, text="Home Virtual Assistant (e.g. Alexa, Home)",
               variable=d1)
c1.pack()

d2=IntVar()
c2=Checkbutton(root, text="Bitdefender BOX", variable=d2)
c2.pack()

d3=IntVar()
c3=Checkbutton(root, text="Smart security cameras (e.g. Nest Cam)",
               variable=d3)
c3.pack()

d4=IntVar()
c4=Checkbutton(root, text="Smart doorbell (e.g. Ring)", variable=d4)
c4.pack()

d5=IntVar()
c5=Checkbutton(root, text="Smart lighting (e.g. Hue)", variable=d5)
c5.pack()

d6=IntVar()
c6=Checkbutton(root, text="Smart fitness aids (e.g. SmartMat)", variable=d6)
c6.pack()

d7=IntVar()
c7=Checkbutton(root, text="Smart kitchenwear", variable=d7)
c7.pack()

d8=IntVar()
c8=Checkbutton(root, text="Smart home security locks", variable=d8)
c8.pack()

d9=IntVar()
c9=Checkbutton(root, text="Amazon IoT Dash Button", variable=d9)
c9.pack()

d10=IntVar()
c10=Checkbutton(root, text="Smart thermostats and air monitors", variable=d10)
c10.pack()

d11=IntVar()
c11=Checkbutton(root, text="Automated 'smart home' controller", variable=d11)
c11.pack()

d12=IntVar()
c12=Checkbutton(root, text="Smart sleep tracker", variable=d12)
c12.pack()

d13=IntVar()
c13=Checkbutton(root, text="Any other smart home devices", variable=d13)
c13.pack()


#run
root.mainloop()


