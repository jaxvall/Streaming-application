import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from bintreeFile import Bintree
from PIL import ImageTk, Image
from pathlib import Path
import webbrowser
import random
import imageio
import cv2

FONT1 = ("Times New Roman", 13)
FONT2 = ("Arial", 13, 'bold')
HEAD_FONT = ("Courier", 15, 'bold')
NAME_FONT = ("ms sans serif", 11)
LOG_FONT = ("Courier", 12, 'italic')
CHAT_FONT = ("Contantia", 10)

# Main class
class Viastream(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        tk.Tk.iconbitmap(self, default='football_icon.ico')

        # Creates menu tabs using Notebook
        tab_control = ttk.Notebook(self, takefocus=0)

        # Creating frames inside the tabs
        matches_frame = ttk.Frame(tab_control)
        self.sign_frame = ttk.Frame(tab_control)
        # Adding the tabs to the notebook
        tab_control.add(matches_frame, text='Matches')
        tab_control.add(self.sign_frame, text='Sign in')

        # matches_frame.grid_rowconfigure(0, weight = 1)
        # matches_frame.grid_columnconfigure(0, weight = 1)
        tab_control.pack(expand=1, fill='both')

        # Creates dictionaries used to store frame objects
        self.frames1 = {}
        self.frames2 = {}
        self.login = False
        self.username = "Ernesto"

        # Stores the different pages(frames) in the dictionary
        for page in (FrontPage, StreamPage):

            frame = page(matches_frame, self)
            self.frames1[page] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        for page in (SignIn, SignUp, LoggedIn):

            frame = page(self.sign_frame, self)
            self.frames2[page] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame1(FrontPage)
        self.show_frame2(SignIn)

    # Shows a frame by raising it to the top
    def show_frame1(self, cont):
        frame = self.frames1[cont]
        # if cont == StreamPage:
        #     frame.stream_video()
        frame.tkraise()

    def show_frame2(self, cont):
        if self.login == True and cont != LoggedIn:
            self.logout_f()
        frame = self.frames2[cont]
        frame.tkraise()

    # Changes the login status and username when a user logs in
    def login_f(self, account):
        self.login = True
        self.username = account.name
        site.update()

    # Changes the login status and username whena user logs out
    def logout_f(self):
        self.login = False
        self.username = ""
        site.update()

    def logged_user(self):
        frame = self.frames2[LoggedIn]
        frame.login_username()

    # Used to check if a user is logged in
    def check_login(self):
        if self.login is True:
            messagebox.showinfo('Sign in', 'You need to be a premium member to watch this stream')
            return
            self.show_frame1(StreamPage)
        else:
            messagebox.showinfo('Sign in', 'You need to be a premium member to watch this stream')

def open_ad(event):
    webbrowser.open_new(r"https://youtu.be/1KsyZF590NM?t=70")

def open_hd(event):
    webbrowser.open_new(r"https://i.kym-cdn.com/entries/icons/original/000/017/403/218_copy.jpg")

# Creates a random viewer count for the matches
def random_count(match):
    viewers = 0
    if match == 1:
        viewers = random.randrange(12000, 13000)
    elif match == 2:
        viewers = random.randrange(54000, 57000)
    # elif match == 3:
    #     viewers = random.randrange(6000, 6500)
    # elif match == 4:
    #     viewers = random.randrange(13000, 14000)
    # elif match == 5:
    #     viewers = random.randrange(2500, 3000)
    # elif match == 6:
    #     viewers = random.randrange(3100, 3200)
    return "(" + "{:,}".format(viewers) + ")"

# Class for the starting page
class FrontPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img_logo = tk.PhotoImage(file='logo2.gif')

        full_hd = tk.PhotoImage(file='full_hd.gif')

        # Pictures of the advertisments
        casino1 = tk.PhotoImage(file='casino_ad1.gif')
        casino2 = tk.PhotoImage(file='casino_ad2.gif')

        logo = tk.Label(self, image=img_logo)
        logo.img_logo = img_logo


        title = tk.Label(self, text='Welcome to Viastream! The best streaming service on earth!!', bg='light blue', font=HEAD_FONT)

        heading1 = tk.Label(self, text='Matches', font=FONT2)
        heading2 = tk.Label(self, text='Score', font=FONT2)
        heading3 = tk.Label(self, text='Link (Viewers)', font=FONT2)
        heading4 = tk.Label(self, text='Scheduled time', font=FONT2)

        match1 = tk.Label(self, text='FC Porto - AS Roma', font=FONT1)
        match2 = tk.Label(self, text='PSG - Man Utd', font=FONT1)
        match3 = tk.Label(self, text='Stade Rennais - Arsenal', font=FONT1)
        match4 = tk.Label(self, text='Leicester City - Fulham', font=FONT1)
        match5 = tk.Label(self, text='Southampton - Tottenham hotspur', font=FONT1)
        match6 = tk.Label(self, text='Juventus - Atlético Madrid', font=FONT1)

        score1 = tk.Label(self, text='1-2', font=FONT1)
        score2 = tk.Label(self, text='1-1', font=FONT1)
        score3 = tk.Label(self, text='-', font=FONT1)
        score4 = tk.Label(self, text='-', font=FONT1)
        score5 = tk.Label(self, text='-', font=FONT1)
        score6 = tk.Label(self, text='-', font=FONT1)

        # Creates the label to look lika a link to watch the match
        view_label1 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label1, view_label1.cget('font')) # Gets the font of the newly made label
        f.configure(underline=True) # Changing the underline setting of the current font
        view_label1.configure(font=f) # Sets the label to have the new font
        view_label1.bind('<Button-1>', lambda e: controller.show_frame1(StreamPage)) # Binds the label to visit the streaming page

        view_label2 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label2, view_label2.cget('font'))
        f.configure(underline=True)
        view_label2.configure(font=f)
        view_label2.bind('<Button-1>', lambda e: controller.check_login())

        view_label3 = tk.Label(self, text='View match', cursor='hand2', font=FONT1)
        f = font.Font(view_label3, view_label3.cget('font'))
        f.configure(underline=True)
        view_label3.configure(font=f)
        view_label3.bind('<Button-1>', lambda e: messagebox.showinfo('Cannot watch', 'The match is not live yet'))

        view_label4 = tk.Label(self, text='View match', cursor='hand2', font=FONT1)
        f = font.Font(view_label4, view_label4.cget('font'))
        f.configure(underline=True)
        view_label4.configure(font=f)
        view_label4.bind('<Button-1>', lambda e: messagebox.showinfo('Cannot watch', 'The match is not live yet'))

        view_label5 = tk.Label(self, text='View match', cursor='hand2', font=FONT1)
        f = font.Font(view_label5, view_label5.cget('font'))
        f.configure(underline=True)
        view_label5.configure(font=f)
        view_label5.bind('<Button-1>', lambda e: messagebox.showinfo('Cannot watch', 'The match is not live yet'))

        view_label6 = tk.Label(self, text='View match', cursor='hand2', font=FONT1)
        f = font.Font(view_label6, view_label6.cget('font'))
        f.configure(underline=True)
        view_label6.configure(font=f)
        view_label6.bind('<Button-1>', lambda e: messagebox.showinfo('Cannot watch', 'The match is not live yet'))

        viewer_count1 = tk.Label(self, text=random_count(1))
        viewer_count2 = tk.Label(self, text=random_count(2))
        viewer_count3 = tk.Label(self, text='( )')
        viewer_count4 = tk.Label(self, text='( )')
        viewer_count5 = tk.Label(self, text='( )')
        viewer_count6 = tk.Label(self, text='( )')

        schedule1 = tk.Label(self, text='Ongoing', font=FONT1)
        schedule2 = tk.Label(self, text='Ongoing', font=FONT1)
        schedule3 = tk.Label(self, text='Tomorrow 18:55', font=FONT1)
        schedule4 = tk.Label(self, text='Saturday 9 mars 16:00', font=FONT1)
        schedule5 = tk.Label(self, text='Saturday 9 mars 16:00', font=FONT1)
        schedule6 = tk.Label(self, text='Tuesday 12 mars 21:00', font=FONT1)

        hd_label1 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label1.full_hd = full_hd
        hd_label1.bind('<Button-1>', open_hd)
        hd_label2 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label2.full_hd = full_hd
        hd_label3 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label3.full_hd = full_hd
        hd_label4 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label4.full_hd = full_hd
        hd_label5 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label5.full_hd = full_hd
        hd_label6 = tk.Label(self, image=full_hd, cursor='hand2')
        hd_label6.full_hd = full_hd

        ad1 = tk.Label(self, image=casino1, cursor='hand2')
        ad1.bind('<Button-1>', open_ad)
        ad1.casino1 = casino1

        ad2 = tk.Label(self, image=casino2, cursor='hand2')
        ad2.bind('<Button-1>', open_ad)
        ad2.casino2 = casino2

        logo.grid(row=0, column=0, padx=(0, 43), pady=(0, 10))

        title.grid(row=0, column=0, columnspan=100, ipadx=65, ipady=55, padx=(180, 0), pady=(0, 10))

        heading1.grid(row=1, column=0, columnspan=1, sticky='w')
        heading2.grid(row=1, column=1, columnspan=1, sticky='w')
        heading3.grid(row=1, column=2, columnspan=2, sticky='w')
        heading4.grid(row=1, column=4, columnspan=1, sticky='w')

        match1.grid(row=2, column=0, sticky='w')
        match2.grid(row=3, column=0, sticky='w')
        match3.grid(row=4, column=0, sticky='w')
        match4.grid(row=5, column=0, sticky='w')
        match5.grid(row=6, column=0, sticky='w')
        match6.grid(row=7, column=0, padx=(0, 50), sticky='w')

        score1.grid(row=2, column=1, padx=4, sticky='w')
        score2.grid(row=3, column=1, padx=4, sticky='w')
        score3.grid(row=4, column=1, padx=4, sticky='w')
        score4.grid(row=5, column=1, padx=4, sticky='w')
        score5.grid(row=6, column=1, padx=4, sticky='w')
        score6.grid(row=7, column=1, padx=(4, 60), sticky='w')

        view_label1.grid(row=2, column=2, sticky='w')
        view_label2.grid(row=3, column=2, sticky='w')
        view_label3.grid(row=4, column=2, sticky='w')
        view_label4.grid(row=5, column=2, sticky='w')
        view_label5.grid(row=6, column=2, sticky='w')
        view_label6.grid(row=7, column=2, sticky='w')

        viewer_count1.grid(row=2, column=3, sticky='w')
        viewer_count2.grid(row=3, column=3, sticky='w')
        viewer_count3.grid(row=4, column=3, sticky='w')
        viewer_count4.grid(row=5, column=3, sticky='w')
        viewer_count5.grid(row=6, column=3, sticky='w')
        viewer_count6.grid(row=7, column=3, padx=(0, 60),  sticky='w')

        schedule1.grid(row=2, column=4, sticky='w')
        schedule2.grid(row=3, column=4, sticky='w')
        schedule3.grid(row=4, column=4, sticky='w')
        schedule4.grid(row=5, column=4, sticky='w')
        schedule5.grid(row=6, column=4, sticky='w')
        schedule6.grid(row=7, column=4, padx=(0, 20),  sticky='w')

        hd_label1.grid(row=2, column=5, pady=5, sticky='w')
        hd_label2.grid(row=3, column=5, pady=5, sticky='w')
        hd_label3.grid(row=4, column=5, pady=5, sticky='w')
        hd_label4.grid(row=5, column=5, pady=5, sticky='w')
        hd_label5.grid(row=6, column=5, pady=5, sticky='w')
        hd_label6.grid(row=7, column=5, padx=(0, 120), pady=5, sticky='w')

        ad1.grid(row=8, column=0, columnspan=5, rowspan=10, pady=(10, 23), sticky='w')
        ad2.grid(row=1, column=6, rowspan=8, columnspan=60, pady=(0, 10))

# Class for the streaming page
class StreamPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.emote0 = tk.PhotoImage(file='football1.gif')
        self.emote1 = tk.PhotoImage(file='pogchamp.gif')
        self.emote2 = tk.PhotoImage(file='biblethump.gif')
        self.emote3 = tk.PhotoImage(file='smile.gif')

        self.emote_dict = {'FootballE ': self.emote0, 'PogChamp ': self.emote1, 'BibleThump ': self.emote2, ':)': self.emote3}
        self.emote_list = list(self.emote_dict.keys())

        # Reads in the video to be streamed
        self.cap = cv2.VideoCapture('match2_t.mp4')
        self.cap_r = self.cap.get(5)
        self.cap_l = self.cap.get(7)

        # List containing the different chat rooms used by optionmenu
        self.chats = ['Home team', 'Away team', 'All chat']

        chat_frame = tk.Frame(self, borderwidth=2, highlightbackground='blue', relief='ridge')

        self.stream_label = tk.Label(self)

        # Creates variables used by the optionmenus
        self.chat_var = tk.StringVar(chat_frame)
        self.emote_var = tk.StringVar(chat_frame)

        button1 = ttk.Button(self, text='Go back', takefocus=0, command=self.go_front_page)
        chat_label = tk.Label(chat_frame, text='Viewer chat', font=NAME_FONT)
        chat_menu = ttk.OptionMenu(chat_frame, self.chat_var, self.chats[2], *self.chats)
        self.chat = tk.Text(chat_frame, height=26, width=37, font=CHAT_FONT, state='disabled', wrap='word')
        self.chat_var.trace('w', self.clear_chat_text)

        self.message = tk.Text(chat_frame, height=4, width=35, font=CHAT_FONT, wrap='word')

        emote_menu = ttk.OptionMenu(chat_frame, self.emote_var, 'Emotes', *self.emote_list, command=self.emote_select)

        chat_button = ttk.Button(chat_frame, width=7, text='Send', takefocus=0, command=self.send_message)
        self.message.bind('<Return>', self.send_message) # Makes it possible to chat by using the enter key

        self.stream_label.grid(row=0, column=0, columnspan=2, rowspan=10, padx=12)

        chat_frame.grid(row=0, column=3, columnspan=2, pady=(0, 0))

        button1.grid(row=0, column=0, padx=(0, 649), pady=(0, 510))

        # Starts the video
        self.stream_video()

        chat_label.grid(row=0, column=3, columnspan=2, padx=(0, 170), pady=(7, 3))
        chat_menu.grid(row=0, column=3, columnspan=2, padx=(160, 0), pady=(7, 1))
        self.chat.grid(row=2, column=3)
        self.message.grid(row=3, column=3, pady=(5, 0))
        emote_menu.grid(row=4, column=3, columnspan=2, padx=(60, 0), pady=(5, 6))
        chat_button.grid(row=4, column=3, columnspan=2, padx=(201, 0), pady=(5, 6))

        # Insert the default info message
        self.message.insert(tk.INSERT, 'Write a message')
        self.message.bind('<Button-1>', self.clear_default_text) # Clears the default text when clicking in the widget

    def stream_video(self):
        ret, frame = self.cap.read()

        if ret is True:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image).resize((750, 470))
            imgtk = ImageTk.PhotoImage(image=img)
            self.stream_label.configure(image=imgtk)
            self.stream_label.imgtk = imgtk # Creates a reference to the image
            self.stream_label.after(4, self.stream_video)

    def clear_default_text(self, event=None):
        if self.message.get(0.0, 'end') == 'Write a message\n':
            self.message.delete(0.0, 'end')

    def clear_message_text(self):
        self.message.delete(1.0, 'end')

    def go_front_page(self):
        self.clear_chat_text()
        self.chat_var.set(self.chats[2])
        self.controller.show_frame1(FrontPage)

    def clear_chat_text(self, *args):
        self.chat.config(state='normal')
        self.chat.delete(0.0, 'end')
        self.chat.config(state='disabled')

    def emote_select(self, emote):
        self.message.insert(tk.INSERT, emote)
        self.emote_var.set('Emotes')

    def send_message(self, event=None):
        if not site.login:
            messagebox.showinfo('Cannot send', 'You need to login before you can chat')
            return
        elif self.message.compare('end-1c', '!=', '1.0'): # Checks if it is an empty string
            # Removes the new line and adds a space so it works correctly with the send_emote function
            message = self.message.get(0.0, 'end').strip('\n') + ' '
            max_length = 200 # Sets the maximum amount of characters a message can contain
            if len(message) > max_length:
                message = message[:max_length]
            self.chat.config(state='normal')
            self.chat.insert(tk.INSERT, site.username + ": ")

            self.send_emote(message)

            self.chat.see('end')
            self.clear_message_text()
            self.chat.config(state='disabled')
            # event.widget.mark_set(tk.INSERT, '1.0')
        return 'break'

    def send_emote(self, message):
        message = self.replace_emotes(message) # Replaces the emots with a ¤ followed by the emote number
        index_mark = 0 # Varible to keep track of where you are in the message for inserting into chat
        for i in range(len(message)):
            char = message[i]
            if char == '¤':
                self.chat.insert(tk.INSERT, message[index_mark:i]) # Inserts the message from the saved index to the current
                emote = self.emote_list[int(message[i+1])] # Retrieves the right emote decided by the number after ¤
                self.chat.image_create(tk.INSERT, image=self.emote_dict[emote])
                self.chat.insert(tk.INSERT, ' ') # Inserts the lost space when the emote got replaced
                index_mark = i + 2 # Sets the marked index to the character after the ¤ and its following number
                # if index_mark == len(message) - 1:
                #     self.chat.insert(tk.INSERT, '\n')
        self.chat.insert(tk.INSERT, message[index_mark:] + '\n')

    def replace_emotes(self, message):
        for num in range(len(self.emote_list)):
            emote = self.emote_list[num]
            if emote in message: # Checks if the emote is in the message
                message = message.replace(emote, '¤' + str(num)) # Replaces the emote with a ¤ followed by the emote number
        return message

# Frame when signing in
class SignIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        space = tk.Label(self)
        space.grid(row=0, column=0, padx=14, pady=2)

        username = tk.Label(self, text='Username', font=FONT1)
        password = tk.Label(self, text='Password', font=FONT1)
        self.name_entry = ttk.Entry(self, width=25)
        self.password_entry = ttk.Entry(self, show='\u2022', width=25)

        self.name_entry.bind('<Return>', self.sign_in_click) # So you can use the enter key to log in
        self.password_entry.bind('<Return>', self.sign_in_click)

        self.var = tk.IntVar() # Variable for storing if the check box is marked or not
        show_pass = ttk.Checkbutton(self, text='Show password', takefocus=0, variable=self.var, command=self.show_password)

        sign_button = ttk.Button(self, text='Sign in', takefocus=0, command=self.sign_in_click)

        sign_up = tk.Label(self, text='Create an account', fg='steel blue', cursor='hand2')
        f = font.Font(sign_up, sign_up.cget('font'))
        f.configure(underline=True)
        sign_up.configure(font=f)
        sign_up.bind('<Button-1>', lambda e: controller.show_frame2(SignUp))

        username.grid(row=1, column=1, sticky='w')
        password.grid(row=3, column=1, sticky='w')
        self.name_entry.grid(row=2, column=1, pady=(0, 10))
        self.password_entry.grid(row=4, column=1, pady=(0, 10))

        show_pass.grid(row=5, column=1, pady=(0, 10), sticky='w')

        sign_button.grid(row=6, column=1)

        sign_up.grid(row=7, column=1, pady=5)

    # Changes the characters to show in the password entry
    def show_password(self):
        if self.var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='\u2022')

    def sign_in_click(self, event=None):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if len(username) < 1 or len(password) < 1:
            messagebox.showinfo('Cannot sign in', 'You need to fill in all the fields')
            return
        elif username not in tree:
            messagebox.showinfo('Cannot sign in', 'Username does not exist')
            return

        hash_pass = hash_function(password) # Hashed the password
        account = tree.get(username) # Gets the account object from the tree

        if account.password != hash_pass: # Checks if hash value is the same as the one stored
            messagebox.showinfo('Cannot sign in', 'Password is incorrect')
            return

        site.login_f(account)
        site.logged_user()
        self.controller.show_frame2(LoggedIn)

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        username = tk.Label(self, text='Username', font=FONT1)
        email = tk.Label(self, text='Email', font=FONT1)
        password = tk.Label(self, text='Password', font=FONT1)
        password2 = tk.Label(self, text='Confirm password', font=FONT1)
        self.name_entry = ttk.Entry(self, width=25)
        self.email_entry = ttk.Entry(self, width=25)
        self.password_entry = ttk.Entry(self, show='\u2022', width=25)
        self.password_entry2 = ttk.Entry(self, show='\u2022', width=25)

        self.name_entry.bind('<Return>', self.sign_up_click)
        self.email_entry.bind('<Return>', self.sign_up_click)
        self.password_entry.bind('<Return>', self.sign_up_click)
        self.password_entry2.bind('<Return>', self.sign_up_click)

        self.var = tk.IntVar()
        show_pass = ttk.Checkbutton(self, text='Show password', takefocus=0, variable=self.var, command=self.show_password)

        sign_button = ttk.Button(self, text='Sign up', takefocus=0, command=self.sign_up_click)

        sign_in = tk.Label(self, text='Already have an account?', fg='steel blue', cursor='hand2')
        f = font.Font(sign_in, sign_in.cget('font'))
        f.configure(underline=True)
        sign_in.configure(font=f)
        sign_in.bind('<Button-1>', lambda e: controller.show_frame2(SignIn))

        space = tk.Label(self)
        space.grid(row=0, column=0, padx=14, pady=2)

        username.grid(row=1, column=1, sticky='w')
        email.grid(row=3, column=1, sticky='w')
        password.grid(row=5, column=1, sticky='w')
        password2.grid(row=7, column=1, sticky='w')
        self.name_entry.grid(row=2, column=1, pady=(0, 10))
        self.email_entry.grid(row=4, column=1, pady=(0, 10))
        self.password_entry.grid(row=6, column=1, pady=(0, 10))
        self.password_entry2.grid(row=8, column=1, pady=(0, 10))

        show_pass.grid(row=9, column=1, pady=(0, 10), sticky='w')

        sign_button.grid(row=10, column=1)

        sign_in.grid(row=11, column=1, pady=5)

    def show_password(self):
        if self.var.get():
            self.password_entry.config(show='')
            self.password_entry2.config(show='')
        else:
            self.password_entry.config(show='\u2022')
            self.password_entry2.config(show='\u2022')

    def sign_up_click(self, event=None):
        username = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        password2 = self.password_entry2.get()

        if len(username) < 1 or len(email) < 1 or len(password) < 1 or len(password2) < 1:
            messagebox.showinfo('Cannot sign you up', 'You need to fill in all the fields')
            return
        elif password != password2:
            messagebox.showinfo('Cannot sign you up', 'Passwords does not match')
            return
        elif username in tree:
            messagebox.showinfo('Cannot sign you up', 'Username already exists')
            return

        hash_pass = hash_function(password)

        new = Account(username, email, hash_pass)
        tree.put(username, new)
        messagebox.showinfo('Thank you!', 'Thank you for signing up. You can now proceed to login.')

        # Clears all the entries when sigining up
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.password_entry2.delete(0, 'end')
        self.controller.show_frame2(SignIn)

# Frame when a user is logged in
class LoggedIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.label1 = tk.Label(self, text='Logged in', font=LOG_FONT)
        logout_label = tk.Label(self, text='Logout', fg='steel blue', cursor='hand2', font=LOG_FONT)
        f = font.Font(logout_label, logout_label.cget('font'))
        f.configure(underline=True)
        logout_label.configure(font=f)
        logout_label.bind('<Button-1>', lambda e: controller.show_frame2(SignIn))

        self.label1.grid(row=0, column=0, padx=20, pady=20)
        logout_label.grid(row=0, column=1)

    def login_username(self):
        self.label1.config(text='Logged in as "' + site.username + '"')

# Class for all the accounts
class Account:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

def hash_function(key):
    hash_value = 0
    counter = 1
    for tkn in key:
        hash_value += ord(tkn) * counter
        counter += 2
    length = len(str(hash_value)) - 1

    # Salts the hash value with a different number depending on the amount of digits
    if length > 3:
        salt = "7" * length
        hash_value -= int(salt)
    elif length <= 3:
        salt = "7" * (length + 1)
        hash_value += int(salt)
    print(hash_value)
    return int(hash_value)

tree = Bintree()
member1 = Account('ernesto', 'e', 878)
tree.put('ernesto', member1)

site = Viastream()
site.title("Viastream.com")
site.geometry("1050x590")
site.update_idletasks() # Updates the geometry of the window
centerw = int(site.winfo_screenwidth()/2-site.winfo_width()/2) # Used the center the window on the screen
centerh = int(site.winfo_screenheight()/2-site.winfo_height()/2) - 20
site.geometry("+{}+{}".format(centerw, centerh))
site.resizable(0,0) # Makes to window unable to resize
site.mainloop()
