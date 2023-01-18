# import all the required modules
import socket
import threading
import tkinter
from tkinter import *
import customtkinter

from Certif.CA.Cert import *
from Ldap.Server import ldapserver


# import all functions /
# everything from chat.py filech
#from chat import *

## TODO : Sockets
"""
PORT = 5050
SERVER = "192.168.0.103"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
client.connect(ADDRESS)
"""

def redirReg():
	Window.withdraw()
	import interface.register

def create_toplevel(title,msg):
	window = customtkinter.CTkToplevel()
	window.title(title)
	window.geometry("400x100")

	# create label on CTkToplevel window
	label = customtkinter.CTkLabel(window, text=msg)
	label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


Window = customtkinter.CTk()
Window.title("Login")
Window.resizable(width=False,
							height=False)
Window.configure(width=500,
							height=400)
pls = customtkinter.CTkLabel(Window,
						text="Welcome To SecureChat",
										  font=("Arial",20,"bold"))
pls.place(relheight=0.15,
					relx=0.5,
					rely=0.2,
				    anchor="center")

	### Pseudo ####
		# create a Label
Window.labelName = customtkinter.CTkLabel(Window,
							text="Login : ",
							   justify=CENTER
							   )

Window.labelName.place(relheight=0.1,
							relx=0.1,
							rely=0.3)

		# create a entry box for
		# tying the message
Window.entryName = customtkinter.CTkEntry(Window)

Window.entryName.place(relwidth=0.4,
							relheight=0.08,
							relx=0.3,
							rely=0.3)

		# set the focus of the cursor
Window.entryName.focus()

		### Password ####
		# create a Label
Window.labelPwd = customtkinter.CTkLabel(Window,
							   text="Password : ",
							   justify=CENTER
							   )

Window.labelPwd.place(relheight=0.1,
							 relx=0.1,
							 rely=0.45)

		# create a entry box for
		# tying the message
Window.entryPwd = customtkinter.CTkEntry(Window,
							  show='*')

Window.entryPwd.place(relwidth=0.4,
							 relheight=0.08,
							 relx=0.3,
							 rely=0.45)


def connect():
	msg = ldapserver.login(Window.entryName.get(),Window.entryPwd.get())
	if (msg == "Authentification succeeded"):
		msgCert = verif_cert(Window.entryName.get())
		print(msgCert)
		if (msgCert == "The certificate is authentic"):
			# TODO : redirection + Get list of users for the connected one
			print("ff")
		else :
			create_toplevel("HACKER !!!!",msgCert)
	else :
		create_toplevel("Error",msg)
		#self.login.destroy()
		#self.layout(name)

		# the thread to receive messages
		#rcv = threading.Thread(target=self.receive)
		#rcv.start()


		# create a Continue Button
		# along with action
Window.go = customtkinter.CTkButton(Window,
						text="CONNECT",
						command= connect)

Window.go.place(relx=0.35,
					rely=0.65)

Window.go = customtkinter.CTkButton(Window,
										  text="register",
										  command=redirReg)

Window.go.place(relx=0.35,
					  rely=0.75)

Window.mainloop()



"""
# The main layout of the chat
	def layout(self, name):

		self.name = name
		# to show chat window
		self.Window.deiconify()
		self.Window.title("CHATROOM")
		self.Window.resizable(width=False,
							height=False)
		self.Window.configure(width=470,
							height=550,
							bg="#17202A")
		self.labelHead = Label(self.Window,
							bg="#17202A",
							fg="#EAECEE",
							text=self.name,
							font="Helvetica 13 bold",
							pady=5)

		self.labelHead.place(relwidth=1)
		self.line = Label(self.Window,
						width=450,
						bg="#ABB2B9")

		self.line.place(relwidth=1,
						rely=0.07,
						relheight=0.012)

		self.textCons = Text(self.Window,
							width=20,
							height=2,
							bg="#17202A",
							fg="#EAECEE",
							font="Helvetica 14",
							padx=5,
							pady=5)

		self.textCons.place(relheight=0.745,
							relwidth=1,
							rely=0.08)

		self.labelBottom = Label(self.Window,
								bg="#ABB2B9",
								height=80)

		self.labelBottom.place(relwidth=1,
							rely=0.825)

		self.entryMsg = Entry(self.labelBottom,
							bg="#2C3E50",
							fg="#EAECEE",
							font="Helvetica 13")

		# place the given widget
		# into the gui window
		self.entryMsg.place(relwidth=0.74,
							relheight=0.06,
							rely=0.008,
							relx=0.011)

		self.entryMsg.focus()

		# create a Send Button
		self.buttonMsg = Button(self.labelBottom,
								text="Send",
								font="Helvetica 10 bold",
								width=20,
								bg="#ABB2B9",
								command=lambda: self.sendButton(self.entryMsg.get()))

		self.buttonMsg.place(relx=0.77,
							rely=0.008,
							relheight=0.06,
							relwidth=0.22)

		self.textCons.config(cursor="arrow")

		# create a scroll bar
		scrollbar = Scrollbar(self.textCons)

		# place the scroll bar
		# into the gui window
		scrollbar.place(relheight=1,
						relx=0.974)

		scrollbar.config(command=self.textCons.yview)

		self.textCons.config(state=DISABLED)

	# function to basically start the thread for sending messages
	def sendButton(self, msg):
		self.textCons.config(state=DISABLED)
		self.msg = msg
		self.entryMsg.delete(0, END)
		snd = threading.Thread(target=self.sendMessage)
		snd.start()

	# function to receive messages
	def receive(self):
		while True:
			try:
				message = client.recv(1024).decode(FORMAT)

				# if the messages from the server is NAME send the client's name
				if message == 'NAME':
					client.send(self.name.encode(FORMAT))
				else:
					# insert messages to text box
					self.textCons.config(state=NORMAL)
					self.textCons.insert(END,
										message+"\n\n")

					self.textCons.config(state=DISABLED)
					self.textCons.see(END)
			except:
				# an error will be printed on the command line or console if there's an error
				print("An error occurred!")
				client.close()
				break

	# function to send messages
	def sendMessage(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode(FORMAT))
			break
"""

