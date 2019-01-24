import tkinter
from tkinter import messagebox
import time


#menu instantiation
window = tkinter.Tk()

#hide menu window until login
window.withdraw()

#window title
window.title('GUI for Bank Reg')

#window size

window.resizable(0,0)

#window background

window.configure(background="cyan")



#####################################################################

#Login Form

#toplevel window for Login 
login_Form = tkinter.Toplevel()
login_Form.wm_geometry("190x220")
login_Form.resizable(0,0)
login_Form.configure(background="cyan")

#login header
label_main = tkinter.Label(login_Form, text="CLIBank", font=("Helvetica", 20), bg="gray1", fg="white")
label_main.pack(fill=tkinter.X)

#blank label space for separator
label_blank = tkinter.Label(login_Form, text=" ", bg="light slate gray")
label_blank.pack()

#welcome label
label_name = tkinter.Label(login_Form, text="Welcome to CLIBank", bg="light slate gray")
label_name.pack()

label_pin = tkinter.Label(login_Form, text="Please enter your PIN", bg="light slate gray")
label_pin.pack()

#pin text entry
Ent_pin = tkinter.Entry(login_Form, show="*")
Ent_pin.pack()
Ent_pin.focus()

#security counter variable
count = 3

#login function
def login_checker():

	var_pin = Ent_pin.get()
	password = 12345

	global count

	if var_pin.isdigit():

		var_pin = int(var_pin)

		if var_pin == password:
			messagebox.showinfo("Successful", "login Successful")
			login_Form.destroy()
			#show Menu window after login confirmation
			window.deiconify()
		else:
			messagebox.showerror("Error", "Incorrect password" +"\n Attempts left: " +str(count -1))
			Ent_pin.delete(0, tkinter.END)
			Ent_pin.focus()
			count -= 1
			print(count)


		if count == 0:
			messagebox.showerror("Error", " Incorrect password" + "\n Transaction canceled")
			login_Form.destroy()
			window.deiconify()

#Login button and Blank space separator
btn_login = tkinter.Button(login_Form, text="Login", command=login_checker)
btn_login.pack()

label_blank = tkinter.Label(login_Form, text="", bg="light slate gray")
label_blank.pack()

#######################################################################

#ATM Menu

#Menu Bar for ATM Menu

def about_app():
	print("App Name: CLIBank with Login Form and ATM Menu")
	print("App Description: ATM Login with 3 attempts security check and ATM Menu with deposit, withdrawal and statement printing options")
	print("Virtual ATM Pin ~ 12345 ~")
	print("Python Version 3.5")
	
	
	messagebox.showinfo("App Info", "App Name: CLIBank with Login Form and ATM Menu\n" + 
						"\nApp description:  ATM Login with 3 attempts security check and ATM Menu with deposit, withdrawal and statement printing options\n" + 
						"\nCLIBank Pin ~ 12345 ~\n" +
						"\nPython Version 3.5 " )
menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
myMenu.add_command(label="logout", command=login_Form)
menubar.add_cascade(label="App Info", menu=myMenu)

#display the menu bar
window.config(menu=menubar)


#ATM Visual Menu

#header labels and blank space separator
lbl_main = tkinter.Label(window, text="MENU", font=("Helvetica", 20), bg="gray1", fg="white")
lbl_main.pack(fill=tkinter.X)

lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

lbl_main = tkinter.Label(window, text="Choose Your Option", font=("Helvetica", 10), bg="light slate gray")
lbl_main.pack(fill=tkinter.X)

lbl_blank = tkinter.Label(window, text=" ", font=("Helvetica", 1), bg="light slate gray")
lbl_blank.pack()

#ATM Initial values and Buttons Menu
initial_balance = 1000

deposit_statement = ""

withdrawal_statement = ""

time_statement = ""

statement_list = []

#Checking balance function on pop up window
def check_balance():
	messagebox.showinfo("Account Balance", "Amount Available is: KES" + str(initial_balance))
	
btn_check = tkinter.Button(window, text="Check Balance", command=check_balance)
btn_check.pack(fill=tkinter.X)


#Deposit balance function on pop up window
def deposit_balance():

	toplevel = tkinter.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Make Cash Deposit", font=("Times", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tkinter.Label(toplevel, text="Enter Amount To Deposit: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tkinter.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_deposit():
		#get the figure entered by the user and saved as var_save variabe
		var_save = ent_top_name.get()


		global initial_balance
		global deposit_statement
		global statement_list
		
		if var_save.isdigit():
			var_save = int(var_save)
			initial_balance = var_save + initial_balance
			
			#deposit time and date
			time_deposit = time.strftime('%H:%M:%S')
			date_deposit = time.strftime('%Y - %m - %d')

			deposit_statement = "Deposit of KES" + str(var_save) + " made at " + str(time_deposit) + " on date: " + str(date_deposit)
		
			statement_list.append(deposit_statement)
		
			print(" ")
			print(deposit_statement)
			print(" ")
			print(initial_balance)
		
			toplevel.destroy()
			
		else:
			messagebox.showinfo("Error", "Invalid Entry")
			ent_top_name.delete(0, tkinter.END)
			ent_top_name.focus()
			
	btn_save = tkinter.Button(toplevel, text="Validate", command=save_deposit)
	btn_save.pack()
	
	lbl_blank = tkinter.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()
	
	btn_cancel = tkinter.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tkinter.X)
	
btn_deposit = tkinter.Button(window, text="Make Deposit", command=deposit_balance)
btn_deposit.pack(fill=tkinter.X)


#Draw balance function on pop up window
def draw_balance():
	toplevel = tkinter.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Cash Withdrawal", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tkinter.Label(toplevel, text="Enter Amount To Withdraw: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tkinter.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_draw():
		#attaching the amount drawn with the variable var_draw
		var_draw = ent_top_name.get()
		var_draw = int(var_draw)
		
		global initial_balance
		global withdrawal_statement
		global statement_list
		
		if initial_balance >= var_draw:
			initial_balance = initial_balance - var_draw
			
			#withdrawal time and date
			time_draw = time.strftime('%H:%M:%S')
			date_draw = time.strftime('%Y - %m - %d')

			withdrawal_statement = "Withdrawal of KES" + str(var_draw) + " made at " + str(time_draw) + " on date: " + str(date_draw)
			
			statement_list.append(withdrawal_statement)
		else:
			messagebox.showinfo("Error", "Insufficient Funds" + "\nMax Balance Allowed is : KES" + str(initial_balance))
			ent_top_name.delete(0, tkinter.END)
			draw_balance()
			ent_top_name.focus()
			
		print(initial_balance)
		
		toplevel.destroy()
		
	btn_save = tkinter.Button(toplevel, text="Validate", command=save_draw)
	btn_save.pack()
	
	lbl_blank = tkinter.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()

	btn_cancel = tkinter.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tkinter.X)
	
btn_draw = tkinter.Button(window, text="Withdraw Money", command=draw_balance)
btn_draw.pack(fill=tkinter.X)

#Print statement function on pop up window
def statement():
	
	global statement_list
	global time_statement
	global initial_balance
	
	time1 = time.strftime('%H:%M:%S')
	
	date1 = time.strftime('%Y-%m-%d')
	
	time_statement = "Statement printed at " + str(time1) + " on date: " + str(date1)
	blank_space = " "
	account_balance = "Your Account Balance is: KES" + str(initial_balance)
	
	statement_list.append(blank_space)
	statement_list.append(account_balance)
	statement_list.append(blank_space)
	statement_list.append(time_statement)
	statement_list.append(blank_space)

	
	toplevel = tkinter.Toplevel()
	toplevel.wm_geometry("800x300")
	toplevel.configure(background="beige")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="`Bank Statement Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack(fill=tkinter.X)
	
	lbl_top_name = tkinter.Label(toplevel, text="Bank Statement Summary: ")
	lbl_top_name.pack(side=tkinter.TOP)
	
	Scrolls = tkinter.Scrollbar(toplevel)
	Scrolls.pack(side=tkinter.RIGHT,fill=tkinter.Y)

	listboxPrintStatement = tkinter.Listbox(toplevel, height=12, yscrollcommand=Scrolls.set)
	listboxPrintStatement.pack(fill=tkinter.X)

	for item in statement_list:
		listboxPrintStatement.insert(tkinter.END, item)

	Scrolls.configure(command=listboxPrintStatement.yview)
	
	btn_close = tkinter.Button(toplevel, text="Close Statement", command=toplevel.destroy)
	btn_close.pack()
	
btn_print = tkinter.Button(window, text="Print Statement", command=statement)
btn_print.pack(fill=tkinter.X)


#blank space labels for separator and Cancel Button
lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

btn_cancel = tkinter.Button(window, text="Cancel Transaction", command=window.destroy)
btn_cancel.pack(fill=tkinter.X)


def new_feature():





    window.mainloop()











