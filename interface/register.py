import tkinter
from tkinter import *
import customtkinter

from Certif.CA.Cert import *
from Certif.Client.cerf_req import *
from Ldap.Server import ldapserver

Windowreg = customtkinter.CTk()
Windowreg.title("Register")
Windowreg.resizable(width=False,
				height=False)
Windowreg.configure(width=500,
				height=500)
pls = customtkinter.CTkLabel(Windowreg,
						text="Create an Account",
						font=("Arial",20,"bold"))
pls.place(relheight=0.15,
					relx=0.5,
					rely=0.1,
				    anchor="center")

	### Pseudo ####
		# create a Label
Windowreg.labelPseudo = customtkinter.CTkLabel(Windowreg,
							text="Login : ",
							   justify=CENTER
							   )

Windowreg.labelPseudo.place(relheight=0.1,
							relx=0.1,
							rely=0.2)

		# create a entry box for
		# tying the message
Windowreg.entryPseudo = customtkinter.CTkEntry(Windowreg)

Windowreg.entryPseudo.place(relwidth=0.4,
							relheight=0.08,
							relx=0.3,
							rely=0.2)

	### firstName ####
		# create a Label
Windowreg.labelFirstName = customtkinter.CTkLabel(Windowreg,
							text="firstName : ",
							   justify=CENTER
							   )

Windowreg.labelFirstName.place(relheight=0.1,
							relx=0.1,
							rely=0.3)

		# create a entry box for
		# tying the message
Windowreg.entryFirstName = customtkinter.CTkEntry(Windowreg)

Windowreg.entryFirstName.place(relwidth=0.4,
							relheight=0.08,
							relx=0.3,
							rely=0.3)

	### lastName ####
		# create a Label
Windowreg.labelLastName = customtkinter.CTkLabel(Windowreg,
							text="lastName : ",
							   justify=CENTER
							   )

Windowreg.labelLastName.place(relheight=0.1,
							relx=0.1,
							rely=0.4)

		# create a entry box for
		# tying the message
Windowreg.entryLastName = customtkinter.CTkEntry(Windowreg)

Windowreg.entryLastName.place(relwidth=0.4,
							relheight=0.08,
							relx=0.3,
							rely=0.4)

	### NumCarte ####
		# create a Label
Windowreg.labelNumCarte = customtkinter.CTkLabel(Windowreg,
							text="Card Number : ",
							   justify=CENTER
							   )

Windowreg.labelNumCarte.place(relheight=0.1,
							relx=0.1,
							rely=0.5)

		# create a entry box for
		# tying the message
Windowreg.entryNumCarte = customtkinter.CTkEntry(Windowreg)

Windowreg.entryNumCarte.place(relwidth=0.4,
							relheight=0.08,
							relx=0.3,
							rely=0.5)

		### Password ####
		# create a Label
Windowreg.labelPwd = customtkinter.CTkLabel(Windowreg,
							   text="Password : ",
							   justify=CENTER
							   )

Windowreg.labelPwd.place(relheight=0.1,
							 relx=0.1,
							 rely=0.6)

		# create a entry box for
		# tying the message
Windowreg.entryPwd = customtkinter.CTkEntry(Windowreg,
							  show='*')

Windowreg.entryPwd.place(relwidth=0.4,
							 relheight=0.08,
							 relx=0.3,
							 rely=0.6)

def redirLog():
	Windowreg.withdraw()
	import interface.login

def register():
	user = {
		'username': Windowreg.entryPseudo.get(),
		'password': Windowreg.entryPwd.get(),
		'numCarte': Windowreg.entryNumCarte.get(),  # student card
		'firstname': Windowreg.entryFirstName.get(),
		'lastname': Windowreg.entryLastName.get()
	}
	# TODO : add port for user
	# TODO : get list of Users
	# Register user with LDAP Service
	ldapserver.register(user)
	# Generate a certificate request for the CA
	gen_cert_req(user["username"],user["firstname"])
	# Certificate creation by the CA :
	create_cert("/home/hime_chan/PycharmProjects/SecureChat/Certif/Client/requests/guest1_req.csr","guest1")




		# create a Continue Button
		# along with action
Windowreg.go = customtkinter.CTkButton(Windowreg,
						text="REGISTER",
						command= register)

Windowreg.go.place(relx=0.35,
					rely=0.75)

Windowreg.go = customtkinter.CTkButton(Windowreg,
										  text="go back to login",
										  command=redirLog)

Windowreg.go.place(relx=0.35,
					  rely=0.85)

Windowreg.mainloop()