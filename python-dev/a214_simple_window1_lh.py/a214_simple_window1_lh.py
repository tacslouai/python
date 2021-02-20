##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_button():
    frame_auth.tkraise()
    user_pass = ent_pass.get()
    lbl_pass = tk.Label(frame_auth, text=user_pass, font=lbl_font)
    lbl_pass.pack(pady=10)

# main window
root = tk.Tk()

root.eval('tk::PlaceWindow . center')

root.wm_geometry("600x600")
root.title("Authorization")

# LOGIN FRAME
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_font = 'Courier'

lbl_username = tk.Label(frame_login, text='Username:', font = lbl_font)
lbl_pass = tk.Label(frame_login, text='Password:', font = lbl_font)

ent_username = tk.Entry(frame_login, bd=3)
ent_pass = tk.Entry(frame_login, bd=3, show="*")

btn_login = tk.Button(frame_login, text = "Login", command = test_button)

lbl_username.pack()
ent_username.pack(pady=5, padx=10)

lbl_pass.pack()
ent_pass.pack(pady=5, padx = 10)

btn_login.pack(pady=10)

# AUTH FRAME
frame_auth = tk.Frame()
frame_auth.grid(row=0, column=0, sticky="news")

boxes = []
num_boxes = 4
for i in range (0, num_boxes):
    temp_box = tk.Frame(root)
    boxes.append(temp_box)


boxes[0].grid(row=0, column=0)
boxes[0].config(bg='blue', height=300, width=400)

boxes[1].grid(row=0, column=1)
boxes[1].config(bg='green1', height=300, width=200)

boxes[2].grid(row=1, column=0)
boxes[2].config(bg='red', height=300, width=400)

boxes[3].grid(row=1, column=1)
boxes[3].config(bg='yellow', height=300, width=200)

frame_login.tkraise()
boxes[0].tkraise()
root.mainloop()
