"""Игра 'crosses and zeroes'."""

from tkinter import *
from random import *
from tkinter import messagebox as mb
import time

window = Tk()
window.title('crosses and zeroes')
game = True
square = []
cross_count = 0
youwin_list = []
comwin_list = []
youwin = False
comwin = False
SIZE = 3
HALF = 5


def message():
    if youwin:
        mb.showinfo(f"{len(youwin_list)} : {len(comwin_list)}")
    elif comwin:
        mb.showinfo(f"{len(youwin_list)} : {len(comwin_list)}")
    new_game()
    

def new_game():
    for x in range(SIZE):
        for y in range(SIZE):
            square[x][y]['text'] = ' '
            square[x][y]['background'] = 'orange'
    global game
    game = True
    global cross_count
    cross_count = 0
    
    
 def press(x, y):
    if game and square[x][y]['text'] == ' ':
        square[x][y]['text'] = 'X'
        global cross_count
        cross_count += 1
        win_check()
        if game and cross_count < SIZE ** 2 % 2 + SIZE ** 2 // 2: 
            computer()
            win_check()


def win_check():
    for i in range(SIZE):
        for j in range(SIZE):
            try:
                line_check(square[i][j],
                           square[i][j + 1],
                           square[i][j + 2])
                           
                line_check(square[j][i],
                           square[j + 1][i],
                           square[j + 2][i])
                           
                line_check(square[i][j],
                           square[i - 1][j + 1],
                           square[i - 2][j + 2])
                           
                line_check(square[i][j],
                           square[i + 1][j + 1],
                           square[i + 2][j + 2])
                           
            except IndexError:
                continue


def line_check(a, b, c):
    if a['text'] == b['text'] == c['text']!= ' ':
        green(a, b, c)
   

def computer():
    while True:
        window.update()
        time.sleep(0.01)
        x = randint(0, SIZE - 1)
        y = randint(0, SIZE - 1)
        if square[x][y]['text'] == ' ':
            square[x][y]['text'] = 'O'
            break


def green(a, b, c):
    a['background'] = b['background'] = c['background'] = 'green'
    global comwin
    global youwin_list
    global comwin_list
    global youwin
    if a['text'] == b['text'] == c['text']== 'X':
        youwin = True
        youwin_list.append(youwin)
    if a['text'] == b['text'] == c['text']== 'O':
        comwin = True
        comwin_list.append(comwin)
    global game
    game = False


def close_window():
    window.destroy()


def start():
    for row in range(SIZE):
        line = []
        for col in range(SIZE):
            button = Button(window, text=' ', width=3, height=1,
                            font=('Verdana', 20, 'bold'),
                            background='orange',
                            command=lambda row=row, col=col: press(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        square.append(line)
    start_button = Button(window, text='начать', command=message)
    start_button.grid(row=SIZE, column=0, columnspan=HALF, sticky='nsew')
    quit_button = Button(window, text='выйти', command=close_window)
    quit_button.grid(row=SIZE, column=3, columnspan=SIZE, sticky='nsew')
    window.update()
    window.mainloop()
    
    

    

start()


    



