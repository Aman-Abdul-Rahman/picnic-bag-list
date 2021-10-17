# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:37:31 2021

@author: mx
"""

from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")
note=Label(root,text="Listed Items:['Tiffin','ID Card','Chocolate','Hanky','Chips','Tickets")
note.place(relx=0.5,rely=0.1,anchor=CENTER)
list1=["Bottle","Tiffin","ID Card","Chocolate","Hanky","Chips","Tickets"]
print(list1)
print(list1[1:4])
lucky_friend=Label(root)

def randomno():
    random_no=random.randint(0,5)
    lucky_friend["text"]="Put Item No:"+str(random_no)+" In Bag"
    
btn1=Button(root,text="Which item to put in bag?",command=randomno)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)
lucky_friend.place(relx=0.5,rely=4.,anchor=CENTER)
root.mainloop()