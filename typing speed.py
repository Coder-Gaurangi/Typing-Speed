words = ['table', 'ink','brochure','dance','apparatus','khaki','situation','situ','south','softener','journey','impeccable','revert','jug','mercy','jabong','fishy','messy','ty']

def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timeLableCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLableCount.configure(text=timeleft)
        timeLableCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLableCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLableCount.configure(text=score)


def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLableCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

import random
from tkinter import messagebox
from tkinter import *
####################################################################  Root Method
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='pink')
root.title('Typing Speed Game')

###################################################################### Variables
score = 0
timeleft = 60
count = 0
miss = 0
######################################################################  Label Methods
fontLabel = Label(root,text='WELCOME',font=('airal',25,'italic bold'),
                  bg='pink',fg='dark green',width=40)
fontLabel.place(x=10,y=10)

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='pink')
wordLabel.place(x=350,y=200)

scoreLable = Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='pink')
scoreLable.place(x=10,y=100)

scoreLableCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='pink',fg='blue')
scoreLableCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left :',font=('airal',25,'italic bold'),bg='pink')
timerLabel.place(x=600,y=100)

timeLableCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='pink',fg='blue')
timeLableCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),
                            bg='pink',fg='navy blue')
gamePlayDetailLabel.place(x=120,y=450)
######################################################################  Entry Method
wordEntry = Entry(root,font=('airal',25,'italic bold'),bd=15,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
###################################################################
root.bind('<Return>',startGame)
root.mainloop()