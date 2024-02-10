import tkinter
import customtkinter
import db_auth

#create the main frame 
root = customtkinter.CTk()
root.geometry("500x400")
root.title("PIsec camera manager")

#create the default settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#creating label
label = customtkinter.CTkLabel(master=root, text="Login System")
label.pack(padx=10, pady=12, side="top")


#creating the frame 
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=60, fill="both", expand=True)

#creating the entry fields
entry_usr = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Username")
entry_pasw = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Password", show='*')
button = customtkinter.CTkButton(master=frame, text="Login", command=db_auth.usr_login)

#placing the widgets
button.pack(padx=10, pady=12, side ="bottom")
entry_usr.pack(padx=10, pady=12, side="top")
entry_pasw.pack(padx=10, pady=12, side="top")


#run the application
root.mainloop()
