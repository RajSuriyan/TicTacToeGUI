from tkinter import *


#function block
global turn
global count
count=0
board={11:"11",12:"12",13:"13",
21:"21",22:"22",23:"23",
31:"31",32:"32",33:"33"}
list1=[11,12,13,21,22,23,31,32,33]

def btn(place,textx,rowx,columnx,functions=None,rel=None):
    button1 = Button(place, text=str(textx), font=('Helvetica', 40),relief=rel, command=functions)
    button1.grid(row=rowx, column=columnx)

def clicked(a,b):
    j=0
    global count
    if count%2==0:
        global turn
        turn= "X"
    else:
        turn="O"

    btn(root,turn,a,b,rel=SUNKEN)


    address=str(a)+str(b)
    board[int(address)] = turn
    if checkwin():

        label=Label(root,text=turn + " WINNER CONGRATULATIONS FROM DEVELOPER",font=('Helvetica','30'))
        label.grid(row=4,column=4)
        btn(root, turn, a, b, rel=SUNKEN)

    else:  # Check for draw
        j = j + 1
    if (j == 9):
        print("MATCH DRAW")
    count+=1



def checkwin():
    masterlist=[[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[13,22,31]]
    for i in masterlist:
        x=i[0]
        y=i[1]
        z=i[2]
        if(board[x]==board[y]==board[z]):
            return True





def printboard():


    btn(root, ' ', 1, 1, lambda e=1:clicked(1,1))
    btn(root, ' ', 1, 2, lambda e=1:clicked(1,2))
    btn(root, ' ', 1, 3, lambda e=1:clicked(1,3))

    btn(root, ' ', 2, 1, lambda e=1:clicked(2,1))
    btn(root, ' ', 2, 2, lambda e=1:clicked(2,2))
    btn(root, ' ', 2, 3, lambda e=1:clicked(2,3))

    btn(root, ' ', 3, 1, lambda e=1:clicked(3,1))
    btn(root, ' ', 3, 2, lambda e=1:clicked(3,2))
    btn(root, ' ', 3, 3, lambda e=1:clicked(3,3))







#root
root=Tk()
root.title('Tic Tac Toe')
root.geometry('400x400')


printboard()



















root.mainloop()