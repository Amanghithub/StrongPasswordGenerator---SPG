from tkinter import *
import random
root = Tk()

root.title("Strong Password Generator - SPG")
root.geometry("500x500")

passShow = Label(root)

array_3d = [[["0","1","2","3","4","5","6","7","8","9"],["!","@","#","$","^","&","%","*"],["A","B","C","D","E","F","G","H","I","J","K"]]]

def newpass():
    random1 = random.randint(0,9)
    random2 = random.randint(0,7)
    random3 = random.randint(0,10)
    
    letter1 = str(array_3d[0][0][random1])
    letter2 = str(array_3d[0][1][random2])
    letter3 = str(array_3d[0][2][random3])
    
    passShow["text"]=letter1+""+letter2+""+letter3
    
btn = Button(root,text="Get Password",command=newpass)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

passShow.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()