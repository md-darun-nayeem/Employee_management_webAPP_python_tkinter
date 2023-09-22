from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # image processing capabilities
from tkinter import messagebox



def main():
    win = Tk()
    app = Login_window(win)
    win.state('zoom')
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title = "Log In"
        self.root.geometry = "1800*900+0+0"

        # Background Image
        self.bg = ImageTk.PhotoImage(file="background01.jpg")
        lbl_bg = Label(self.root, image=self.bg)  # for showing image on window
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)  # we used rel to make it suitable for every divice

        # Frame making
        frame = Frame(self.root, bg="black")
        frame.place(x=1400, y=170, width=340, height=700)

        # Top login PNG
        img1 = Image.open("login.png")
        img1 = img1.resize((260, 100), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage1 = ImageTk.PhotoImage(img1)
        lblimg = Label(image=self.photoImage1, bg="white", borderwidth=0)
        lblimg.place(x=1435, y=175, width=260, height=100)

        # Start Now label
        get_str = Label(frame, text="Start Now", font=("times new roman", 20, "bold"), fg="black", bg="orange")
        get_str.place(x=95, y=120)

        # user_name label
        user_name = Label(frame, text="User Name", font=("times new roman", 15, "bold"), fg="black", bg="orange")
        user_name.place(x=70, y=185)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=40, y=220, width=270)

        # password label
        user_pass = Label(frame, text="Enter Password", font=("times new roman", 15, "bold"), fg="black", bg="orange")
        user_pass.place(x=70, y=275)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=310, width=270)

        # Icon Image
        img2 = Image.open("user2.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage2 = ImageTk.PhotoImage(img2)
        lblimg = Label(frame, image=self.photoImage2, bg="white", borderwidth=0)
        lblimg.place(x=30, y=185, width=25, height=25)

        # Pass icon image
        img3 = Image.open("pass.png")
        img3 = img3.resize((30, 30), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage3 = ImageTk.PhotoImage(img3)
        lblimg = Label(frame, image=self.photoImage3, bg="white", borderwidth=0)
        lblimg.place(x=30, y=275, width=30, height=30)

        # Log In Button  Activeforground will help us not to change the color when we click the button
        logInButton = Button(frame, command=self.login, text="Log In", font=("times new roman", 20, "bold"),
                             bd=3, relief=RIDGE, fg="black", bg="yellow", activebackground="yellow",
                             activeforeground="black")  # Relief is boarder design
        logInButton.place(x=110, y=370, width=120, height=35)

        # Registration Button
        regButton = Button(frame, text="New User Registration", command=self.register_windows,
                           font=("times new roman", 14, "bold"),
                           bd=3, relief=RIDGE, fg="white", bg="blue", activebackground="blue",
                           activeforeground="white")  # Relief is boarder design
        regButton.place(x=15, y=420, width=300, height=35)

        # Down Image
        img5 = Image.open("employee.jpg")
        img5 = img5.resize((300, 200), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage01 = ImageTk.PhotoImage(img5)
        lblimg = Label(frame, image=self.photoImage01, bg="white", borderwidth=0)
        lblimg.place(x=20, y=475, width=300, height=180)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "User & Pass both are required")
        elif self.txtuser.get() == "abc" and self.txtpass.get() == "123":
            messagebox.showinfo("Successful", "Welcome to Employee Management")
        else:
            messagebox.showerror("Invalid Information")

    def register_windows(self):
        self.new_windows = Toplevel(self.root)
        self.app = Register(self.new_windows)



# ================== Register==================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry = ("1920*1080+0+0")

        #   ==========Variables==========
        self.var_fname = StringVar()
        self.var_contract = StringVar()
        self.var_sqqstn = StringVar()
        self.var_lname = StringVar()
        self.var_gmail = StringVar()
        self.var_sqans = StringVar()
        self.var_password = StringVar()
        self.var_passcnfrm = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file="reg.jpg")
        lbl_bg = Label(self.root, image=self.bg)  # for showing image on window
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)  # we used rel to make it suitable for every divice

        # Frame making
        frame = Frame(self.root, bg="white", bd=6, relief=RIDGE)
        frame.place(x=1100, y=190, width=620, height=650)

        # Register Label
        user_name = Label(frame, text="Register Here", font=("times new roman", 15, "bold"), fg="black", bg="orange")
        user_name.place(x=20, y=20)

        # =============Label and entry==============

        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=40, y=60)
        self.txtpass = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=85, height=30, width=215)

        # Contract
        contract = Label(frame, text="Contract No", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contract.place(x=40, y=125)
        self.txtpass = ttk.Entry(frame, textvariable=self.var_contract, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=150, height=30, width=215)

        # Select Security question
        sqqstn = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black",
                       bg="white", )
        sqqstn.place(x=40, y=190)
        self.comSecQstn = ttk.Combobox(frame, textvariable=self.var_sqqstn, font=("times new roman", 15, "bold"),
                                       state="readonly")
        self.comSecQstn["values"] = ("select", "Your birth place", "Your Best friend name", "Your favorite drink")
        self.comSecQstn.place(x=40, y=215, width="215", height="30")
        self.comSecQstn.current(0)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black",
                         bg="white")
        password.place(x=40, y=255)
        self.txtpass = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=280, height=30, width=215)

        # Right side row
        # Last Name
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname.place(x=350, y=60)
        self.lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 20, "bold"))
        self.lname.place(x=350, y=85, height=30, width=215)

        # Gmail
        gmail = Label(frame, text="Gmail", font=("times new roman", 15, "bold"), fg="black", bg="white")
        gmail.place(x=350, y=125)
        self.gmail = ttk.Entry(frame, textvariable=self.var_gmail, font=("times new roman", 20, "bold"))
        self.gmail.place(x=350, y=150, height=30, width=215)

        # Select Security ans
        sqans = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black",
                      bg="white")
        sqans.place(x=350, y=190)
        self.question = ttk.Entry(frame, textvariable=self.var_sqans, font=("times new roman", 20, "bold"))
        self.question.place(x=350, y=215, height=30, width=215)

        # Password
        passcnfrm = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black",
                          bg="white")
        passcnfrm.place(x=350, y=255)
        self.confirmPass = ttk.Entry(frame, textvariable=self.var_passcnfrm, font=("times new roman", 20, "bold"))
        self.confirmPass.place(x=350, y=280, height=30, width=215)

        # Check Button
        self.var_check = IntVar()
        chkBtn = Checkbutton(frame, variable=self.var_check, text="I agree the terms & conditions",
                             font=("times new roman", 15, "bold"),
                             fg="black", bg="orange", onvalue=1, offvalue=0)
        chkBtn.place(x=40, y=320, height=30, width=290)

        # ====================Button Image==================
        # reg button image
        btn1 = Image.open("registerBtn.png")
        btn1 = btn1.resize((300, 50), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage09 = ImageTk.PhotoImage(btn1)
        btn1 = Button(frame, image=self.photoImage09, command=self.register_data, borderwidth=0, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white")
        btn1.place(x=30, y=370, width=270)

        # Log In button image
        btn2 = Image.open("logBtn.jpg")
        btn2 = btn2.resize((300, 50), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage21 = ImageTk.PhotoImage(btn2)
        btn2 = Button(frame, image=self.photoImage21, borderwidth=0, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white")
        btn2.place(x=330, y=370, width=270)

        # Down Image
        img5 = Image.open("regDown.jpg")
        img5 = img5.resize((330, 200), Image.ANTIALIAS)  # ANTIALIAS will resize high resulation image
        self.photoImage01 = ImageTk.PhotoImage(img5)
        lblimg = Label(frame, image=self.photoImage01, bg="white", borderwidth=0)
        lblimg.place(x=140, y=450, width=340, height=160)

    # ================Function====================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_gmail.get() == "":
            messagebox.showerror("Error", "All information are required")
        elif self.var_password.get() != self.var_passcnfrm.get():
            messagebox.showerror("Offs!", "password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms")
        else:
            messagebox.showinfo("Success", "Welcome Sir")


if __name__ == "__main__":
    main()
