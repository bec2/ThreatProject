#    Copyright (C) 2021  Beckett LeClair
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
import webbrowser

#need to declare this to display things later
root=Tk()

#Establishing the variables for added devices
d1=bool() #Home virtual assistant
d2=bool() #Bitdefender BOX
d3=bool() #Smart security cam
d4=bool() #Smart doorbell
d5=bool() #Smart lighting
d6=bool() #Smart fitness aid
d7=bool() #Smart kitchenware
d8=bool() #Smart home security locks
d9=bool() #Amazon Dash
d10=bool()#Smart thermostat or air monitor
d11=bool()#Automated smart home controller
d12=bool()#Sleep tracker
d13=bool()#Any other

#Establishing the variables for risk factors
r1=bool() #other wifi networks used
r2=bool() #lacking 2fa
r3=bool() #default router passwd
r4=bool() #weak passwd
r5=bool() #sound can travel
r6=bool() #opted in to voice processing
r7=bool() #leave mic on
r8=bool() #unpatched
r9=bool() #unrecognised apps
r10=bool()#unrecognised devices
r11=bool()#other users
r12=bool()#no arbitrary traffic
r13=bool()#opted in to 3rd party processing
r14=bool()#didn't read tos

#Making a way to hold the status of a checkbox
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

checkB1 = IntVar()
checkB2 = IntVar()
checkB3 = IntVar()
checkB4 = IntVar()
checkB5 = IntVar()
checkB6 = IntVar()
checkB7 = IntVar()
checkB8 = IntVar()
checkB9 = IntVar()
checkB10 = IntVar()
checkB11 = IntVar()
checkB12 = IntVar()
checkB13 = IntVar()
checkB14 = IntVar()

#Sort categories for the modelling algorithm
catVoice = bool()   #voice input devices
catSign = bool()    #device types generally requiring sign in to function
catIntern = bool()  #devices connecting to the internal network
catExtern = bool()  #devices communicating over the internet
catSecure = bool()  #devices affecting physical home security

#Threat base scores - taken from avg of the associated cvss values to 1dp
#The numbers relate to the matching threat from STRIDE - see paper
stride1 = float(3.8)
stride2 = float(5.8)
stride3 = float(6.6)
stride4 = float(6.1)
stride5 = float(3.9)
stride6 = float(5.6)
stride7 = float(6.4)
stride8 = float(4.8)
stride9 = float(3.0)
stride10 = float(4.9)
stride11 = float(5.5)
stride12 = float(4.6)
stride13 = float(4.3)
stride14 = float(4.2)
stride15 = float(7.1)
stride16 = float(7.1)

#Way to check if a stride variable is turned on or not
strideOn1 = bool()
strideOn2 = bool()
strideOn3 = bool()
strideOn4 = bool()
strideOn5 = bool()
strideOn6 = bool()
strideOn7 = bool()
strideOn8 = bool()
strideOn9 = bool()
strideOn10 = bool()
strideOn11 = bool()
strideOn12 = bool()
strideOn13 = bool()
strideOn14 = bool()
strideOn15 = bool()
strideOn16 = bool()

#Initialise variables for holding up to 16 calculations for 16 stride categs
calc1 = float()
calc2 = float()
calc3 = float()
calc4 = float()
calc5 = float()
calc6 = float()
calc7 = float()
calc8 = float()
calc9 = float()
calc10 = float()
calc11 = float()
calc12 = float()
calc13 = float()
calc14 = float()
calc15 = float()
calc16 = float()

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

#same as above, but for risk factor variables
def clickB1():
    global r1
    global checkB1
    if checkB1.get() :
        r1 = 1
    else:
        r1 = 0

def clickB2():
    global r2
    global checkB2
    if checkB2.get() :
        r2 = 1
    else:
        r2 = 0

def clickB3():
    global r3
    global checkB3
    if checkB3.get() :
        r3 = 1
    else:
        r3 = 0

def clickB4():
    global r4
    global checkB4
    if checkB4.get() :
        r4 = 1
    else:
        r4 = 0

def clickB5():
    global r5
    global checkB5
    if checkB5.get() :
        r5 = 1
    else:
        r5 = 0

def clickB6():
    global r6
    global checkB6
    if checkB5.get() :
        r6 = 1
    else:
        r6 = 0

def clickB7():
    global r7
    global checkB7
    if checkB7.get() :
        r7 = 1
    else:
        r7 = 0

def clickB8():
    global r8
    global checkB8
    if checkB8.get() :
        r8 = 1
    else:
        r8 = 0

def clickB9():
    global r9
    global checkB9
    if checkB9.get() :
        r9 = 1
    else:
        r9 = 0

def clickB10():
    global r10
    global checkB10
    if checkB10.get() :
        r10 = 1
    else:
        r10 = 0

def clickB11():
    global r11
    global checkB11
    if checkB11.get() :
        r11 = 1
    else:
        r10 = 0

def clickB12():
    global r12
    global checkB12
    if checkB12.get() :
        r12 = 1
    else:
        r12 = 0

def clickB13():
    global r13
    global checkB13
    if checkB13.get() :
        r13 = 1
    else:
        r13 = 0

def clickB14():
    global r14
    global checkB14
    if checkB14.get() :
        r14 = 1
    else:
        r14 = 0


#establishing the Window class
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

        #self.c2=Checkbutton(root, text="Bitdefender BOX", variable=check2, onvalue=1,
                       #offvalue=0, command=click2)
        #self.c2.pack()

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

        self.c7=Checkbutton(root, text="Smart kitchenware", variable=check7,
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
    #Check the user has selected at least one item before going ahead
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
            #self.c2.forget()
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

        def clickExitBtn2(self):
            exit()

        #Glossary for the terms on this page that might not be known
        def clickGBtn(self):
            top = Toplevel(root)
            top.geometry("600x250")
            top.title("Glossary")
            Label(top, text="2FA", font=('Geneva 12')).place(x=10, y=10)
            Label(top, text="A form of security that requires 2 identification steps to log in, e.g. a password and a ",
                  font=('Geneva 10')).place(x=10, y=30)
            Label(top, text="code sent to your phone.", font=('Geneva 10')).place(x=10, y=50)
            Label(top, text="Router", font=('Geneva 12')).place(x=10, y=80)
            Label(top, text="The box you connect to in order to get Wi-Fi.",
                  font=('Geneva 10')).place(x=10, y=100)
            Label(top, text="Patch", font=('Geneva 12')).place(x=10, y=130)
            Label(top, text="The latest update to your device or software that fixes some things from prior versions.",
                  font=('Geneva 10')).place(x=10, y=150)
            Label(top, text="Digital traffic", font=('Geneva 12')).place(x=10, y=180)
            Label(top, text="The signals being sent out and received from digital devices.",
                  font=('Geneva 10')).place(x=10, y=200)
            
            
        def clickNextBtn2(self):
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
            self.c14.forget()
            calculator()
        
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
            text3=Label(self, text="Click 'Glossary' if you don't understand a term.",
                        font=("Geneva 15"), bg='#996Db6')
            text3.place(x=70, y=75)

            #new checkboxes for risk factors

            self.c1=Checkbutton(root,
                                text="I connect my home devices to Wi-Fi networks that aren't my own.",
                                variable=checkB1, onvalue=1, offvalue=0,
                                command=clickB1)
            self.c1.pack()

            self.c2=Checkbutton(root,
                                text="My online accounts aren't all protected with 2FA where possible.",
                                variable=checkB2, onvalue=1, offvalue=0,
                                command=clickB2)
            self.c2.pack()

            self.c3=Checkbutton(root,
                                text="My Wi-Fi password is still the default one the router box came with.",
                                variable=checkB3, onvalue=1, offvalue=0,
                                command=clickB3)
            self.c3.pack()

            self.c4=Checkbutton(root,
                                text="Not all of my passwords have combined capitals and lowercases, numbers, and symbols.",
                                variable=checkB4, onvalue=1, offvalue=0,
                                command=clickB4)
            self.c4.pack()

            self.c5=Checkbutton(root,
                                text="My voice controlled devices are sometimes in places with thin walls / windows that let sound through.",
                                variable=checkB5, onvalue=1, offvalue=0,
                                command=clickB5)
            self.c5.pack()

            self.c6=Checkbutton(root,
                                text="I have not opted out of company processing of my voice commands.",
                                variable=checkB6, onvalue=1, offvalue=0,
                                command=clickB6)
            self.c6.pack()

            self.c7=Checkbutton(root,
                                text="I leave my voice activated devices on when I am not using them, or having other conversations.",
                                variable=checkB7, onvalue=1, offvalue=0,
                                command=clickB7)
            self.c7.pack()

            self.c8=Checkbutton(root,
                                text="I don't have all my devices updated to the most recent patch.",
                                variable=checkB8, onvalue=1, offvalue=0,
                                command=clickB8)
            self.c8.pack()

            self.c9=Checkbutton(root,
                                text="I have installed apps or skills from sources I don't recognise or trust.",
                                variable=checkB9, onvalue=1, offvalue=0,
                                command=clickB9)
            self.c9.pack()

            self.c10=Checkbutton(root,
                                 text="I have home devices from sources I don't recognise or trust.",
                                 variable=checkB10, onvalue=1, offvalue=0,
                                 command=clickB10)
            self.c10.pack()

            self.c11=Checkbutton(root,
                                 text="People other than the registered account holder(s) interface with the devices.",
                                 variable=checkB11, onvalue=1, offvalue=0,
                                 command=clickB11)
            self.c11.pack()

            self.c12=Checkbutton(root,
                                 text="My devices aren't set up to generate some arbitrary digital traffic when I'm not home.",
                                 variable=checkB12, onvalue=1, offvalue=0,
                                 command=clickB12)
            self.c12.pack()

            self.c13=Checkbutton(root,
                                 text="I haven't opted out of third party data processing or collection where possible in my devices.",
                                 variable=checkB13, onvalue=1, offvalue=0,
                                 command=clickB13)
            self.c13.pack()

            self.c14=Checkbutton(root,
                                 text="I didn't fully read the terms of service or processing rules for at least one of my devices.",
                                 variable=checkB14, onvalue=1, offvalue=0,
                                 command=clickB14)
            self.c14.pack()
            

            #buttons        
            exitButton2 = Button(self, text="Quit", command=self.clickExitBtn2)
            exitButton2.place(x=70, y=140)

            glossButton = Button(self, text="Glossary", command=self.clickGBtn)
            glossButton.place(x=390, y=140)

            nextButton2 = Button(self, text="Next", command=self.clickNextBtn2)
            nextButton2.place(x=750, y=140)

    app = Window2(root)
    app['bg']='#996Db6'

#A loading page displays text while the algorithm does its job
#This acts as a space to run all the calculations in the background
def calculator():

    class WindowC(Frame):

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master=master
            self.pack(fill=BOTH, expand=1)

            text1=Label(self, text="Calculating...", font=("Geneva 20"),
                        bg='#996Db6')
            text1.place(x=70,y=50)
            
    app = WindowC(root)
    app['bg']='#996Db6'
    
    #Depending on what devices were added, different categories get turned on
    #catIntern should be active for any device choice
    global catIntern
    catIntern = 1
    
    if d1 == 1 or d11 == 1 or d12 == 1:
        global catVoice
        catVoice = 1
    else:
        pass

    if d1 == 1 or d3 == 1 or d4 == 1 or d6 == 1 or d9 == 1 or d11 == 1 or d12 == 1 or d13 == 1:
        global catSign
        catSign = 1
    else:
        pass

    if d1 == 1 or d3 == 1 or d6 == 1 or d8 == 1 or d9 == 1 or d10 == 1 or d11 == 1 or d13 == 1:
        global catExtern
        catExtern = 1
    else:
        pass

    if d1 == 1 or d3 == 1 or d4 == 1 or d8 == 1 or d10 == 1 or d11 == 1 or d13 == 1:
        global catSecure
        catSecure = 1
    else:
        pass

    #Recall the values before we use them 
    global strideOn1
    global strideOn2
    global strideOn3
    global strideOn4
    global strideOn5
    global strideOn6
    global strideOn7
    global strideOn8
    global strideOn9
    global strideOn10
    global strideOn11
    global strideOn12
    global strideOn13
    global strideOn14
    global strideOn15
    global strideOn16

    global calc1
    global calc2
    global calc3
    global calc4
    global calc5
    global calc6
    global calc7
    global calc8
    global calc9
    global calc10
    global calc11
    global calc12
    global calc13
    global calc14
    global calc15
    global calc16

    #Turn on correct strideOn values per subcategory
    if catVoice == 1:
        strideOn1 = 1
        strideOn4 = 1
        strideOn7 = 1
        strideOn10 = 1
        strideOn11 = 1
        strideOn12 = 1
    else:
        pass

    if catSign == 1:
        strideOn2 = 1
        strideOn8 = 1
    else:
        pass

    if catIntern == 1:
        strideOn3 = 1
        strideOn6 = 1
        strideOn7 = 1
        strideOn9 = 1
        strideOn13 = 1
        strideOn14 = 1
        strideOn15 = 1
        strideOn16 = 1
    else:
        pass

    if catExtern == 1:
        strideOn2 = 1
        strideOn5 = 1
        strideOn8 = 1
        strideOn11 = 1
        strideOn13 = 1
        strideOn15 = 1
    else:
        pass

    if catSecure == 1:
        strideOn3 = 1
        strideOn6 = 1
        strideOn7 = 1
        strideOn9 = 1
        strideOn14 = 1
        strideOn16 = 1
    else:
        pass

    #Add stride cvss scores into totals if those stride values are on
    #This could probably be made more elegant with arrays if there is time
    if strideOn1 == 1:
        calc1 = stride1
    else:
        pass

    if strideOn2 == 1:
        calc2 = stride2
    else:
        pass

    if strideOn3 == 1:
        calc3 = stride3
    else:
        pass

    if strideOn4 == 1:
        calc4 = stride4
    else:
        pass

    if strideOn5 == 1:
        calc5 = stride5
    else:
        pass

    if strideOn6 == 1:
        calc6 = stride6
    else:
        pass

    if strideOn7 == 1:
        calc7 = stride7
    else:
        pass

    if strideOn8 == 1:
        calc8 = stride8
    else:
        pass

    if strideOn9 == 1:
        calc9 = stride9
    else:
        pass

    if strideOn10 == 1:
        calc10 = stride10
    else:
        pass

    if strideOn11 == 1:
        calc11 = stride11
    else:
        pass

    if strideOn12 == 1:
        calc12 = stride12
    else:
        pass

    if strideOn13 == 1:
        calc13 = stride13
    else:
        pass

    if strideOn14 == 1:
        calc14 = stride14
    else:
        pass

    if strideOn15 == 1:
        calc15 = stride15
    else:
        pass

    if strideOn16 == 1:
        calc16 = stride16
    else:
        pass

    #Add risk scores to totals depending on which risks are turned on
    #see paperwork for how risk scores are determined
    
    #'I connect my home devices to Wi-Fi networks that aren't mine'
    if checkB1 == 1:
        if calc2 > 0:
            calc2 = calc2 + 3
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 + 3
        else:
            pass
        if calc5 > 0:
            calc5 = calc5 + 3
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 3
        else:
            pass
        if calc7 > 0:
            calc7 = calc7 + 3
        else:
            pass
        if calc8 > 0:
            calc8 = calc8 + 3
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 + 3
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 + 3
        else:
            pass
        if calc13 > 0:
            calc13 = calc13 + 3
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 + 3
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 + 3
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 + 3
        else:
            pass
    else:
        pass

    #'My accounts aren't all using 2FA where possible'
    if checkB2 == 1:
        if calc1 > 0:
            calc1 = calc1 + 1
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 1
        else:
            pass
    else:
        pass

    #'My wi-fi passwd is the default one'
    if checkB3 == 1:
        if calc2 > 0:
            calc2 = calc2 + 2
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 + 2
        else:
            pass
        if calc5 > 0:
            calc5 = calc5 + 2
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 2
        else:
            pass
        if calc7 > 0:
            calc7 = calc7 + 2
        else:
            pass
        if calc8 > 0:
            calc8 = calc8 + 2
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 + 2
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 + 2
        else:
            pass
        if calc13 > 0:
            calc13 = calc13 + 2
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 + 2
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 + 2
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 + 2
        else:
            pass
    else:
        pass

    #'Not all my passwds are strong'
    if checkB4 == 1:
        if calc2 > 0:
            calc2 = calc2 + 2
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 + 2
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 2
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 + 2
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 + 2
        else:
            pass
        if cac16 > 0:
            calc16 = calc16 + 2
        else:
            pass
    else:
        pass

    #'My devices are in places with sound leaks'
    if checkB5 == 1:
        if calc1 > 0:
            calc1 = calc1 + 1
        else:
            pass
        if calc4 > 0:
            calc4 = calc4 + 1
        else:
            pass
        if calc10 > 0:
            calc10 = calc10 + 1
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 + 1
        else:
            pass
    else:
        pass

    #'I'm not opted out of first party processing'
    if checkB6 == 1:
        if calc11 > 0:
            calc11 = calc11 + 1
        else:
            pass
    else:
        pass

    #'I leave the mic on when doing other things'
    if checkB7 == 1:
        if calc1 > 0:
            calc1 = calc1 + 2
        else:
            pass
        if calc11 > 0:
            calc11 = calc11 + 2
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 + 2
        else:
            pass
    else:
        pass

    #'I don't have the latest patches'
    if checkB8 == 1:
        if calc15 > 0:
            calc15 = calc15 + 3
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 + 3
        else:
            pass
    else:
        pass

    #'I have untrusted skills or apps'
    if checkB9 == 1:
        if calc2 > 0:
            calc2 = calc2 + 3
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 + 3
        else:
            pass
        if calc5 > 0:
            calc5 = calc5 + 3
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 3
        else:
            pass
        if calc7 > 0:
            calc7 = calc7 + 3
        else:
            pass
        if calc8 > 0:
            calc8 = calc8 + 3
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 + 3
        else:
            pass
        if calc11 > 0:
            calc11 = calc11 + 3
        else:
            pass
        if calc13 > 0:
            calc13 = calc13 + 3
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 + 3
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 + 3
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 + 3
        else:
            pass
    else:
        pass

    #'I have untrusted devices'
    if checkB10 == 1:
        if calc2 > 0:
            calc2 = calc2 + 3
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 + 3
        else:
            pass
        if calc5 > 0:
            calc5 = calc5 + 3
        else:
            pass
        if calc6 > 0:
            calc6 = calc6 + 3
        else:
            pass
        if calc7 > 0:
            calc7 = calc7 + 3
        else:
            pass
        if calc8 > 0:
            calc8 = calc8 + 3
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 + 3
        else:
            pass
        if calc11 > 0:
            calc11 = calc11 + 3
        else:
            pass
        if calc13 > 0:
            calc13 = calc13 + 3
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 + 3
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 + 3
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 + 3
        else:
            pass
    else:
        pass

    #'unregistered users interface with the devices'
    if checkB11 == 1:
        if calc1 > 0:
            calc1 = calc1 + 2
        else:
            pass
        if calc10 > 0:
            calc10 = calc10 + 2
        else:
            pass
        if calc11 > 0:
            calc11 = calc11 + 2
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 + 2
        else:
            pass
    else:
        pass

    #'I don't generate arbitrary traffic while out'
    if checkB12 == 1:
        if calc9 > 0:
            calc9 = calc9 + 2
        else:
            pass
    else:
        pass

    #'I'm opted in to third party processing'
    if checkB13 == 1:
        if calc11 > 0:
            calc11 = calc11 + 1
        else:
            pass
    else:
        pass

    #'I didn't fully read ToS'
    if checkB14 == 1:
        if calc11 > 0:
            calc11 = calc11 + 1
        else:
            pass
    else:
        pass

    #take away 1 from scores if appropriate mitigations are indicated in risk values
    #see docs for explanation
    if checkB1 == 0:
        if calc2 > 0:
            calc2 = calc2 - 1
        else:
            pass
        if calc3 > 0:
            calc3 = calc3 - 1
        else:
            pass
    else:
        pass

    if checkB2 == 0:
        if calc1 > 0:
            calc1 = calc1 - 1
        else:
            pass
    else:
        pass

    if checkB3 == 0:
        if calc8 > 0:
            calc8 = calc8 - 1
        else:
            pass
        if calc15 > 0:
            calc15 = calc15 - 1
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 - 1
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 - 1
        else:
            pass
    else:
        pass

    if checkB4 == 0:
        if calc8 > 0:
            calc8 = calc8 - 1
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 - 1
        else:
            pass
        if calc9 > 0:
            calc9 = calc9 - 1
        else:
            pass
    else:
        pass

    if checkB5 == 0:
        if calc10 > 0:
            calc10 = calc10 - 1
        else:
            pass
        if calc12 > 0:
            calc12 = calc12 - 1
        else:
            pass
    else:
        pass

    if checkB6 == 0:
        if calc11 > 0:
            calc11 = calc11 - 1
        else:
            pass
    else:
        pass

    if checkB8 == 0:
        if calc15 > 0:
            calc15 = calc15 - 1
        else:
            pass
        if calc16 > 0:
            calc16 = calc16 - 1
        else:
            pass
    else:
        pass

    if checkB9 == 0:
        if calc13 > 0:
            calc13 = calc13 - 1
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 - 1
        else:
            pass
    else:
        pass

    if checkB10 == 0:
        if calc13 > 0:
            calc13 = calc13 - 1
        else:
            pass
        if calc14 > 0:
            calc14 = calc14 - 1
        else:
            pass
    else:
        pass

    if checkB12 == 0:
        if calc9 > 0:
            calc9 = calc9 - 1
        else:
            pass
    else:
        pass

    if checkB13 == 0:
        if calc11 > 0:
            calc11 = calc11 - 1
        else:
            pass
    else:
        pass


    #add lindunn scores
    #this is being done separately to the cvss score for ease of anyone reading the code
    #see docs for why these scores in particular are used
    if catVoice == 1:
        calc1 = calc1 + 5.5
        cacl4 = calc4 + 5.5
        calc7 = calc7 + 5.5
        calc10 = calc10 + 5.5
        cacl11 = calc11 + 5.5
        calc12 = calc12 + 5.5
    else:
        pass

    if catSign == 1:
        calc2 = calc2 + 8.5
        calc8 = calc8 + 8.5
    else:
        pass

    if catIntern == 1:
        calc3 = calc3 + 2
        calc6 = calc6 + 2
        calc7 = calc7 + 2
        calc9 = calc9 + 2
        calc13 = calc13 + 2
        calc14 = calc14 + 2
        calc15 = calc15 + 2
        calc16 = calc16 + 2
    else:
        pass

    if catExtern == 1:
        calc2 = calc2 + 5
        calc5 = calc5 + 5
        calc8 = calc8 + 5
        calc11 = calc11 + 5
        calc13 = calc13 + 5
        calc15 = calc15 + 5
    else:
        pass

    if catSecure == 1:
        calc3 = calc3 + 2
        calc6 = calc6 + 2
        calc7 = calc7 + 2
        calc9 = calc9 + 2
        calc14 = calc14 + 2
        calc16 = calc16 + 2
        app.pack_forget()
    else:
        app.pack_forget()

    #if we mitigated all avenues for private conversation leak, we can remove it
    if checkB6 == 0 and checkB13 == 0:
        calc11 = 0
    else:
        pass

    #Put all our results in a list so we can sort them
    global calcList2
    calcList2 = [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9,
                calc10, calc11, calc12, calc13, calc14, calc15, calc16]
    #Remove all null values
    while 0 in calcList2:
        calcList2.remove(0)   
    #Arrange list in descending order so biggest threats are first
    calcList2.sort(reverse=True)

    #Go to page 3
    page3()

#Displaying the results to the user
def page3():

    class Window3(Frame):

        def clickExitBtn3(self):
            exit()

        def clickGBtn2(self):
            top2 = Toplevel(root)
            top2.geometry("600x250")
            top2.title("Glossary")
            Label(top2, text="2-Factor-Authentication", font=('Geneva 12')).place(x=10, y=10)
            Label(top2, text="A form of security that requires 2 identification steps to log in, e.g. a password and a ",
                  font=('Geneva 10')).place(x=10, y=30)
            Label(top2, text="code sent to your phone.", font=('Geneva 10')).place(x=10, y=50)
            Label(top2, text="Administrator", font=('Geneva 12')).place(x=10, y=80)
            Label(top2, text="Someone with the highest privileges on the system. They can control many things.",
                  font=('Geneva 10')).place(x=10, y=100)
            Label(top2, text="Encryption", font=('Geneva 12')).place(x=10, y=130)
            Label(top2, text="Using a cipher to conceal the real 'plaintext' contents of some data.",
                  font=('Geneva 10')).place(x=10, y=150)
            Label(top2, text="Server", font=('Geneva 12')).place(x=10, y=180)
            Label(top2, text="An external entity that a device usually connects with via the Internet.",
                  font=('Geneva 10')).place(x=10, y=200)
            
        #further guidance tab
        def clickFurtherBtn(self):
            top = Toplevel(root)
            top.geometry("800x520")
            top.title("Further Guidance")
            #Some questions based on LINDUNN GO findings
            Label(top, text="More questions to ask yourself:",
                  font=('Geneva 15')).place(x=10, y=00)
            Label(top, text="How much sensitive data is stored on my device?").place(x=10,y=30)
            Label(top, text="Are my actions being used to build a profile on me, for example to target ads at me?").place(x=10,y=50)
            Label(top, text="Do interactions with other users affect the data that is linked to me personally?").place(x=10,y=70)
            Label(top, text="Is everyone using the device aware of the data collection rules and able to reasonably consent to them?").place(x=10,y=90)
            Label(top, text="Does usage behaviour reveal anything about my personal safety, for example what times I'm not home?").place(x=10,y=110)
            Label(top, text="How much do the manufacturers know about my personal life through my device usage, and am I ok with this?").place(x=10,y=130)
            Label(top, text="Are my usage patterns linkable to me personally, and am I okay with this?").place(x=10, y=150)
            Label(top, text="If others interact with my device, could they do things that might incriminate me?").place(x=10, y=170)
            Label(top, text="Could my device data be used to blackmail me?").place(x=10, y=190)
            Label(top, text="Do my device manufacturers have history of privacy violations or ulterior motives I'm not ok with?").place(x=10,y=210)
            Label(top, text="Do my devices have any known vulnerabilities that I could find by searching online?").place(x=10,y=230)
            Label(top, text="Do I really know where my personal data goes and everything it's used for?").place(x=10, y=250)
            Label(top, text="If you find yourself worried by the answers to any of the above, consider how", font = "Geneva 15").place(x=10,y=270)
            Label(top, text="much you use the device and if you feel safe/comfortable continuing to do so.", font = "Geneva 15").place(x=10,y=300)

            #showing the user where they can find more detailed info for their specific devices
            def callback(url):
                webbrowser.open_new(url)

            Label(top, text="For more individualised device information, consult manufacturer info:", font="Geneva 15").place(x=10, y=350)
            link1 = Label(top, text="Apple devices", fg="red", cursor="hand2", font="Geneva 10 underline")
            link1.place(x=10, y=380)
            link1.bind("<Button-1>", lambda e: callback("https://support.apple.com/manuals"))

            link2 = Label(top, text="Samsung devices", fg="red", cursor="hand2", font="Geneva 10 underline")
            link2.place(x=10, y=400)
            link2.bind("<Button-1>", lambda e: callback("https://www.samsung.com/us/support/downloads/"))

            link3 = Label(top, text="Google devices", fg="red", cursor="hand2", font="Geneva 10 underline")
            link3.place(x=10, y=420)
            link3.bind("<Button-1>", lambda e: callback("https://support.google.com/?hl=en"))

            link4 = Label(top, text="Amazon devices", fg="red", cursor="hand2", font="Geneva 10 underline")
            link4.place(x=10, y=440)
            link4.bind("<Button-1>", lambda e: callback("https://www.amazon.co.uk/gp/help/customer/display.html"))
            
            link5 = Label(top, text="See IoTLineup for links to many more home IoT devices.", fg="red", cursor="hand2", font="Geneva 10 underline")
            link5.place(x=10, y=460)
            link5.bind("<Button-1>", lambda e: callback("http://iotlineup.com/"))

            Label(top, text="The programmer of this app is not responsible for external content.", font = "Geneva 10").place(x=10, y=480)

                       

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master=master
            self.pack(fill=BOTH, expand=1)
        
            exitButton3 = Button(self, text="Quit", command=self.clickExitBtn3)
            exitButton3.place(x=70, y=50)

            furtherButton = Button(self, text="More advice", command=self.clickFurtherBtn)
            furtherButton.place(x=70, y=90)

            glossButton2 = Button(self, text="Glossary",command=self.clickGBtn2)
            glossButton2.place(x=70, y=130)

            hint1 = Label(self, text="Hint: Hover the mouse over ", font="Geneva 10")
            hint2 = Label(self, text="the box and use the mouse  ", font="Geneva 10")
            hint3 = Label(self, text="wheel to scroll up and down.", font="Geneva 10")
            hint1.place(x=655, y=10)
            hint2.place(x=655, y=30)
            hint3.place(x=655, y=50)

            text1 = Label(self, text="The threats are ordered from",font="Geneva 10",bg="#996Db6")
            text2 = Label(self, text="high to low, in terms of how", font="Geneva 10",bg="#996Db6")
            text3 = Label(self, text="serious the risk is in your",font="Geneva 10",bg="#996Db6")
            text4 = Label(self, text="specified case. However, you", font="Geneva 10",bg="#996Db6")
            text5 = Label(self, text="should take all threats", font="Geneva 10",bg="#996Db6")
            text6 = Label(self, text="seriously as bad people can", font="Geneva 10",bg="#996Db6")
            text7 = Label(self, text="exploit any of them. Try to", font="Geneva 10",bg="#996Db6")
            text8 = Label(self, text="mitigate as many as you can,", font="Geneva 10",bg="#996Db6")
            text9 = Label(self, text="as best as you can.", font="Geneva 10",bg="#996Db6")
            text1.place(x=655, y=100)
            text2.place(x=655, y=120)
            text3.place(x=655, y=140)
            text4.place(x=655, y=160)
            text5.place(x=655, y=180)
            text6.place(x=655, y=200)
            text7.place(x=655, y=220)
            text8.place(x=655, y=240)
            text9.place(x=655, y=260)

            #Convert calc values to str so we can display them in a list
            calcS1=str(calc1)
            calcS2=str(calc2)
            calcS3=str(calc3)
            calcS4=str(calc4)
            calcS5=str(calc5)
            calcS6=str(calc6)
            calcS7=str(calc7)
            calcS8=str(calc8)
            calcS9=str(calc9)
            calcS10=str(calc10)
            calcS11=str(calc11)
            calcS12=str(calc12)
            calcS13=str(calc13)
            calcS14=str(calc14)
            calcS15=str(calc15)
            calcS16=str(calc16)

            #Print results in the order we sorted them
            listbox = Listbox(self, width="53", height="100")

            for float in calcList2:
                if float is calc1:
                    listbox.insert(END,"OUTSIDER COMMANDS [Score: "+calcS1+"]")
                    listbox.insert(END,"Someone else might command your device to do something.")
                    listbox.insert(END,"For example, someone in the vicinity of a voice")
                    listbox.insert(END, "controlled device may say 'Add X to my shopping list.'")
                    listbox.insert(END,"LOWERING RISK: Turn on 2-factor-authentication if you")
                    listbox.insert(END,"can, or activate voice recognition if you have it.")
                    listbox.insert(END,"")
                elif float is calc2:
                    listbox.insert(END,"FAKE SERVER SIGNALS [Score: "+calcS2+"]")
                    listbox.insert(END,"If your device isn't sufficiently secure, an attacker")
                    listbox.insert(END,"can make a fake signal pretending to be your device")
                    listbox.insert(END,"and request anything from your device's server.")
                    listbox.insert(END,"LOWERING RISK: Check your device uses strong encryption")
                    listbox.insert(END,"and never connect to Wi-Fi you don't 100% trust.")
                    listbox.insert(END,"")
                elif float is calc3:
                    listbox.insert(END,"FAKE DEVICE SIGNALS [Score: "+calcS3+"]")
                    listbox.insert(END,"If your device isn't sufficiently secure, an attacker")
                    listbox.insert(END,"can make a fake signal pretending to be your device")
                    listbox.insert(END,"and request anything from other connected devices.")
                    listbox.insert(END,"LOWERING RISK: Check your device uses strong encryption")
                    listbox.insert(END,"and never connect to Wi-Fi you don't 100% trust.")
                    listbox.insert(END,"")
                elif float is calc4:
                    listbox.insert(END,"VOICE CAPTURE & MODIFICATION [Score: "+calcS4+"]")
                    listbox.insert(END,"An attacker could record your voice commands and then")
                    listbox.insert(END,"cut and paste pieces together to send to your device")
                    listbox.insert(END,"to make up an arbitrary command that sounds like you.")
                    listbox.insert(END,"LOWERING RISK: Set up your device to notify you of any")
                    listbox.insert(END,"potential attack attempts, if you can.")
                    listbox.insert(END,"")
                elif float is calc5:
                    listbox.insert(END,"SERVER SIGNAL MODIFICATION [Score: "+calcS5+"]")
                    listbox.insert(END,"If your device isn't designed securely, an attacker")
                    listbox.insert(END,"can copy the signals from the server, modify them, and")
                    listbox.insert(END,"send them to ask your device to do anything.")
                    listbox.insert(END,"LOWERING RISK: Set up your device to notify you of any")
                    listbox.insert(END,"potential attack attempts, if you can.")
                    listbox.insert(END,"")
                elif float is calc6:
                    listbox.insert(END,"DEVICE SIGNAL MODIFICATION [Score: "+calcS6+"]")
                    listbox.insert(END,"If your device isn't designed securely, an attacker")
                    listbox.insert(END,"can copy the signals your device sends to other devices")
                    listbox.insert(END,"and modify them to ask anything of those devices.")
                    listbox.insert(END,"LOWERING RISK: Set up your device to notify you of any")
                    listbox.insert(END,"potential attack attempts, if you can.")
                    listbox.insert(END,"")
                elif float is calc7:
                    listbox.insert(END,"ACTION CAPTURE [Score: "+calcS7+"]")
                    listbox.insert(END,"An action by a connected device can be captured and")
                    listbox.insert(END,"used when the attacker pleases, for example by telling")
                    listbox.insert(END,"a smart door lock to open itself.")
                    listbox.insert(END,"LOWERING RISK: Set up your device to notify you of any")
                    listbox.insert(END,"potential attack attempts, if you can.")
                    listbox.insert(END,"")
                elif float is calc8:
                    listbox.insert(END,"PERSONAL DATA LEAK [Score: "+calcS8+"]")
                    listbox.insert(END,"Personal details sent between your device and the server")
                    listbox.insert(END,"could be read by the attacker, and if they are not well")
                    listbox.insert(END,"encrypted, they can read all your personal details.")
                    listbox.insert(END,"LOWERING RISK: Check your device uses strong encryption")
                    listbox.insert(END,"and always choose strong passwords, never default ones.")
                    listbox.insert(END,"")
                elif float is calc9:
                    listbox.insert(END,"ACTION LEAK [Score: "+calcS9+"]")
                    listbox.insert(END,"The requests sent to connected devices can be read. For")
                    listbox.insert(END,"example, an attacker can read when you send requests to a")
                    listbox.insert(END,"smart lock to determine when you might not be home.")
                    listbox.insert(END,"LOWERING RISK: Check encryption is good, use good passwords,")
                    listbox.insert(END,"and turn on settings to create 'fake' traffic if included.")
                    listbox.insert(END,"")
                elif float is calc10:
                    listbox.insert(END,"EAVESDROPPERS [Score: "+calcS10+"]")
                    listbox.insert(END,"People who are nearby will be able to hear any requests")
                    listbox.insert(END,"you ask of your voice controlled devices, including any")
                    listbox.insert(END,"that are sensitive or contain personal details.")
                    listbox.insert(END,"LOWERING RISK: Don't install devices in places where sound")
                    listbox.insert(END,"leaks easily. Always consider who is in the vicinity.")
                    listbox.insert(END,"")
                elif float is calc11:
                    listbox.insert(END,"PRIVATE CONVERSATION LEAK [Score: "+calcS11+"]")
                    listbox.insert(END,"If you are opted-in to share with the manufacturer,")
                    listbox.insert(END,"employees can analyse private commands or accidentally-")
                    listbox.insert(END,"picked-up private conversations you have near the device.")
                    listbox.insert(END,"LOWERING RISK: Opt-out of any 'share my data with the")
                    listbox.insert(END,"manufacturer' settings.")
                    listbox.insert(END,"")
                elif float is calc12:
                    listbox.insert(END,"INTERFERING COMMANDS [Score: "+calcS12+"]")
                    listbox.insert(END,"Someone can give continuous voice commands to the device to")
                    listbox.insert(END,"prevent you from doing it, including by playing voice clips")
                    listbox.insert(END,"outside of your human range of hearing to avoid detection.")
                    listbox.insert(END,"LOWERING RISK: Don't put devices in areas with sound leaks.")
                    listbox.insert(END,"Watch out for ads or videos that might use your wake word.")
                    listbox.insert(END,"")
                elif float is calc13:
                    listbox.insert(END,"CONGESTING SERVER SIGNALS [Score: "+calcS13+"]")
                    listbox.insert(END,"An attacker could make a fake server signal and spam your")
                    listbox.insert(END,"device with it, so your device would not be able to handle")
                    listbox.insert(END,"any legitimate requests you have of it.")
                    listbox.insert(END,"LOWERING RISK: Only use trusted devices/apps. Turn on")
                    listbox.insert(END,"settings to notify you of attempted attacks, if possible.")
                    listbox.insert(END,"")
                elif float is calc14:
                    listbox.insert(END,"CONGESTING ACTION SIGNALS [Score: "+calcS14+"]")
                    listbox.insert(END,"An attacker could fake a signal from a connected device and")
                    listbox.insert(END,"spam your device with it, to prevent you from being able to")
                    listbox.insert(END,"make any legitimate requests of it.")
                    listbox.insert(END,"LOWERING RISK: Only use trusted devices/apps. Turn on")
                    listbox.insert(END,"settings to notify you of attempted attacks, if possible.")
                    listbox.insert(END,"")
                elif float is calc15:
                    listbox.insert(END,"COMPROMISED SERVER SIGNAL [Score: "+calcS15+"]")
                    listbox.insert(END,"If your device isn't sufficiently secure, a hacker can use")
                    listbox.insert(END,"some known weakness to gain access to your device, giving")
                    listbox.insert(END,"themselves total access to everything as an administrator.")
                    listbox.insert(END,"LOWERING RISK: Use strong passwords. Update to the latest")
                    listbox.insert(END,"security patch and enable threat notifications if you can.")
                    listbox.insert(END,"")
                elif float is calc16:
                    listbox.insert(END,"COMPROMISED ACTION SIGNAL [Score: "+calcS16+"]")
                    listbox.insert(END,"If connected devices aren't sufficiently secure, hackers")
                    listbox.insert(END,"can exploit known weaknesses to gain access and give")
                    listbox.insert(END,"themselves total access to everything as an administrator.")
                    listbox.insert(END,"LOWERING RISK: Use strong passwords. Update to the latest")
                    listbox.insert(END,"security patch and enable threat notifications if you can.")
                    listbox.insert(END,"")
                else:
                    print("error: unexpected value in list")
                    
            listbox.pack()
                    

    app=Window3(root)
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


