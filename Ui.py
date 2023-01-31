from tkinter import *

"""pick which screen to display"""
def display_screen(screen):
    screen.tkraise()

root = Tk()
# to make program window start out maximized
root.state('zoomed')
# make each screen fill up the whole window
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# creating each screen in the project, uses Frame() built in function
screen_1 = Frame(root)
screen_2 = Frame(root)
screen_beginner = Frame(root)
screen_intermediate = Frame(root)
screen_advanced = Frame(root)
screen_role = Frame(root)
screen_role_2 = Frame(root)
screen_role_3 = Frame(root)
#-----------------------------------------------------------------------------
screen_begin_top = Frame(root)
screen_interm_top = Frame(root)
screen_adv_top = Frame(root)

screen_begin_top_pass = Frame(root)
screen_begin_top_aggre = Frame(root)
screen_begin_top_between = Frame(root)

screen_interm_top_pass = Frame(root)
screen_interm_top_aggre = Frame(root)
screen_interm_top_between = Frame(root)

screen_adv_top_pass = Frame(root)
screen_adv_top_aggre = Frame(root)
screen_adv_top_between = Frame(root)
#------------------------------------------------------------------------------
screen_begin_mid = Frame(root)
screen_interm_mid = Frame(root)
screen_adv_mid = Frame(root)

screen_begin_mid_pass = Frame(root)
screen_begin_mid_aggre = Frame(root)
screen_begin_mid_between = Frame(root)

screen_interm_mid_pass = Frame(root)
screen_interm_mid_aggre = Frame(root)
screen_interm_mid_between = Frame(root)

screen_adv_mid_pass = Frame(root)
screen_adv_mid_aggre = Frame(root)
screen_adv_mid_between = Frame(root)
#------------------------------------------------------------------------------
screen_begin_jungle = Frame(root)
screen_interm_jungle = Frame(root)
screen_adv_jungle = Frame(root)

screen_begin_jungle_pass = Frame(root)
screen_begin_jungle_aggre = Frame(root)
screen_begin_jungle_between = Frame(root)

screen_interm_jungle_pass = Frame(root)
screen_interm_jungle_aggre = Frame(root)
screen_interm_jungle_between = Frame(root)

screen_adv_jungle_pass = Frame(root)
screen_adv_jungle_aggre = Frame(root)
screen_adv_jungle_between = Frame(root)

#------------------------------------------------------------------------------
screen_begin_marksman = Frame(root)
screen_interm_marksman = Frame(root)
screen_adv_marksman = Frame(root)

screen_begin_marksman_pass = Frame(root)
screen_begin_marksman_aggre = Frame(root)
screen_begin_marksman_between = Frame(root)

screen_interm_marksman_pass = Frame(root)
screen_interm_marksman_aggre = Frame(root)
screen_interm_marksman_between = Frame(root)

screen_adv_marksman_pass = Frame(root)
screen_adv_marksman_aggre = Frame(root)
screen_adv_marksman_between = Frame(root)

#------------------------------------------------------------------------------
screen_begin_support = Frame(root)
screen_interm_support = Frame(root)
screen_adv_support = Frame(root)

screen_begin_support_pass = Frame(root)
screen_begin_support_aggre = Frame(root)
screen_begin_support_between = Frame(root)

screen_interm_support_pass = Frame(root)
screen_interm_support_aggre = Frame(root)
screen_interm_support_between = Frame(root)

screen_adv_support_pass = Frame(root)
screen_adv_support_aggre = Frame(root)
screen_adv_support_between = Frame(root)




# list for all the screens
screen_list = [screen_1, screen_2, screen_beginner, screen_intermediate, screen_advanced,
               screen_role, screen_role_2, screen_role_3,

               screen_begin_top, screen_interm_top, screen_adv_top,
               screen_begin_top_pass, screen_begin_top_aggre, screen_begin_top_between,
               screen_interm_top_pass, screen_interm_top_aggre, screen_interm_top_between,
               screen_adv_top_pass, screen_adv_top_aggre, screen_adv_top_between,

               screen_begin_mid, screen_interm_mid, screen_adv_mid,
               screen_begin_mid_pass, screen_begin_mid_aggre, screen_begin_mid_between,
               screen_interm_mid_pass, screen_interm_mid_aggre, screen_interm_mid_between,
               screen_adv_mid_pass, screen_adv_mid_aggre, screen_adv_mid_between,

               screen_begin_jungle, screen_interm_jungle, screen_adv_jungle,
               screen_begin_jungle_pass, screen_begin_jungle_aggre, screen_begin_jungle_between,
               screen_interm_jungle_pass, screen_interm_jungle_aggre, screen_interm_jungle_between,
               screen_adv_jungle_pass, screen_adv_jungle_aggre, screen_adv_jungle_between,

               screen_begin_marksman, screen_interm_marksman, screen_adv_marksman,
               screen_begin_marksman_pass, screen_begin_marksman_aggre, screen_begin_marksman_between,
               screen_interm_marksman_pass, screen_interm_marksman_aggre, screen_interm_marksman_between,
               screen_adv_marksman_pass, screen_adv_marksman_aggre, screen_adv_marksman_between,

               screen_begin_support, screen_interm_support, screen_adv_support,
               screen_begin_support_pass, screen_begin_support_aggre, screen_begin_support_between,
               screen_interm_support_pass, screen_interm_support_aggre, screen_interm_support_between,
               screen_adv_support_pass, screen_adv_support_aggre, screen_adv_support_between,
               ]
for frame in (screen_list):
    frame.grid(row=0, column=0, sticky='nsew')


#==============================================================screen_1 code
screen_1_title = Label(screen_1, text='Welcome to the League of Legends Champion Selector!',
                       font='times 35', bg='bisque')
screen_1_title.pack(fill='x')

screen_1_button = Button(screen_1, text='Click Here To Get Started!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_2))
screen_1_button.pack()


#===============================================================screen_2 code
screen_2_title = Label(screen_2, text='How familiar are you with League of Legends?',
                       font='times 35', bg='bisque')
screen_2_title.pack()

screen_2_button_1 = Button(screen_2, text='Beginner', font='times 15', padx=10, pady=10,
                         command=lambda: display_screen(screen_role))
screen_2_button_1.pack()

screen_2_button_2 = Button(screen_2, text="Intermediate", font='times 15', padx=10, pady=10,
                         command=lambda: display_screen(screen_role_2))
screen_2_button_2.pack()

screen_2_button_3 = Button(screen_2, text="Advanced", font='times 15', padx=10, pady=10,
                         command=lambda: display_screen(screen_role_3))
screen_2_button_3.pack()

screen_2_button_4 = Button(screen_2, text="Back to Welcome Page", font='times 15', padx=10, pady=10, bg= 'red',
                         command=lambda: display_screen(screen_1))
screen_2_button_4.pack()


#==============================================================screen_role code
screen_role_title = Label(screen_role, text='What role do you want to play?',
                       font='times 30', bg='bisque')
screen_role_title.pack()
screen_role_info = Label(screen_role, text="For a beginner we recommend top or mid",
                       font='times 18', bg='yellow')
screen_role_info.pack()

screen_role_button = Button(screen_role, text='Top', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_top))
screen_role_button.pack()

screen_role_button = Button(screen_role, text='Mid', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_mid))
screen_role_button.pack()

screen_role_button = Button(screen_role, text='Jungle', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_jungle))
screen_role_button.pack()

screen_role_button = Button(screen_role, text='Marksman', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_marksman))
screen_role_button.pack()

screen_role_button = Button(screen_role, text='Support', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_support))
screen_role_button.pack()

screen_role_button = Button(screen_role, text='Back to Skill Level', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_2))
screen_role_button.pack()


#==============================================================screen_role_2 code
screen_role_2_title = Label(screen_role_2, text='What role do you want to play?',
                       font='times 30', bg='bisque')
screen_role_2_title.pack()

screen_role_2_title = Label(screen_role_2, text='As an intermediate player you have more options and can '
                                                'generally choose any role',
                       font='times 20', bg='yellow')
screen_role_2_title.pack()

screen_role_2_button = Button(screen_role_2, text='Top', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_interm_top))
screen_role_2_button.pack()

screen_role_2_button = Button(screen_role_2, text='Mid', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_interm_mid))
screen_role_2_button.pack()

screen_role_2_button = Button(screen_role_2, text='Jungle', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_interm_jungle))
screen_role_2_button.pack()

screen_role_2_button = Button(screen_role_2, text='Marksman', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_interm_marksman))
screen_role_2_button.pack()

screen_role_2_button = Button(screen_role_2, text='Support', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_interm_support))
screen_role_2_button.pack()

screen_role_2_button = Button(screen_role_2, text='Back to Skill Level', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_2))
screen_role_2_button.pack()


#==============================================================screen_role_3 code
screen_role_3_title = Label(screen_role_3, text='What role do you want to play?',
                       font='times 30', bg='bisque')
screen_role_3_title.pack()

screen_role_3_title = Label(screen_role_3, text='Advanced',
                       font='times 20', bg='yellow')
screen_role_3_title.pack()

screen_role_3_button = Button(screen_role_3, text='Top', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_adv_top))
screen_role_3_button.pack()

screen_role_3_button = Button(screen_role_3, text='Mid', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_adv_mid))
screen_role_3_button.pack()

screen_role_3_button = Button(screen_role_3, text='Jungle', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_adv_jungle))
screen_role_3_button.pack()

screen_role_3_button = Button(screen_role_3, text='Marksman', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_adv_marksman))
screen_role_3_button.pack()

screen_role_3_button = Button(screen_role_3, text='Support', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_adv_support))
screen_role_3_button.pack()

screen_role_3_button = Button(screen_role_3, text='Back to Skill Level', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_2))
screen_role_3_button.pack()





#==============================================================screen_begin_top code
screen_begin_top_title = Label(screen_begin_top, text="What's your play-style?",
                       font='times 30', bg='bisque')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_top, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_top_aggre))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_top, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_top, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_top_pass))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_top, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_top, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_top_between))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_top, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_top, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_begin_mid code
screen_begin_top_title = Label(screen_begin_mid, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_mid, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_mid_aggre))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_mid, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_mid, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_mid_pass))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_mid, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_mid, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_mid_between))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_mid, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_mid, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_begin_jungle code
screen_begin_top_title = Label(screen_begin_jungle, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_jungle, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_jungle_aggre))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_jungle, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_jungle, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_jungle_pass))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_jungle, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_jungle, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_jungle_between))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_jungle, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_jungle, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_begin_marksman code
screen_begin_top_title = Label(screen_begin_marksman, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_marksman, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_marksman_pass))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_marksman, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_marksman, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_marksman_aggre))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_marksman, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_marksman, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_marksman_between))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_marksman, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_marksman, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_begin_support code
screen_begin_top_title = Label(screen_begin_support, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_support, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_support_aggre))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_support, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_support, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_support_pass))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_support, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_support, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_begin_support_between))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_begin_support, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_begin_support, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_interm_top code
screen_begin_top_title = Label(screen_interm_top, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_top, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_top, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_top, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_top, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_top, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_top, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_top, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_interm_mid code
screen_begin_top_title = Label(screen_interm_mid, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_mid, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_mid, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_mid, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_mid, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_mid, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_mid, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_mid, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_interm_jungle code
screen_begin_top_title = Label(screen_interm_jungle, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_jungle, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_jungle, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_jungle, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_jungle, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_jungle, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_jungle, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_jungle, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_interm_marksman code
screen_begin_top_title = Label(screen_interm_marksman, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_marksman, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_marksman, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_marksman, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_marksman, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_marksman, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_marksman, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_marksman, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_interm_support code
screen_begin_top_title = Label(screen_interm_support, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_support, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_support, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_support, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_support, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_support, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_interm_support, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_interm_support, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_adv_top code
screen_begin_top_title = Label(screen_adv_top, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_top, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_top, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_top, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_top, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_top, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_top, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_top, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_adv_mid code
screen_begin_top_title = Label(screen_adv_mid, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_mid, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_mid, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_mid, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_mid, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_mid, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_mid, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_mid, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_adv_jungle code
screen_begin_top_title = Label(screen_adv_jungle, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_jungle, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_jungle, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_jungle, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_jungle, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_jungle, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_jungle, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_jungle, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_adv_marksman code
screen_begin_top_title = Label(screen_adv_marksman, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_marksman, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_marksman, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_marksman, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_marksman, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_marksman, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_marksman, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_marksman, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_adv_support code
screen_begin_top_title = Label(screen_adv_support, text="What's your play-style?",
                       font='times 30', bg='white')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_support, text='Aggressive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_support, text="(Going in early, trying to get kills to extend your lead)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_support, text='Passive', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_support, text="(Play safe early, look to scale and get stronger later)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_support, text='Somewhere Inbetween', font='times 15', padx=5, pady=5,
                         command=lambda: display_screen(screen_1))
screen_begin_top_1.pack()

screen_begin_top_title = Label(screen_adv_support, text="(Play aggressive if you can find an opportunity, if not "
                                                      "then farm and scale up)",
                       font='times 12')
screen_begin_top_title.pack(fill='x')

screen_begin_top_1 = Button(screen_adv_support, text='Back to Role Selection', font='times 15', padx=10, pady=10, bg='red',
                         command=lambda: display_screen(screen_role))
screen_begin_top_1.pack()


#==============================================================screen_begin_top_pass
screen_intermediate_title = Label(screen_begin_top_pass, text="Your Recommended Champions are: Sion, Malphite, Cho'Gath ",
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_top_pass, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_top_aggre
screen_advanced_title = Label(screen_begin_top_aggre, text='Your Recommended Champions are: Garen, Darius , Wukong',
                       font='times 30', bg='white')
screen_advanced_title.pack(fill='x')

screen_advanced_button = Button(screen_begin_top_aggre, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_advanced_button.pack()


#==============================================================screen_begin_top_between
screen_intermediate_title = Label(screen_begin_top_between, text='Your Recommended Champions are: Volibear, Urgot, Mordekaiser ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_top_between, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()


#==============================================================screen_begin_mid_pass
screen_intermediate_title = Label(screen_begin_mid_pass, text='Your Recommended Champions are: Annie, Malzahar, Ziggs ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_mid_pass, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_mid_aggre
screen_intermediate_title = Label(screen_begin_mid_aggre, text='Your Recommended Champions are: Annie, Ahri, Fizz ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_mid_aggre, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_mid_between
screen_intermediate_title = Label(screen_begin_mid_between, text='Your Recommended Champions are: Annie, Neeko, Swain ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_mid_between, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()


#==============================================================screen_begin_jungle_pass
screen_intermediate_title = Label(screen_begin_jungle_pass, text='Your Recommended Champions are: Amumu, Shyvanna, Nocturne ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_jungle_pass, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_jungle_aggre
screen_intermediate_title = Label(screen_begin_jungle_aggre, text='Your Recommended Champions are: Xin Zhao, Volibear, Jarvan IV ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_jungle_aggre, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_jungle_between
screen_intermediate_title = Label(screen_begin_jungle_between, text='Your Recommended Champions are: KhaZix, Warwick, Sejuani ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_jungle_between, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()


#==============================================================screen_begin_marksman_pass
screen_intermediate_title = Label(screen_begin_marksman_pass, text='Your Recommended Champions are: Sivir, Jinx, Ashe ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_marksman_pass, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_marksman_aggre
screen_intermediate_title = Label(screen_begin_marksman_aggre, text='Your Recommended Champions are: Caitlyn, Lucian, Tristana ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_marksman_aggre, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_marksman_between
screen_intermediate_title = Label(screen_begin_marksman_between, text='Your Recommended Champions are: Caitlyn, Lucian, Miss Fortune ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_marksman_between, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()


#==============================================================screen_begin_support_pass
screen_intermediate_title = Label(screen_begin_support_pass, text='Your Recommended Champions are: Soraka, Lulu, Janna ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_support_pass, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_support_aggre
screen_intermediate_title = Label(screen_begin_support_aggre, text='Your Recommended Champions are: Leona, Blitzcrank, Nautilus ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_support_aggre, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()

#==============================================================screen_begin_support_between
screen_intermediate_title = Label(screen_begin_support_between, text='Your Recommended Champions are: Lulu, Blitzcrank, Braum ',
                       font='times 30', bg='white')
screen_intermediate_title.pack(fill='x')

screen_intermediate_button = Button(screen_begin_support_between, text='Try Again!', font='times 15', padx=10, pady=10, bg='green',
                         command=lambda: display_screen(screen_1))
screen_intermediate_button.pack()


# display the first screen when the program starts
display_screen(screen_1)

root.mainloop()