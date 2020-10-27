# ---------------------------------------------------------------ALL REQUIRD FILES-------------------------------------------------------------

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as tf
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import random,pickle,os,playsound,datetime



root = Tk()
style = ThemedStyle(root)
root.wm_iconbitmap("data/img/ico/icon.ico")
root.title('Hand Cricket')

if os.path.isfile('data/files/app_data.p'):
    f1 = open('data/files/app_data.p','rb')
    theme = pickle.load(f1)
else:
    theme=2


if theme ==2:
    bg_color='gray10'
    fg_color='dodgerblue'
    root.config(bg='gray10')
    label_bg_color = 'gray20'
    label_fg_color = 'dodgerblue'
elif theme ==1:
    bg_color='white'
    fg_color='dodgerblue'
    root.config(bg='white')
    label_bg_color = 'dodgerblue'
    label_fg_color = 'white'

style.set_theme("vista")
root.geometry('300x520')
root.maxsize(300,518)
 
# --------------------------------------------------------------------VARIBILES-----------------------------------------------------------------
# n=0
player_run=0
comp_run=0
Total_runs=0
comp_Total_runs=0
player_wicket=0
comp_wicket=0
players_balls=0
comp_balls=0
target=0
Total_overs = 0
Total_wicket =0
who_win = ''
player_bat_choice={}
comp_bat_choice={}




# -------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------
def raise_frame(frame):
    frame.tkraise()

def effect(file):
    playsound.playsound(file)

def comp_score_board():
    comp_score['text']=f'{comp_Total_runs}/{comp_wicket}'
    balls_remain['text']=f'Balls : {comp_balls}'
def player_score_board():
    score['text']=f'{Total_runs}/{player_wicket}'
    balls_remain['text']=f'Balls : {players_balls}'

def overs(o,w):
    global players_balls, comp_balls
    if int(w) == 0 or int(o) == 0:
        pass
    else: 
        global Total_overs, Total_wicket
        Total_overs = int(o)
        Total_wicket = int(w) 
        raise_frame(root_frame2)
        players_balls=Total_overs*6
        comp_balls=Total_overs*6
        balls_remain['text']=f'Balls : {players_balls}'
        over_count['text']=f'Total Overs : {Total_overs}'

def comp_bat():
    comp_bat_choice[f"{comp_balls}"] = [player_run,comp_run]
def player_bat():
    player_bat_choice[f"{players_balls}"] = [player_run,comp_run]




def player_bat_match_result():
    global who_win
    if players_balls==0 and comp_balls==0 or comp_wicket==Total_wicket:
        for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['but%s'%i].config(state='disabled')
        if Total_runs > comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='green')
            concustion_label['text']= f'YOU WIN'
            who_win = 'p'
            effect('data\sound\win.mp3')
        elif Total_runs==comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'TIE'
            who_win = 't'
            effect("data\sound\loss.mp3")
        else:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'YOU LOSS'
            who_win= 'c'
            effect("data\sound\loss.mp3")
    
    elif players_balls == 0 and Total_runs < comp_Total_runs:
        conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
        concustion_label['text']= f'YOU LOSS'
        who_win = 'c'
        for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['but%s'%i].config(state='disabled')
        effect("data\sound\loss.mp3")


def comp_bat_match_result():
    global who_win
    if players_balls==0 and comp_balls==0 or player_wicket==Total_wicket:
        for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['but%s'%i].config(state='disabled')
        if Total_runs > comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='green')
            concustion_label['text']= f'YOU WIN'
            effect('data\sound\win.mp3')
            who_win = 'p'
        elif Total_runs==comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'TIE'
            who_win='t'
            effect("data\sound\loss.mp3")
        else:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'YOU LOSS'
            who_win='c'
            effect("data\sound\loss.mp3")
    
    elif comp_balls == 0 and Total_runs > comp_Total_runs:
        conc_style.configure('conc.TLabel',background=bg_color,foreground='green')
        concustion_label['text']= f'YOU WIN'
        who_win='p'
        for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['but%s'%i].config(state='disabled')
        effect('data\sound\win.mp3')




def player_bat_match():
    global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs

    player_select_no['text']=f"{player_run}"
    comp_select_no['text']=f"{comp_run}"

    if players_balls==0 or player_wicket==Total_wicket:
        who_ball['text']='Bowlling : You'
        who_bat['text']='Batting : Comp'
        players_balls=0
        target = Total_runs+1
        target_label['text']=f'Target : {target}'
        if comp_run == player_run:
            comp_wicket +=1
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'Out'
            comp_balls -= 1
            comp_score_board()
        else:
            comp_Total_runs+=comp_run
            comp_balls -= 1
            comp_score_board()
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'Continue'
        comp_bat()

    else:
        who_ball['text']='Bowlling : Comp'
        who_bat['text']='Batting : You'
        if comp_run == player_run:
            player_wicket +=1
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'Out'
            players_balls -= 1
            player_score_board()
            
        else:
            Total_runs+=player_run
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'Continue'
            players_balls -= 1
            player_score_board()
        player_bat()
    player_bat_match_result()



def comp_bat_match():
    global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs

    player_select_no['text']=f"{player_run}"
    comp_select_no['text']=f"{comp_run}"

    if comp_balls==0 or comp_wicket==Total_wicket:
        who_ball['text']='Bowlling : Comp'
        who_bat['text']='Batting : You'
        comp_balls=0
        target = comp_Total_runs+1
        target_label['text']=f'Target : {target}'
        if comp_run == player_run:
            player_wicket +=1
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'Out'
            players_balls -= 1
            player_score_board()
        else:
            Total_runs+=player_run
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'Continue'
            players_balls -= 1
            player_score_board()
        player_bat()

    else:
        who_bat['text']='Batting : Comp'
        who_ball['text']='Bowlling : You'

        if comp_run == player_run:
            comp_wicket +=1
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'Out'
            comp_balls -= 1
            comp_score_board()
            # effect(out)
            
        else:
            comp_Total_runs+=comp_run
            conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
            concustion_label['text']= f'Continue'
            comp_balls -= 1
            comp_score_board()
        comp_bat()
    comp_bat_match_result()


def comp_select():
    global comp_run
    comp_run = random.choice((0,1,2,3,4,4,6,3,6))


def add_runs(run):
    global player_run
    global player_wicket,match_is_of
    player_run = run
    comp_select()
    if First_to.get()=='ba':
        comp_bat_match()
        match_is_of=1
    elif First_to.get()=='b':
        player_bat_match()
        match_is_of=2

def coin_toss(select):
    effect('data\sound\coinflip.mp3')
    overs(over.get(),wicket.get())
    coin_face = random.choice(('h','t'))
    if select== coin_face:
        raise_frame(root_frame3)
    else:
        raise_frame(root_frame2)
        First_to.set('ba')

def quitapp():
    root.destroy()

def newgame():
    global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs,Total_overs,Total_wicket
    global player_run
    global player_wicket
    player_run=0
    comp_run=0
    player_wicket=0
    comp_wicket=0
    Total_runs=0
    comp_Total_runs=0
    players_balls=0
    comp_balls=0
    target=0
    Total_overs = 0
    Total_wicket =0
    who_win=''
    for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['but%s'%i].config(state='normal')
    raise_frame(root_frame1)
    balls_remain['text']=f'Balls : {comp_balls}'
    comp_score['text']=f'{comp_Total_runs}/{comp_wicket}'
    conc_style.configure('conc.TLabel',background=bg_color,foreground='white')
    concustion_label['text']= f'-'
    player_select_no['text']=f"{player_run}"
    comp_select_no['text']=f"{comp_run}"
    score['text']=f'{Total_runs}/{player_wicket}'
    target_label['text']=f'Target : {target}'
    comp_bat_choice.clear()
    player_bat_choice.clear()


def save_game():
    if who_win == '':
        msg.showwarning("Warning", 'You have not Played a Game or\nYou have not Completed Your Game\nPlease do it First then only\nYou can save a Game File ')
    else:
        name = tf.asksaveasfilename(defaultextension=".txt",
                            filetypes=[("Text files",".txt"),
                                        ("Word files",".doc")],
                            initialdir="dir",
                            initialfile='game.txt',
                            title="Save as")
        
        if name != '':
            with open(name,'w') as file:
                file.write(f'{datetime.datetime.now().strftime("%B %d, %Y")}\n')
                file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")}\n\n')
                if who_win == 'p':
                    file.write("PLAYER WINS")
                elif who_win == 'c':
                    file.write("COMP WINS")
                elif who_win == 't':
                    file.write("MATCH TIE")
                
                file.write(f'\nTotal Over : {Total_overs}\t\tTotal Balls : {Total_overs*6}\nTotal Wicket : {Total_wicket}\tTarget : {target}\n\n\n')
                if match_is_of == 1:

                    file.write('First Inning\nBAT : comp , BALL : player\n')
                    file.write(f'Score : {comp_Total_runs}/{comp_wicket}\n\n')
                    for k,v in comp_bat_choice.items():
                        file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')

                    file.write('\n\nSecond Inning\nBAT : player , BALL : comp\n')
                    file.write(f'Score : {Total_runs}/{player_wicket}\n\n')
                    for k,v in player_bat_choice.items():
                        file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')
                
                

                elif match_is_of == 2:

                    file.write('First Inning\nBAT : player , BALL : comp\n')
                    file.write(f'Score : {Total_runs}/{player_wicket}\n\n')
                    for k,v in player_bat_choice.items():
                        file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')

                    file.write('\n\nSecond Inning\nBAT : comp , BALL : player\n')
                    file.write(f'Score : {comp_Total_runs}/{comp_wicket}\n\n')
                    for k,v in comp_bat_choice.items():
                        file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')
        else:
            msg.showwarning("Warn",'You have Not Select or Set the Game File\nSo Game file is Not Save')


# ------------------------------------------------------------FRAMES AND MAIN PROGRAM-----------------------------------------------------------


# ----------------------------------------------------------------------FRAME1------------------------------------------------------------------
    

root_frame1=Frame(root,bg=bg_color)
root_frame2=Frame(root,bg=bg_color)
root_frame3=Frame(root,bg=bg_color)
for frame in (root_frame1,root_frame2,root_frame3):
    frame.grid(row=0,column=0,sticky='news')

raise_frame(root_frame1)

root_frame1_label_style=ttk.Style()
root_frame1_label_style.configure('TLabel',background=bg_color,foreground=fg_color)
over_select_label=ttk.Label(root_frame1,text='Select No. of Overs',font="Helvetica 15 bold",style='TLabel')
over_select_label.config(anchor=CENTER)
over_select_label.pack(padx=(23,0),pady=(20,0))

over=StringVar()
over.set('0')
over_select= ttk.Spinbox(root_frame1,from_=1,to=50,font='Helvetica 15 bold',textvariable=over)
over_select.pack(pady=8,padx=(23,0))

wicket=StringVar()
wicket.set('0')
player_select_label=ttk.Label(root_frame1,text='Select No. of Players',font="Helvetica 15 bold",style='TLabel')
player_select_label.config(anchor=CENTER)
player_select_label.pack(padx=(23,0))

no_of_players=ttk.Spinbox(root_frame1,from_=1,to=50,font='Helvetica 15 bold',textvariable=wicket)
no_of_players.pack(pady=8,padx=(23,0))

style_checkbutton=ttk.Style()
style_checkbutton.configure('TCheckbutton',width=10,hight=100,background=bg_color,foreground=fg_color,font='Helvetica 15 bold')

toss_label=ttk.Label(root_frame1,text='Select the Face',font='Helvetica 15 bold',style='TLabel')
toss_label.pack(pady=(10,5))

toss=StringVar()
head=ttk.Checkbutton(root_frame1,text='HEADS',variable=toss,onvalue='h',style='TCheckbutton')
tails=ttk.Checkbutton(root_frame1,text='TAILS',variable=toss,onvalue='t',style='TCheckbutton')
head.pack()
tails.pack()
over_selected=ttk.Button(root_frame1,text='Toss',command=lambda : coin_toss(toss.get()))
over_selected.pack(pady=15,padx=(23,0))


# ----------------------------------------------------------------------FRAME3------------------------------------------------------------------


First_to=StringVar()
label1=Label(root_frame3,text='YOU WIN THE TOSS',background=bg_color,foreground=fg_color,font='Helvetica 15 bold')
label1.pack(padx=(20,0))
bat=ttk.Checkbutton(root_frame3,text='BAT',variable=First_to,onvalue='b',style='TCheckbutton')
ball=ttk.Checkbutton(root_frame3,text='BALL',variable=First_to,onvalue='ba',style='TCheckbutton')
bat.pack(pady=5,padx=(52,0))
ball.pack(pady=5,padx=(52,0))
buttton_of_match=ttk.Button(root_frame3,text="Start",command=lambda : raise_frame(root_frame2))
buttton_of_match.pack(pady=10)


# ----------------------------------------------------------------------FRAME2------------------------------------------------------------------


selected_no_frame=Frame(root_frame2,bg=bg_color)
selected_no_frame.pack()

player_select_no_label=ttk.Label(selected_no_frame,text='   You Select  ',font="none 10 bold",style='TLabel')
player_select_no_label.grid(row=0,column=0,padx=(15,5),pady=5)
comp_select_no_label=ttk.Label(selected_no_frame,text='Comp Select',font="none 10 bold",style='TLabel')
comp_select_no_label.grid(row=0,column=1,padx=(40,0),pady=5)

player_select_no=ttk.Label(selected_no_frame,text='-',font='Helvetica 30 bold',style='TLabel')
comp_select_no=ttk.Label(selected_no_frame,text='-',font='Helvetica 30 bold',style='TLabel')
player_select_no.grid(row=1,column=0,padx=(15,5),pady=(5,2))
comp_select_no.grid(row=1,column=1,padx=(40,0),pady=(5,2))

conc_frame=Frame(root_frame2,bg=bg_color, relief=SUNKEN)
conc_frame.pack()
conc_style=ttk.Style()
conc_style.configure('conc.TLabel',background=bg_color,foreground='white')
concustion_label=ttk.Label(conc_frame,text='-',font='Helvetica 15 bold',style='conc.TLabel')
concustion_label.pack(padx=(31,10),pady=(0,15))

button_frame=Frame(root_frame2,bg=bg_color)
button_frame.pack(pady=20)
for i in range(0,7):
    if i==5:
        continue
    else:
        globals()['img%s'%i]= ImageTk.PhotoImage(Image.open(f"data/img/hand_numbers/img{i}.png"))


but0=Button(button_frame,text=i,image=img0,borderwidth=2,command= lambda : add_runs(0) )
but1=Button(button_frame,text=i,image=img1,borderwidth=2,command= lambda : add_runs(1) )
but2=Button(button_frame,text=i,image=img2,borderwidth=2,command= lambda : add_runs(2) )
but3=Button(button_frame,text=i,image=img3,borderwidth=2,command= lambda : add_runs(3) )
but4=Button(button_frame,text=i,image=img4,borderwidth=2,command= lambda : add_runs(4) )
but6=Button(button_frame,text=i,image=img6,borderwidth=2,command= lambda : add_runs(6) )

but0.grid(row=0,column=0,padx=(25,6),pady=5)
but1.grid(row=0,column=1,padx=(4,0),pady=5)
but2.grid(row=0,column=2,padx=(10,0),pady=5)
but3.grid(row=1,column=0,padx=(25,6),pady=5)
but4.grid(row=1,column=1,padx=(4,0),pady=5)
but6.grid(row=1,column=2,padx=(10,0),pady=5)


scrore_frame=Frame(root_frame2,bg=bg_color)
scrore_frame.pack(pady=10)

score_name_label=ttk.Label(scrore_frame,text='Your Score : ',font='Helvetica 20 bold')
score_name_label.grid(row=2,column=0,sticky=W,pady=(3,0),padx=(8,0))
score=ttk.Label(scrore_frame,text=f'{Total_runs}/{player_wicket}',font='Helvetica 20 bold')
score.grid(row=2,column=1,sticky=W,pady=(3,0))

comp_score_name_label=ttk.Label(scrore_frame,text='Comp Score : ',font='Helvetica 20 bold')
comp_score_name_label.grid(row=3,column=0,sticky=W,pady=(3,0),padx=(8,0))
comp_score=ttk.Label(scrore_frame,text=f'{comp_Total_runs}/{comp_wicket}',font='Helvetica 20 bold')
comp_score.grid(row=3,column=1,sticky=W,pady=(3,0))


over_count=ttk.Label(scrore_frame,text='Over : 3',font='Helvetica 13 bold')
over_count.grid(row=4,column=0,sticky=W,padx=9)

balls_remain=ttk.Label(scrore_frame,text='Balls : 0',font='Helvetica 13 bold')
balls_remain.grid(row=4,column=1,sticky=W,padx=0)

target_label=ttk.Label(scrore_frame,text=f'Target : {target}',font='Helvetica 13 bold')
target_label.grid(row=5,column=0,sticky=W,padx=8)

who_bat=ttk.Label(scrore_frame,text='Batting : -',font='Helvetica 10 ')
who_ball=ttk.Label(scrore_frame,text='Bowling : -' ,font='Helvetica 10 ')
who_bat.grid(row=6,column=0,sticky=W,padx=(10,0))
who_ball.grid(row=7,column=0,sticky=W,padx=(10,0))




# --------------------------------------------------------------------MENU----------------------------------------------------------------------




mainmenu = Menu(root, activebackground=label_bg_color)
root.config(menu=mainmenu)
m1 = Menu(mainmenu, tearoff=0, bg=bg_color, fg=fg_color,activebackground=label_bg_color, activeforeground=label_fg_color)
m1.add_command(label='New Game',command=newgame)
m1.add_command(label='Save Game',command=save_game)
m1.add_separator()
m1.add_command(label='Exit',command=quitapp)
mainmenu.add_cascade(label='Menu', menu=m1)

def temp_light():
    global theme
    theme=1
    msg.showinfo("RESTART", 'Please Restart the application for apply the Theme')
def temp_dark():
    global theme
    theme=2
    msg.showinfo("RESTART", 'Please Restart the application for apply the Theme')

m2 = Menu(mainmenu, tearoff=0, bg=bg_color, fg=fg_color,activebackground=label_bg_color, activeforeground=label_fg_color)
m2_sub = Menu(m2,tearoff=0, bg=bg_color, fg=fg_color,activebackground=label_bg_color, activeforeground=label_fg_color)
m2_sub.add_command(label='Dark', command=temp_dark)
m2_sub.add_command(label='Light', command=temp_light)
m2.add_cascade(label='Theme',menu=m2_sub)
m2.add_command(label='Help', command=lambda: msg.showinfo('Help', 'We will help you soon'))
m2.add_command(label='More About', command=lambda: msg.showinfo('About', 'This GUI is created by AKG007\n            Made in India'))
mainmenu.add_cascade(label='Settings', menu=m2)

root.mainloop()






f1= open('data/files/app_data.p','wb')
pickle.dump(theme,f1)
f1.close()