from tkinter import messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(bg="cadet Blue")

Tops = Frame(root, bg="cadet Blue", pady=2, width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)

lbltitle=Label(Tops, bg="cadet Blue",font=('Times',30,'bold'),text='Tic Tac Toe Game',bd=20,fg='green',justify=CENTER)
lbltitle.grid(row=0,column=0)

MainFrame = Frame(root, bg="powder Blue", pady=2, width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame,bd=10, bg="powder Blue",width=750,height=500,pady=2,padx=10,relief=RIDGE)
LeftFrame.pack(side=LEFT)


RightFrame = Frame(MainFrame,bd=10, bg="powder Blue",width=560,height=500,pady=2,padx=10,relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame,bd=10, bg="powder Blue", width=560,height=200,pady=2,padx=10,relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame,bd=10, bg="powder Blue",width=560,height=200,pady=2,padx=10,relief=RIDGE)
RightFrame2.grid(row=1,column=0)

playerx=IntVar()
player0=IntVar()

playerx.set(0)
player0.set(0)

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] ==" " and click == False:
        buttons["text"] = "0"
        click = True
        scorekeeper()

def scorekeeper():
    if (button1['text']=="X" and button2['text']=="X" and button3['text']=="X"):
        button1.configure(bg="white")
        button2.configure(bg="white")
        button3.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button4['text']=="X" and button5['text']=="X" and button6['text']=="X"):
        button6.configure(bg="white")
        button5.configure(bg="white")
        button4.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button7['text']=="X" and button8['text']=="X" and button9['text']=="X"):
        button7.configure(bg="white")
        button8.configure(bg="white")
        button9.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button1['text']=="X" and button4['text']=="X" and button7['text']=="X"):
        button1.configure(bg="white")
        button4.configure(bg="white")
        button7.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button5['text']=="X" and button2['text']=="X" and button8['text']=="X"):
        button5.configure(bg="white")
        button2.configure(bg="white")
        button8.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button6['text']=="X" and button9['text']=="X" and button3['text']=="X"):
        button6.configure(bg="white")
        button9.configure(bg="white")
        button3.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    if (button1['text']=="X" and button5['text']=="X" and button9['text']=="X"):
        button1.configure(bg="white")
        button5.configure(bg="white")
        button9.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')
    if (button5['text']=="X" and button7['text']=="X" and button3['text']=="X"):
        button5.configure(bg="white")
        button7.configure(bg="white")
        button3.configure(bg="white")
        
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner X",'you have won the game')

    #=======================0 turn ================================

    if (button5['text']=="0" and button7['text']=="0" and button3['text']=="0"):
        button5.configure(bg="blue")
        button7.configure(bg="blue")
        button3.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button5['text']=="0" and button9['text']=="0" and button1['text']=="0"):
        button1.configure(bg="blue")
        button5.configure(bg="blue")
        button9.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button1['text']=="0" and button2['text']=="0" and button3['text']=="0"):
        button1.configure(bg="blue")
        button2.configure(bg="blue")
        button3.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button4['text']=="0" and button5['text']=="0" and button6['text']=="0"):
        button5.configure(bg="blue")
        button6.configure(bg="blue")
        button4.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button7['text']=="0" and button8['text']=="0" and button9['text']=="0"):
        button7.configure(bg="blue")
        button8.configure(bg="blue")
        button9.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button1['text']=="0" and button4['text']=="0" and button7['text']=="0"):
        button1.configure(bg="blue")
        button4.configure(bg="blue")
        button7.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')


    if (button2['text']=="0" and button8['text']=="0" and button5['text']=="0"):
        button2.configure(bg="blue")
        button8.configure(bg="blue")
        button5.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        player0.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')

    if (button3['text']=="0" and button6['text']=="0" and button9['text']=="0"):
        button3.configure(bg="blue")
        button6.configure(bg="blue")
        button9.configure(bg="blue")
        
        n=int(player0.get())
        score=n+1
        playerx.set(score)
        messagebox.showinfo("Winner 0",'you have won the game')





def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(bg="yellow")
    button2.configure(bg="yellow")
    button3.configure(bg="yellow")
    button4.configure(bg="yellow")
    button5.configure(bg="yellow")
    button6.configure(bg="yellow")
    button7.configure(bg="yellow")
    button8.configure(bg="yellow")
    button9.configure(bg="yellow")

    
def newgame():
    reset()
    playerx.set(0) 
    player0.set(0)

    

lblplayerx=Label(RightFrame1, bg="cadet Blue",font=('Times',30,'bold'),text='player x:',bd=20,fg='green',justify=CENTER)
lblplayerx.grid(row=0,column=0)
txtplayerx=Entry(RightFrame1, bg="cadet Blue",font=('Times',30,'bold'),textvariable=playerx,bd=20,fg='green',justify=CENTER)
txtplayerx.grid(row=0,column=1)

lblplayer0=Label(RightFrame1, bg="cadet Blue",font=('Times',30,'bold'),text='player 0:',bd=20,fg='green',justify=CENTER)
lblplayer0.grid(row=1,column=0)
txtplayer0=Entry(RightFrame1, bg="cadet Blue",font=('Times',30,'bold'),textvariable=player0,bd=20,fg='green',justify=CENTER)
txtplayer0.grid(row=1,column=1)

buttonclear=Button(RightFrame2,text="RESET",font=('airal 26 bold'),height=1,width=20,bg='cadet Blue',command=reset)
buttonclear.grid(row=0,column=0,sticky=S+N+E+W)
buttonnew=Button(RightFrame2,text="NEW GAME",font=('arial 26 bold'),height=1,width=20,bg='cadet Blue',command=newgame)
buttonnew.grid(row=1,column=0,sticky=S+N+E+W)



button1=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N)
button2=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='yellow',command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

root.mainloop()
