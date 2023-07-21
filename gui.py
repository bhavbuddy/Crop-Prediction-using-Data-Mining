from tkinter import *
import tkinter.messagebox as mb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.metrics import zero_one_loss as accuracy_score
from sklearn.metrics import confusion_matrix
from pyswarm import pso
from parameters import parametres
import matplotlib.pyplot as plt
root = Tk()
# Set size of the form
root.geometry("500x500")
#Providing title to the form
root.title('crop prediction')
#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="crop prediction", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)
#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="Temperature", width=20,font=("bold",10))
label_1.place(x=80,y=130)
#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.pack()
entry_1.place(x=240,y=130)
label_3 =Label(root,text="Humidity", width=20,font=("bold",10))
label_3.place(x=68,y=180)
entry_3=Entry(root)
entry_3.pack()
entry_3.place(x=240,y=180)
label_4 =Label(root,text="PH", width=20,font=("bold",10))
label_4.place(x=68,y=220)
entry_4=Entry(root)
entry_4.pack()
entry_4.place(x=240,y=220)
label_5=Label(root,text="Rainfall", width=20,font=("bold",10))
label_5.place(x=58,y=270)
entry_5=Entry(root)
entry_5.pack()
entry_5.place(x=240,y=270)
    v1 = entry_1.get()
    v2 = entry_3.get()
    v3 = entry_4.get()
    v4 = entry_5.get()
    a = v1.strip()
    b = v2.strip()
    c = v3.strip()
    d = v4.strip()
    if v1 == '':
        v11 = 0.000
    else:
        a = ''.join(c for c in a if c.isdigit() or c == '.')
   v11 = float(a)
    if v2 =='':
        v12 = 0.000
    else:
        b = ''.join(c for c in b if c.isdigit() or c == '.')
        v12 = float(b)
    if v3 == '':
        v13 = 0.000
    else:
        c = ''.join(c for c in c if c.isdigit() or c == '.')
        v13 = float(c)
    if v4 == '':
        v14 = 0.0000
    else:
        d = ''.join(c for c in d if c.isdigit() or c == '.')
        v14 = float(d)
    mb.showinfo('Result', f'Temperature: {v11}, Humidity: {v12}, PH: {v13}, Rainfall: {v14}')
Button(root,text='Submit',width=15,bg="pink",command=open_popup).place(x=200
,y=300)
root.mainloop()
