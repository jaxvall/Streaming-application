import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from hash import *
import webbrowser
import random
from PIL import ImageTk, Image
import cv2

FONT1 = ("Times New Roman", 13)
FONT2 = ("Arial", 13, 'bold')
HEAD_FONT = ("Courier", 15, 'bold')
NAME_FONT = ("ms sans serif", 11)
LOG_FONT = ("Courier", 13, 'italic')

class Viastream(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.iconbitmap(self, default='football_icon.ico')

        tab_control = ttk.Notebook(self)
        matches_frame = ttk.Frame(tab_control)
        self.sign_frame = ttk.Frame(tab_control)
        tab_control.add(matches_frame, text='Matches')
        tab_control.add(self.sign_frame, text='Sign in')

        # container.pack(fill='both')
        matches_frame.grid_rowconfigure(0, weight = 1)
        matches_frame.grid_columnconfigure(0, weight = 1)
        tab_control.pack(expand=1, fill='both')


        # im = ImageTk.PhotoImage(Image.open("football_banner.jpg"))
        # banner = Label(self, image = im)
        # banner.pack()

        self.frames1 = {}
        self.frames2 = {}
        self.login = False
        self.username = "Ernesto"

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

    def show_frame1(self, cont):
        frame = self.frames1[cont]
        frame.tkraise()

    def show_frame2(self, cont):
        if self.login == True and cont != LoggedIn:
            self.logout_f()
        frame = self.frames2[cont]
        frame.tkraise()

    def login_f(self, account):
        self.login = True
        self.username = account.name
        site.update()

    def logout_f(self):
        self.login = False
        self.username = ""
        site.update()

    def logged_user(self):
        frame = LoggedIn(self.sign_frame, self)
        frame.login_username()

def open_stream(event):
    print('This worked:))')
    # webbrowser.open_new(r"http://www.google.com")

def random_count(match):
    viewers = 0
    if match == 1:
        viewers = random.randrange(300, 400)
    elif match == 2:
        viewers = random.randrange(10500, 11000)
    elif match == 3:
        viewers = random.randrange(6000, 6500)
    elif match == 4:
        viewers = random.randrange(7600, 8000)
    elif match == 5:
        viewers = random.randrange(1100, 1200)

    return "(" + "{:,}".format(viewers) + ")"

class FrontPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title = tk.Label(self, text='Welcome to Viastream! The best streaming service on earth!!', font=HEAD_FONT)

        heading1 = tk.Label(self, text='Matches', font=FONT2)
        heading2 = tk.Label(self, text='Home Team Chat (Viewers)', font=FONT2)
        heading3 = tk.Label(self, text='Away Team Chat (Viewers)', font=FONT2)
        heading4 = tk.Label(self, text='All Chat (Viewers)', font=FONT2)

        view_label1 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label1, view_label1.cget('font'))
        f.configure(underline=True)
        view_label1.configure(font=f)
        view_label1.bind('<Button-1>', lambda e: controller.show_frame1(StreamPage))

        view_label2 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label2, view_label2.cget('font'))
        f.configure(underline=True)
        view_label2.configure(font=f)
        view_label2.bind('<Button-1>', lambda e: messagebox.showinfo('Sign up!', 'You need to sign up to gain access to this stream'))

        view_label3 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label3, view_label3.cget('font'))
        f.configure(underline=True)
        view_label3.configure(font=f)
        view_label3.bind('<Button-1>', lambda e: controller.show_frame1(StreamPage))

        view_label4 = tk.Label(self, text='View match', fg='steel blue', cursor='hand2', font=FONT1)
        f = font.Font(view_label4, view_label4.cget('font'))
        f.configure(underline=True)
        view_label4.configure(font=f)
        view_label4.bind('<Button-1>', lambda e: controller.show_frame1(StreamPage))

        viewer_count1 = tk.Label(self, text=random_count(1))
        viewer_count2 = tk.Label(self, text=random_count(2))
        viewer_count3 = tk.Label(self, text=random_count(3))
        viewer_count4 = tk.Label(self, text=random_count(4))
        viewer_count5 = tk.Label(self, text=random_count(5))

        empty = tk.Label(self)

        match1 = tk.Label(self, text='Arsenal vs Liverpool', font=FONT1)
        match2 = tk.Label(self, text='Real Madrid vs Athletic Bilbao', font=FONT1)
        match3 = tk.Label(self)
        match4 = tk.Label(self)
        match5 = tk.Label(self, text='Fulham vs Crystal Palace', font=FONT1)
        match6 = tk.Label(self)

        title.grid(row=0, column=0, columnspan=100, pady=(20, 50))

        heading1.grid(row=1, column=0, columnspan=3, sticky='w')
        heading2.grid(row=1, column=1, columnspan=3, sticky='w')
        heading3.grid(row=1, column=4, columnspan=3, sticky='w')
        heading4.grid(row=1, column=7, columnspan=3, sticky='w')

        view_label1.grid(row=2, column=2, sticky='w')
        view_label2.grid(row=2, column=5, sticky='w')
        view_label3.grid(row=2, column=8, sticky='w')
        view_label4.grid(row=3, column=2, sticky='w')

        match1.grid(row=2, column=0, sticky='w')
        match2.grid(row=3, column=0, sticky='w')
        match3.grid(row=4, column=0, sticky='w')
        match4.grid(row=5, column=0, sticky='w')
        match5.grid(row=6, column=0, sticky='w')
        match6.grid(row=7, column=0, sticky='w')

        viewer_count1.grid(row=2, column=3, sticky='w')
        viewer_count2.grid(row=2, column=6, sticky='w')
        viewer_count3.grid(row=2, column=9, sticky='w')
        viewer_count4.grid(row=3, column=3, sticky='w')
        viewer_count5.grid(row=3, column=6, sticky='w')

        empty.grid(row=2, column=1, padx=(0, 0))

class StreamPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        chat_frame = tk.Frame(self, borderwidth=2, highlightbackground='blue', relief='ridge')

        video_frame = tk.Frame(self, width=100, height=300)

        button1 = ttk.Button(video_frame, text='Go back', command=self.go_front_page)
        stream_label = tk.Label(chat_frame, text='Viewer chat', font=NAME_FONT)
        self.chat = tk.Text(chat_frame, height=29, width=30, state='disabled', wrap='word')
        self.message = tk.Text(chat_frame, height=3, width=20)
        chat_button = ttk.Button(chat_frame, text='Send', command=self.send_message)

        self.message.bind('<Return>', self.send_message)

        chat_frame.pack(side='right', pady=(0, 25))
        video_frame.pack(side='left')
        button1.pack(side='top')
        stream_label.pack(side='top', anchor='w')
        self.chat.pack(side='top')
        self.message.pack(side='left')
        chat_button.pack(side='right', pady=(30, 0))

        self.message.insert(tk.INSERT, 'Write a message')
        self.message.bind('<Button-1>', self.clear_default_text)

    def clear_default_text(self, event=None):
        if self.message.get(0.0, 'end') == 'Write a message\n':
            self.message.delete(0.0, 'end')

    def clear_message_text(self):
        self.message.delete(1.0, 'end')

    def go_front_page(self):
        self.clear_chat_text()
        self.controller.show_frame1(FrontPage)

    def clear_chat_text(self):
        self.chat.config(state='normal')
        self.chat.delete(0.0, 'end')
        self.chat.config(state='disabled')

    def send_message(self, event=None):
        if not site.login:
            messagebox.showinfo('Cannot write', 'You need to login before you can chat')
            return
        elif self.message.compare('end-1c', '!=', '1.0'):
            self.chat.config(state='normal')
            self.chat.insert(tk.INSERT, site.username + ": ")
            self.chat.insert(tk.INSERT, self.message.get(0.0, 'end'))
            self.chat.see('end')
            self.clear_message_text()
            self.chat.config(state='disabled')
            self.message.mark_set(tk.INSERT, '0.0')

class SignIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        username = tk.Label(self, text='Username', font=FONT1)
        password = tk.Label(self, text='Password', font=FONT1)
        self.name_entry = ttk.Entry(self)
        self.password_entry = ttk.Entry(self, show='*')

        sign_button = ttk.Button(self, text='Sign in', command=self.sign_in_click)

        sign_up = tk.Label(self, text='Make account', fg='steel blue', cursor='hand2')
        f = font.Font(sign_up, sign_up.cget('font'))
        f.configure(underline=True)
        sign_up.configure(font=f)
        sign_up.bind('<Button-1>', lambda e: controller.show_frame2(SignUp))

        username.grid(row=0, column=0)
        password.grid(row=1, column=0)
        self.name_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        sign_button.grid(row=2, column=1)

        sign_up.grid(row=2, column=0)

    def sign_in_click(self):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if len(username) < 1 or len(password) < 1:
            messagebox.showinfo('Cannot sign in', 'You need to fill in all the fields')
            return
        elif username not in table:
            messagebox.showinfo('Cannot sign in', 'Username does not exist')
            return

        account = table.get(username)
        if account.password != password:
            messagebox.showinfo('Cannot sign in', 'Password is incorrect')

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
        self.name_entry = ttk.Entry(self)
        self.email_entry = ttk.Entry(self)
        self.password_entry = ttk.Entry(self, show='*')
        self.password_entry2 = ttk.Entry(self, show='*')

        sign_button = ttk.Button(self, text='Sign up', command=self.sign_up_click)

        sign_in = tk.Label(self, text='Already have an account?', fg='steel blue', cursor='hand2')
        f = font.Font(sign_in, sign_in.cget('font'))
        f.configure(underline=True)
        sign_in.configure(font=f)
        sign_in.bind('<Button-1>', lambda e: controller.show_frame2(SignIn))

        username.grid(row=0, column=0, sticky='w')
        email.grid(row=1, column=0, sticky='w')
        password.grid(row=2, column=0, sticky='w')
        password2.grid(row=3, column=0, sticky='w')
        self.name_entry.grid(row=0, column=1)
        self.email_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)
        self.password_entry2.grid(row=3, column=1)

        sign_button.grid(row=4, column=1)

        sign_in.grid(row=4, column=0)

    def sign_up_click(self):
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
        elif username in table:
            messagebox.showinfo('Cannot sign you up', 'Username already exists')
            return

        new = Account(username, email, password)
        table.store(username, new)
        messagebox.showinfo('Thank you!', 'Thank you for signing up. You can now proceed to login.')
        self.controller.show_frame2(SignIn)

class LoggedIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.label1 = tk.Label(self, text='Logged in as ', font=LOG_FONT)
        logout_label = tk.Label(self, text='Logout', fg='steel blue', cursor='hand2', font=LOG_FONT)
        f = font.Font(logout_label, logout_label.cget('font'))
        f.configure(underline=True)
        logout_label.configure(font=f)
        logout_label.bind('<Button-1>', lambda e: controller.show_frame2(SignIn))

        self.label1.grid(row=0, column=0, padx=20, pady=20)
        logout_label.grid(row=0, column=1)

    def login_username(self):
        self.label1.config(text='Logged in as ' + site.username)

class Account:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


table = HashTable(100)

site = Viastream()
site.title("Viastream.com")
site.geometry("1000x600")
site.update_idletasks()
centerw = int(site.winfo_screenwidth()/2-site.winfo_width()/2)
centerh = int(site.winfo_screenheight()/2-site.winfo_height()/2)
site.geometry("+{}+{}".format(centerw, centerh))
site.resizable(0,0)
site.mainloop()
