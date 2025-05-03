#git add .
#git commit -m "Your message"
#git pushprint("hello world")
from PIL import Image, ImageTk
import tkinter as tk
#   import customtkinter as ctk

root = tk.Tk()
root.title("tamagotchi game")
root.iconbitmap("C:/Users/julia/OneDrive - University of Florida/Comp Sim/tamagotchi/boba_bear_icon.ico")
root.geometry("500x400")
root.config(bg="#b4dc87") # Change background color to red using hex code

# function: button output
def out_button_1():
    rxn_1 = tk.Label(root, text="thank you for telling me .⋅˚ <3 ₊‧ 🜲 ‧₊˚",
                      font=("Cascadia Code", 10, "bold"), fg="#f2fcdc", bg="#b4dc87")
    rxn_1.pack()
    e.delete(0, tk.END)

#creating label widget
label_1 = tk.Label(root, text="⋆｡‧˚ʚ🍓ɞ˚‧｡⋆Hi Julianna!⋆｡‧˚ʚ🍓ɞ˚‧｡⋆", 
                   font=("Cascadia Code", 15, "bold"), fg="#f2fcdc", bg="#b4dc87")
image_1 = Image.open("C:/Users/julia/OneDrive - University of Florida/Comp Sim/tamagotchi/poc_body_1.png")
photo = ImageTk.PhotoImage(image_1.resize((67, 88)))
label_2 = tk.Label(root, image=photo, bg = "#b4dc87")
label_3 = tk.Label(root, text="What are you worried about?", 
                   font=("Cascadia Code",   10, "bold" ), fg="#f2fcdc", bg="#b4dc87")

#creating buttons
button_1 = tk.Button(root, text="Click Me!", font =("Cascadia Code", 10, "bold"), borderwidth = 3, 
                     padx= 20, command = out_button_1, activebackground ="#b4dc87", activeforeground= "#e9f7cb", fg = "#f2fcdc", bg="#b4dc87")  

#initating input box
e = tk.Entry(root, width = 50, font =("Cascadia Code", 10, "bold"), borderwidth = 3, bg="#ffd0de", fg = "white")
e.config(insertbackground="white")

#adding labels to screen
label_1.pack(pady=20)
label_2.pack(pady=5)
label_3.pack(pady=20)
#label_2.grid(row=1, column=5)

#adding input box to screen
e.pack(pady=20)

#adding buttons to screen
button_1.pack(pady=10)

#wrap text test






#end
root.mainloop()



