import tkinter
import customtkinter
import db_input as DBi 

#create the root window
root = customtkinter.CTk()
root.geometry("500x600")
root.title("PIsec camera manager")

#create the default configurations
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#create the label
label = customtkinter.CTkLabel(master=root, text="Create account")
label.pack(padx=10, pady=12)


#create the frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=60, fill="both", expand=True)

#create the entry fields
entry_usr = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Username")
entry_pasw = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Password", show='*')
entry_pasw_confirm = customtkinter.CTkEntry(master=frame, placeholder_text="Confirm Password", show='*')
entry_email = customtkinter.CTkEntry(master=frame, placeholder_text="Enter email")

#place the entry fields
entry_usr.pack(padx=10, pady=12)
entry_pasw.pack(padx=10, pady=12)
entry_pasw_confirm.pack(padx=10, pady=12)
entry_email.pack(padx=10, pady=12)

#create a button
button_ca = customtkinter.CTkButton(master=frame, text="Create", command=DBi.create_Usr)
button_ca.pack(padx=10, pady=12)

#run the application
root.mainloop()
