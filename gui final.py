import tkinter as tk
from tkinter import *
# Top level window
frame = tk.Tk()
frame.title("Block Chain")
frame.config(bg="light blue")
frame.geometry('600x300')

# Function for getting Input
# from textbox and printing it
# at label widget


def printInput():
    inp1 = inputtxt.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    inp3 = inputtxt3.get(1.0, "end-1c")
    if (inp1 == "3.2" and inp2 == "2.4"): 
        lbl4.config(bg = "light green",text = "BLock DETAILS "+ txt1)
        inputtxt.config(bg="light green")
        inputtxt2.config(bg="light green")
        inputtxt3.config(bg= "light green")


    elif (inp1 == "0" and inp2 == "0"): 
        lbl4.config(bg = "light green",text = "BLock DETAILS "+ txt2)
        inputtxt.config(bg="light green")
        inputtxt2.config(bg="light green")
        inputtxt3.config(bg= "light green")


    elif (inp1 == "56" and inp2 == "42"): 
        lbl4.config(bg = "light green",text = "BLock DETAILS "+ txt3)
        inputtxt.config(bg="light green")
        inputtxt2.config(bg="light green")
        inputtxt3.config(bg= "light green")


    elif (inp1 == "3.25" and inp2 == "2.42"): 
        lbl4.config(bg = "light green",text = "BLock DETAILS: "+ txt4)
        inputtxt.config(bg="light green")
        inputtxt2.config(bg="light green")
        inputtxt3.config(bg= "light green")
        
    else :  
        lbl4.config(text = "Error! Coordinates doesn't belong to any block")
        inputtxt.config(bg="red")
        inputtxt2.config(bg="red")
        inputtxt3.config(bg= "red")
        
	
	
# TextBox Creationpadx=200, pady=200
lbl = tk.Label(frame,bg="light green",text="Enter the coordinates of the 3d space:")
lbl.grid(row=0,column=0)


lbl1= tk.Label(frame, text_="X:     ")
lbl1.grid(row=1,column=4)
#lbl2.pack(padx=5 ,pady= 20)
inputtxt = tk.Text(frame,height = 1,width = 20)
inputtxt.grid(row=1,column=5,pady=5)
#inputtxt.pack(padx=5, pady=25)
lbl2= tk.Label(frame, text_="Y:      ")
lbl2.grid(row=2,column=4)
#lbl3.pack(padx=5 ,pady= 20)
inputtxt2 = tk.Text(frame,height = 1,width = 20)
inputtxt2.grid(row=2,column=5,pady=5)
#inputtxt2.pack(padx=5, pady=20)
lbl3= tk.Label(frame, text_="Z:      ")
lbl3.grid(row=3,column=4)
#lbl3.pack(padx=5 ,pady= 20)
inputtxt3 = tk.Text(frame,height = 1,width = 20)
inputtxt3.grid(row=3,column=5,pady=5)
#inputtxt3.pack(padx=5, pady=20)


# Button Creation
printButton = tk.Button(frame,bg="yellow",text = "Verify Block",command = printInput)
printButton.grid(row=4,column=5,pady=5)


# Label Creation
lbl4 = tk.Label(frame,bg ="light blue", text = "")
lbl4.grid(row=5,column=5)

#TODO
#shift to a characte based model?
#funcs. for rotor 4 and 5
#implement such that the order and selection of rotors is implemented
#combine all rotor functions into one with an integer argument to decide which
#rotor stepping according to historically accurate notch
#custom input of connections for plugboard function
#except default the other reflector lists
#function strings and comments
alphabetlist=['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor1list=['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']
rotor2list=['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']
rotor3list=['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']









































txt1 = '''
Index: 1
X: 3.2
y: 2.4
Z: 4.3
Timestamp: 1648488061
Hash: 1645223173
Previous Hash: 3408968250
Is Block Valid?: 1
'''

txt2 = '''
Index: 0
x: 0
y: 0
z: 0
Timestamp: 1650657703
Hash: 355950936
Previous Hash: 0
Is Block Valid?: 1'''


txt3 ='''
Index: 2
x: 56
y: 42
z: 45
Timestamp: 1650657703
Hash: 296455081
Previous Hash: 4119001667
Is Block Valid?: 0
Is chain still valid? 0
'''

'''Index: 0
x: 0
y: 0
z: 0
Timestamp: 1650657703
Hash: 355950936
Previous Hash: 0
Is Block Valid?: 1
'''

txt4 = '''
x: 3.25
y: 2.42
z: 43.3
Timestamp: 1650657703
Hash: 296455081
Previous Hash: 4119001667
Is Block Valid?: 1
Is chain still valid? 1
'''






#lbl.pack()
frame.mainloop()
