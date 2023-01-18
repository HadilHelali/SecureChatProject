import socket
import threading
import tkinter as tk
import cons
import customtkinter
import customtkinter as ctk

from Certif.CA.Cert import verif_cert, create_cert
from Certif.Client.cerf_req import gen_cert_req
from Ldap.Server import ldapserver
from RSA.rsa_fun import *

IP = "localhost"
PORT_R=1234
PORT_S=50036


class App2(ctk.CTk):

    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        # Create a container frame to hold all pages
        container = ctk.CTkFrame(self)
        # TODO : set the size in the beginning
        container.configure(width=600,
							height=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Register):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def show_chatroom_param(self ,container, param , login):
        '''Show a frame for the given page name'''
        chatroom = ChatRoom(parent=container, controller=self ,param=param , login=login)
        self.frames[ChatRoom] = chatroom
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        chatroom.grid(row=0, column=0, sticky="nsew")
        chatroom.tkraise()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pls = customtkinter.CTkLabel(self,
                                     text="Welcome To SecureChat",
                                     font=("Arial", 20, "bold"))
        pls.place(relheight=0.15,
                  relx=0.5,
                  rely=0.2,
                  anchor="center")

        ### Pseudo ####
        # create a Label
        labelName = customtkinter.CTkLabel(self,text="Login : ",justify=tk.CENTER)

        labelName.place(relheight=0.1,
                               relx=0.1,
                               rely=0.3)

        # create a entry box for
        # tying the message
        entryName = customtkinter.CTkEntry(self)

        entryName.place(relwidth=0.4,
                               relheight=0.08,
                               relx=0.3,
                               rely=0.3)

        # set the focus of the cursor
        entryName.focus()

        ### Password ####
        # create a Label
        labelPwd = customtkinter.CTkLabel(self,text="Password : ",justify=tk.CENTER)
        labelPwd.place(relheight=0.1,
                              relx=0.1,
                              rely=0.45)

        # create a entry box for
        # tying the message
        entryPwd = customtkinter.CTkEntry(self,show='*')

        entryPwd.place(relwidth=0.4,
                              relheight=0.08,
                              relx=0.3,
                              rely=0.45)

        def create_toplevel(title, msg):
            window = customtkinter.CTkToplevel()
            window.title(title)
            window.geometry("400x100")

            # create label on CTkToplevel window
            label = customtkinter.CTkLabel(window, text=msg)
            label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        def connect():
            msg = ldapserver.login(entryName.get(),entryPwd.get())
            if (msg == "Authentification succeeded"):
                msgCert = verif_cert(entryName.get())
                print(msgCert)
                if (msgCert == "The certificate is authentic"):
                    # get list of Users :
                    list = ldapserver.getallUsers()
                    list.remove(entryName.get())
                    currentLogin = entryName.get()
                    # Redirect to chatRoom :
                    controller.show_chatroom_param(container=parent, param=list , login=currentLogin)
                else:
                    create_toplevel("HACKER !!!!", msgCert)
            else:
                create_toplevel("Error", msg)


        go = customtkinter.CTkButton(self,text="CONNECT",command=connect)
        go.place(relx=0.35,rely=0.65)
        go = customtkinter.CTkButton(self,text="register",command=lambda: controller.show_frame("Register"))
        go.place(relx=0.35,rely=0.75)

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pls = customtkinter.CTkLabel(self,text="Create an Account",font=("Arial", 20, "bold"))
        pls.place(relheight=0.15,relx=0.5,rely=0.1,anchor="center")

        ### Pseudo ####
        # create a Label
        labelPseudo = customtkinter.CTkLabel(self,text="Login : ",justify=ctk.CENTER)

        labelPseudo.place(relheight=0.1,relx=0.1,rely=0.2)

        # create a entry box for
        # tying the message
        entryPseudo = customtkinter.CTkEntry(self)

        entryPseudo.place(relwidth=0.4,relheight=0.08,relx=0.3,rely=0.2)

        ### firstName ####
        # create a Label
        labelFirstName = customtkinter.CTkLabel(self,text="firstName : ",justify=ctk.CENTER)

        labelFirstName.place(relheight=0.1,relx=0.1,rely=0.3)

        # create a entry box for
        # tying the message
        entryFirstName = customtkinter.CTkEntry(self)

        entryFirstName.place(relwidth=0.4,relheight=0.08,relx=0.3,rely=0.3)

        ### lastName ####
        # create a Label
        labelLastName = customtkinter.CTkLabel(self,text="lastName : ",justify=ctk.CENTER)

        labelLastName.place(relheight=0.1,relx=0.1,rely=0.4)

        # create a entry box for
        # tying the message
        entryLastName = customtkinter.CTkEntry(self)

        entryLastName.place(relwidth=0.4,relheight=0.08,relx=0.3,rely=0.4)

        ### NumCarte ####
        # create a Label
        labelNumCarte = customtkinter.CTkLabel(self,text="Card Number : ",justify=ctk.CENTER)

        labelNumCarte.place(relheight=0.1,relx=0.1,rely=0.5)

        # create a entry box for
        # tying the message
        entryNumCarte = customtkinter.CTkEntry(self)

        entryNumCarte.place(relwidth=0.4,relheight=0.08,relx=0.3,rely=0.5)

        ### Password ####
        # create a Label
        labelPwd = customtkinter.CTkLabel(self,text="Password : ",justify=ctk.CENTER)

        labelPwd.place(relheight=0.1,relx=0.1,rely=0.6)

        # create a entry box for
        # tying the message
        entryPwd = customtkinter.CTkEntry(self,show='*')

        entryPwd.place(relwidth=0.4,relheight=0.08,relx=0.3,rely=0.6)

        def register():
            user = {
                'username': entryPseudo.get(),
                'password': entryPwd.get(),
                'numCarte': entryNumCarte.get(),  # student card
                'firstname': entryFirstName.get(),
                'lastname': entryLastName.get()
            }
            # TODO : add port for user
            # Register user with LDAP Service
            ldapserver.register(user)
            # Generate a certificate request for the CA
            gen_cert_req(user["username"], user["firstname"])
            # Certificate creation by the CA :
            create_cert(user["username"])
            # Generate private and public keys :
            generateKeys(user["username"])
            # get list of Users :
            list = ldapserver.getallUsers()
            list.remove(user["username"])
            currentLogin = user["username"]
            # Redirect to chatRoom :
            controller.show_chatroom_param(container=parent, param=list, login=currentLogin)

        # create a Continue Button
        # along with action
        go = customtkinter.CTkButton(self,text="REGISTER",command=register)
        go.place(relx=0.35,rely=0.75)
        go = customtkinter.CTkButton(self,text="go back to login",command=lambda: controller.show_frame("Login"))

        go.place(relx=0.35,rely=0.85)

class ChatRoom(tk.Frame):
    def __init__(self ,parent , controller , param , login):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.list = param
        # chat mate :
        self.sendTo = ""
        self.sendToIndex = 0
        self.current = login
        # messages :
        self.MsgToSend = ""
        self.sendOk = False

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # User name :
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=self.current,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)


        # chatroom components :
        self.Btns = []
        self.Frames = []
        self.chatbox = []
        self.send_box = []
        self.send_button = []

        for i in range(len(self.list)):
            self.Btns.append("btn"+str(i))
            self.Frames.append("frame" + str(i))
            self.chatbox.append("chatbox" + str(i))
            self.send_box.append("send_box" + str(i))
            self.send_button.append("send_button" + str(i))

        for l in range(len(self.list)) :
            # navigation :
            self.Btns[l] = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text=self.list[l],
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), anchor="w",
                                                   command=lambda l=l: self.btn_button_event(l)
                                                   )
            self.Btns[l].grid(row=l + 1, column=0, sticky="ew")
            # create home frame
            self.Frames[l] = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.Frames[l].grid_columnconfigure(0, weight=1)
            # the inside of the chatbox :

            # chatbox (where we'll have the conversation) :
            self.chatbox[l] = customtkinter.CTkTextbox(self.Frames[l])
            self.chatbox[l].grid(row=1, rowspan=5, column=1, columnspan=3, padx=(5, 10), pady=(20, 10), sticky="nsew")
            self.chatbox[l].insert(tk.END, "new text to insert")  # insert at line 0 character 0
            # input :
            # create main entry and button
            self.send_box[l] = customtkinter.CTkEntry(self.Frames[l], placeholder_text="type your message")
            self.send_box[l].grid(row=10, column=1, columnspan=1, padx=(5, 0), pady=(20, 20), sticky="nsew")

            # send button :
            self.send_button[l] = customtkinter.CTkButton(master=self.Frames[l], text="send" ,fg_color="transparent", border_width=2,
                                                         text_color=("gray10", "#DCE4EE"),
                                                          command= self.onSubmit )
            self.send_button[l].grid(row=10, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        x1 = threading.Thread(target=self.sending)
        x2 = threading.Thread(target=self.receiving)
        x1.start()
        x2.start()

    def onSubmit(self):
        self.MsgToSend = self.send_box[self.sendToIndex].get()
        # print in chatbox :
        Msg = "Me >> "+self.MsgToSend
        self.chatbox[self.sendToIndex].insert(tk.END, Msg)
        self.sendOk = True


    def sending(self): # behaves like a client
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((IP,PORT_S))
        while True :
            #msg = input("Enter the message you want to send")
            if self.sendOk == True :
                encrytMsg = encrypt(self.MsgToSend, self.pubKey)
                s.send(encrytMsg)
                self.sendOk = False


    def receiving(self): # behaves like a server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((IP,PORT_R))
        while True :
            encrytedMsg = s.recvfrom(PORT_S)
            Msg = decrypt(encrytedMsg, self.myKey)
            addedMsg = "from ",self.sendTo,">> ",Msg
            # print in chatbox :
            self.chatbox[self.sendToIndex].insert(tk.END, addedMsg )


    def select_frame_by_name(self, p):
        # set button color for selected button
        print(p)
        # chat mate :
        self.sendToIndex = p
        self.sendTo = self.list[p]
        self.myKey, self.pubKey = getKeys(self.current, self.sendTo)
        for j in range(len(self.list)) :
            self.Btns[j].configure(fg_color=("gray75", "gray25") if j == p else "transparent")
        # show selected frame
            if j == p :
                self.Frames[p].grid(row=0, column=1, sticky="nsew")
            else:
                self.Frames[p].grid_forget()



    def btn_button_event(self,q):
        self.select_frame_by_name(q)

app2 = App2()
app2.mainloop()