#Import necessary modules and libraries
from tkinter import *
import base64

#Initialize window
root = Tk()
root.geometry('510x360')
root.resizable(0,0)
root.iconbitmap('message_icon.ico')

#Title of the window
root.title("Message Encode Decode")

#Label for text in software
Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()

#Define variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

#Define functions for working of encoding, 
#Decoding,mode,password,result,exit and reset of software.

#Function to encode the message
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))    
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#Function to decode the message
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))   
    return "".join(dec)

#Function to set the mode of message
#i.e. Encode OR Decode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

#Function to exit window   
def Exit():
    root.destroy()

#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

#Name and Buttons

#Message Box
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 230,y=60)
Entry(root,width=60, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=45, y = 90)

#Key Box
Label(root, font = 'arial 12 bold', text ='KEY').place(x=250, y = 115)
Entry(root,width=60,font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=45,y=145)

#Mode Box
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=150, y = 170)
Entry(root,width=60,font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=45,y=200)

#Result Box
Entry(root,width=60,font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=45,y=230)

#Result Button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=230, y = 260)

#Reset Button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=160, y = 310)

#exit Button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=300, y = 310)

root.mainloop()