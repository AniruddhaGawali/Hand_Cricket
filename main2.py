import random,pickle,os,datetime
from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as tf
from PIL import Image,ImageTk
import tkinter.messagebox as msg 


player_run=5
comp_run=5
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
First_to=''



class Game_Func():

    def comp_score_board():
        comp_score['text']=f'{comp_Total_runs}/{comp_wicket}'
        balls_remain['text']=f'Balls : {comp_balls}'

    def player_score_board():
        score['text']=f'{Total_runs}/{player_wicket}'
        balls_remain['text']=f'Balls : {players_balls}'

    def comp_bat():
        comp_bat_choice[f"{comp_balls}"] = [player_run,comp_run]
    def player_bat():
        player_bat_choice[f"{players_balls}"] = [player_run,comp_run]


    def effect(file):
            import playsound
            playsound.playsound(file)

    def add_runs(run):
        global player_run
        global player_wicket,match_is_of
        global comp_run
        comp_run = random.choice((0,1,2,3,4,4,6,3,6))
        player_run = run
        
        if First_to.get()=='ba':
            Game_Func.comp_bat_match()
            match_is_of=1
        elif First_to.get()=='b':
            Game_Func.player_bat_match()
            match_is_of=2

    def comp_bat_match():
        global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs

        player_select_no['text']=f"{player_run}"
        comp_select_no['text']=f"{comp_run}"

        if comp_balls==0 or comp_wicket==Total_wicket:
            Game_Func.set_inning()
            comp_balls=0
            target = comp_Total_runs+1
            target_label['text']=f'Target : {target}'
            if comp_run == player_run:
                player_wicket +=1
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'Out'
                players_balls -= 1
                Game_Func.player_score_board()
            else:
                Total_runs+=player_run
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'Continue'
                players_balls -= 1
                Game_Func.player_score_board()
            Game_Func.player_bat()

        else:
            Game_Func.set_inning()

            if comp_run == player_run:
                comp_wicket +=1
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'Out'
                comp_balls -= 1
                Game_Func.comp_score_board()
                # effect(out)
                
            else:
                comp_Total_runs+=comp_run
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'Continue'
                comp_balls -= 1
                Game_Func.comp_score_board()
            Game_Func.comp_bat()
        Game_Func.comp_bat_match_result()


    def player_bat_match():
        global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs

        player_select_no['text']=f"{player_run}"
        comp_select_no['text']=f"{comp_run}"

        if players_balls==0 or player_wicket==Total_wicket:
            Game_Func.set_inning()
            players_balls=0
            target = Total_runs+1
            target_label['text']=f'Target : {target}'
            if comp_run == player_run:
                comp_wicket +=1
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'Out'
                comp_balls -= 1
                Game_Func.comp_score_board()
            else:
                comp_Total_runs+=comp_run
                comp_balls -= 1
                Game_Func.comp_score_board()
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'Continue'
            Game_Func.comp_bat()

        else:
            Game_Func.set_inning()
            if comp_run == player_run:
                player_wicket +=1
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'Out'
                players_balls -= 1
                Game_Func.player_score_board()
                
            else:
                Total_runs+=player_run
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'Continue'
                players_balls -= 1
                Game_Func.player_score_board()
            Game_Func.player_bat()
        Game_Func.player_bat_match_result()


    
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
                Game_Func.effect('data\sound\win.mp3')
            elif Total_runs==comp_Total_runs:
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'TIE'
                who_win = 't'
                Game_Func.effect("data\sound\loss.mp3")
            else:
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'YOU LOSS'
                who_win= 'c'
                Game_Func.effect("data\sound\loss.mp3")
        
        elif players_balls == 0 and Total_runs < comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
            concustion_label['text']= f'YOU LOSS'
            who_win = 'c'
            for i in range(0,7):
                if i==5:
                    continue
                else:
                    globals()['but%s'%i].config(state='disabled')
            Game_Func.effect("data\sound\loss.mp3")


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
                Game_Func.effect('data\sound\win.mp3')
                who_win = 'p'
            elif Total_runs==comp_Total_runs:
                conc_style.configure('conc.TLabel',background=bg_color,foreground='gray40')
                concustion_label['text']= f'TIE'
                who_win='t'
                Game_Func.effect("data\sound\loss.mp3")
            else:
                conc_style.configure('conc.TLabel',background=bg_color,foreground='red')
                concustion_label['text']= f'YOU LOSS'
                who_win='c'
                Game_Func.effect("data\sound\loss.mp3")
        
        elif comp_balls == 0 and Total_runs > comp_Total_runs:
            conc_style.configure('conc.TLabel',background=bg_color,foreground='green')
            concustion_label['text']= f'YOU WIN'
            who_win='p'
            for i in range(0,7):
                if i==5:
                    continue
                else:
                    globals()['but%s'%i].config(state='disabled')
            Game_Func.effect('data\sound\win.mp3')


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
                        file.write("-----------------------PLAYER WINS-----------------------")
                    elif who_win == 'c':
                        file.write("-----------------------COMP WINS------------------------")
                    elif who_win == 't':
                        file.write("----------------------MATCH TIE--------------------------")
                    
                    file.write(f'\nTotal Over : {Total_overs}\t\tTotal Balls : {Total_overs*6}\nTotal Wicket : {Total_wicket}\tTarget : {target}\n\n\n')
                    if match_is_of == 1:

                        file.write('First Inning\nBAT : comp , BALL : player\n')
                        file.write(f'Score : {comp_Total_runs}/{comp_wicket}\n\n')
                        for k,v in comp_bat_choice.items():
                            if v[0]==v[1]:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k} --- out\n')
                            else:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')

                        file.write('\n\nSecond Inning\nBAT : player , BALL : comp\n')
                        file.write(f'Score : {Total_runs}/{player_wicket}\n\n')
                        for k,v in player_bat_choice.items():
                            if v[0]==v[1]:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k} --- out\n')
                            else:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')
                    
                    

                    elif match_is_of == 2:

                        file.write('First Inning\nBAT : player , BALL : comp\n')
                        file.write(f'Score : {Total_runs}/{player_wicket}\n\n')
                        for k,v in player_bat_choice.items():
                            if v[0]==v[1]:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k} --- out\n')
                            else:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')

                        file.write('\n\nSecond Inning\nBAT : comp , BALL : player\n')
                        file.write(f'Score : {comp_Total_runs}/{comp_wicket}\n\n')
                        for k,v in comp_bat_choice.items():
                            if v[0]==v[1]:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k} --- out\n')
                            else:
                                file.write(f'player choics : {v[0]} , comp choics : {v[1]}  balls remain : {k}\n')
            else:
                msg.showwarning("Warn",'You have Not Select or Set the Game File\nSo Game file is Not Save')


    def set_inning():
        if First_to.get()== 'ba':
            if comp_balls==0 or comp_wicket==Total_wicket:
                who_ball['text']='Bowlling : Comp'
                who_bat['text']='Batting : You'
            else:
                who_bat['text']='Batting : Comp'
                who_ball['text']='Bowlling : You'
                
        elif First_to.get()=='b':
            if players_balls==0 or player_wicket==Total_wicket:
                who_ball['text']='Bowlling : You'
                who_bat['text']='Batting : Comp'
            else:
                who_ball['text']='Bowlling : Comp'
                who_bat['text']='Batting : You'
        else:
            pass



    



class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('300x525')
        self.maxsize(300,525)
        self.wm_iconbitmap("data/img/ico/icon.ico")
        self.title('Hand Cricket')


        # -------------------------
        if theme == 1 :
            self.light()
        elif theme == 2 : 
            self.dark()
        # -------------------------
        menubar = MenuBar(self)
        self.config(menu=menubar)
        # -------------------------
        self._frame = None
        self.switch_frame(Start_Page)
        # -------------------------



    def switch_frame(self, frame_class):
        global new_frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(anchor='center')

    def dark(self):    
        global bg_color,fg_color,label_bg_color,label_fg_color
        bg_color='gray10'
        fg_color='dodgerblue'
        label_bg_color = 'gray20'
        label_fg_color = 'dodgerblue'
        self.config(bg='gray10')

    def light(self):
        global bg_color,fg_color,label_bg_color,label_fg_color
        bg_color='white'
        fg_color='dodgerblue'
        label_bg_color = 'dodgerblue'
        label_fg_color = 'white'
        self.config(bg='white')

    @staticmethod
    def start():
        global theme
        if os.path.isfile('data/files/app_data.p'):
            f1 = open('data/files/app_data.p','rb')
            theme = pickle.load(f1)
        else:
            theme=1

    @staticmethod
    def overs(o,w):
        global players_balls, comp_balls
        if int(w) == 0 or int(o) == 0:
            pass
        else: 
            global Total_overs, Total_wicket
            Total_overs = int(o)
            Total_wicket = int(w) 
            players_balls=Total_overs*6
            comp_balls=Total_overs*6


    def coin_toss(self,select):
        global First_to
        First_to=StringVar()
        Game_Func.effect('data\sound\coinflip.mp3')
        self.overs(over.get(),wicket.get())
        coin_face = random.choice(('h','t'))
        if select== coin_face:
            self.switch_frame(Second_Page)

        else:
            First_to.set('ba')
            self.switch_frame(Third_Page)
            who_ball['text']='Bowlling : You'
            who_bat['text']='Batting : Comp'

    def newgame(self):
        global Total_runs,target,player_wicket,players_balls,comp_balls,comp_wicket,comp_Total_runs,Total_overs,Total_wicket,who_win
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
        self.switch_frame(Start_Page)
        
        who_win=''
        comp_bat_choice.clear()
        player_bat_choice.clear()



# ==============================================================================================================================================



class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        global theme

        def quitapp():
            parent.destroy()

        fileMenu = Menu(self, tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='dodgerblue')
        self.add_cascade(label="Menu",underline=0, menu=fileMenu)
        fileMenu.add_command(label="New Game", underline=1,command=lambda : parent.newgame())
        fileMenu.add_command(label='Save Game',command=Game_Func.save_game)
        fileMenu.add_command(label='Exit',command=quitapp)


        def temp_light():
            global theme
            theme=1
            parent.light()
            parent.switch_frame(fa)


            # new_frame.pack()
            # msg.showinfo("RESTART", 'Please relogin the Application')
        def temp_dark():
            global theme
            theme=2
            parent.dark()
            parent.switch_frame(fa)



        fileMenu2 = Menu(self, tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='dodgerblue')
        self.add_cascade(label="Settings",underline=0, menu=fileMenu2)
        sub_menu=Menu(fileMenu2,tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='dodgerblue')
        sub_menu.add_command(label='Light',underline=1,command= lambda :  temp_light())
        sub_menu.add_command(label='Dark',underline=1,command= lambda : temp_dark())
        fileMenu2.add_cascade(label="Theme",underline=0, menu=sub_menu)
        fileMenu2.add_command(label="About",underline=0,command= lambda : msg.showinfo('Info','This application is created by AKG\n              MADE IN INDIA'))




class Start_Page(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg=bg_color)

        global fa 
        fa=Start_Page


        root_frame1=Frame(self,bg=bg_color)
        root_frame1.pack(pady=(80,0))

        root_frame1_label_style=ttk.Style()
        root_frame1_label_style.configure('TLabel',background=bg_color,foreground=fg_color)
        over_select_label=ttk.Label(root_frame1,text='Select No. of Overs',font="Helvetica 15 bold",style='TLabel')
        over_select_label.config(anchor=CENTER)
        over_select_label.pack(padx=(0,0),pady=(0,0))

        global over,toss,wicket
        over=StringVar()
        wicket=StringVar()
        toss=StringVar()


        over.set('0')
        over_select= ttk.Spinbox(root_frame1,from_=1,to=50,font='Helvetica 15 bold',textvariable=over)
        over_select.pack(pady=8,padx=(0,0))

        wicket.set('0')
        player_select_label=ttk.Label(root_frame1,text='Select No. of Players',font="Helvetica 15 bold",style='TLabel')
        player_select_label.config(anchor=CENTER)
        player_select_label.pack(padx=(0,0))

        no_of_players=ttk.Spinbox(root_frame1,from_=1,to=50,font='Helvetica 15 bold',textvariable=wicket)
        no_of_players.pack(pady=8,padx=(0,0))

        style_checkbutton=ttk.Style()
        style_checkbutton.configure('TCheckbutton',width=10,hight=100,background=bg_color,foreground=fg_color,font='Helvetica 15 bold')

        toss_label=ttk.Label(root_frame1,text='Select the Face',font='Helvetica 15 bold',style='TLabel')
        toss_label.pack(pady=(0,0))

        head=ttk.Checkbutton(root_frame1,text='HEADS',variable=toss,onvalue='h',style='TCheckbutton')
        tails=ttk.Checkbutton(root_frame1,text='TAILS',variable=toss,onvalue='t',style='TCheckbutton')
        head.pack()
        tails.pack()
        over_selected=ttk.Button(root_frame1,text='Toss',command=lambda : master.coin_toss(toss.get()))
        over_selected.pack(pady=15,padx=(0,0))






class Second_Page(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg=bg_color)

        global fa 
        fa=Second_Page

        root_frame3=Frame(self,bg=bg_color)
        root_frame3.pack(pady=(160,0))

        def sf():
            if First_to.get()=='':
                pass
            else:
                master.switch_frame(Third_Page)
                if First_to.get() =='b':
                    who_ball['text']='Bowlling : Comp'
                    who_bat['text']='Batting : You'
                else:
                    who_ball['text']='Bowlling : You'
                    who_bat['text']='Batting : Comp'
        label1=Label(root_frame3,text='YOU WIN THE TOSS',background=bg_color,foreground=fg_color,font='Helvetica 15 bold')
        label1.pack(padx=(20,0))
        bat=ttk.Checkbutton(root_frame3,text='BAT',variable=First_to,onvalue='b',style='TCheckbutton')
        ball=ttk.Checkbutton(root_frame3,text='BALL',variable=First_to,onvalue='ba',style='TCheckbutton')
        bat.pack(pady=5,padx=(0,0))
        ball.pack(pady=5,padx=(0,0))
        buttton_of_match=ttk.Button(root_frame3,text="Start",command=sf)
        buttton_of_match.pack(pady=10)



class Third_Page(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg=bg_color)

        global fa 
        fa=Third_Page

        root_frame2=Frame(self,bg=bg_color)
        root_frame2.pack()

        global player_select_no,comp_select_no,conc_style,concustion_label,score,comp_score,over_count,balls_remain,target_label,who_bat,who_ball

        selected_no_frame=Frame(root_frame2,bg=bg_color)
        selected_no_frame.pack()

        root_frame1_label_style=ttk.Style()
        root_frame1_label_style.configure('TLabel',background=bg_color,foreground=fg_color)

        player_select_no_label=ttk.Label(selected_no_frame,text='   You Select  ',font="none 10 bold",style='TLabel')
        player_select_no_label.grid(row=0,column=0,padx=(0,15),pady=5)
        comp_select_no_label=ttk.Label(selected_no_frame,text='Comp Select',font="none 10 bold",style='TLabel')
        comp_select_no_label.grid(row=0,column=1,padx=(10,0),pady=5)

        player_select_no=ttk.Label(selected_no_frame,text=f'-',font='Helvetica 30 bold',style='TLabel')
        comp_select_no=ttk.Label(selected_no_frame,text=f'-',font='Helvetica 30 bold',style='TLabel')
        player_select_no.grid(row=1,column=0,padx=(0,10),pady=(5,2))
        comp_select_no.grid(row=1,column=1,padx=(5,0),pady=(5,2))

        conc_frame=Frame(root_frame2,bg=bg_color, relief=SUNKEN)
        conc_frame.pack()
        conc_style=ttk.Style()
        conc_style.configure('conc.TLabel',background=bg_color,foreground='white')
        concustion_label=ttk.Label(conc_frame,text='-',font='Helvetica 15 bold',style='conc.TLabel')
        concustion_label.pack(padx=(3,0),pady=(0,15))

        button_frame=Frame(root_frame2,bg=bg_color)
        button_frame.pack(pady=20)
        for i in range(0,7):
            if i==5:
                continue
            else:
                globals()['img%s'%i]= ImageTk.PhotoImage(Image.open(f"data/img/hand_numbers/img{i}.png"))


        global but0,but1,but2,but3,but4,but6

        but0=Button(button_frame,text=0,image=img0,borderwidth=2,command= lambda : Game_Func.add_runs(0) )
        but1=Button(button_frame,text=1,image=img1,borderwidth=2,command= lambda : Game_Func.add_runs(1) )
        but2=Button(button_frame,text=2,image=img2,borderwidth=2,command= lambda : Game_Func.add_runs(2) )
        but3=Button(button_frame,text=3,image=img3,borderwidth=2,command= lambda : Game_Func.add_runs(3) )
        but4=Button(button_frame,text=4,image=img4,borderwidth=2,command= lambda : Game_Func.add_runs(4) )
        but6=Button(button_frame,text=5,image=img6,borderwidth=2,command= lambda : Game_Func.add_runs(6) )

        but0.grid(row=0,column=0,padx=(0,10),pady=5)
        but1.grid(row=0,column=1,padx=(0,10),pady=5)
        but2.grid(row=0,column=2,padx=(0,0),pady=5)
        but3.grid(row=1,column=0,padx=(0,10),pady=5)
        but4.grid(row=1,column=1,padx=(0,10),pady=5)
        but6.grid(row=1,column=2,padx=(0,0),pady=5)



        scrore_frame=Frame(root_frame2,bg=bg_color)
        scrore_frame.pack(pady=10)

        score_name_label=ttk.Label(scrore_frame,text='Your Score : ',font='Helvetica 20 bold')
        score_name_label.grid(row=2,column=0,sticky=W,pady=(3,0),padx=(0,0))
        score=ttk.Label(scrore_frame,text=f'{Total_runs}/{player_wicket}',font='Helvetica 20 bold')
        score.grid(row=2,column=1,sticky=W,pady=(3,0))

        comp_score_name_label=ttk.Label(scrore_frame,text='Comp Score : ',font='Helvetica 20 bold')
        comp_score_name_label.grid(row=3,column=0,sticky=W,pady=(3,0),padx=(0,0))
        comp_score=ttk.Label(scrore_frame,text=f'{comp_Total_runs}/{comp_wicket}',font='Helvetica 20 bold')
        comp_score.grid(row=3,column=1,sticky=W,pady=(3,0))


        over_count=ttk.Label(scrore_frame,text=f'Over : {Total_overs}',font='Helvetica 13 bold')
        over_count.grid(row=4,column=0,sticky=W,padx=0)

        balls_remain=ttk.Label(scrore_frame,text=f'Balls : {players_balls}',font='Helvetica 13 bold')
        balls_remain.grid(row=4,column=1,sticky=W,padx=0)

        target_label=ttk.Label(scrore_frame,text=f'Target : -',font='Helvetica 13 bold')
        target_label.grid(row=5,column=0,sticky=W,padx=0)

        who_bat=ttk.Label(scrore_frame,text='Batting : -',font='Helvetica 10 ')
        who_ball=ttk.Label(scrore_frame,text='Bowling : -' ,font='Helvetica 10 ')
        who_bat.grid(row=6,column=0,sticky=W,padx=(2,0))
        who_ball.grid(row=7,column=0,sticky=W,padx=(2,0))
        Game_Func.set_inning()











    

SampleApp.start()
app = SampleApp()
app.mainloop()
f1= open('data/files/app_data.p','wb')
pickle.dump(theme,f1)
f1.close()