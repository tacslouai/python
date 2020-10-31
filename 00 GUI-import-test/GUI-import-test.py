#################################################################################
# This program imports various python modules to ensure you are ready for CSP
# Written by George, feel free to distribute.
################################################################################
import tkinter as tk
success_list=[]
fail_list=[]


def test_imports():
  
  imports =["turtle", "random", 'PIL', 'godirect', 'logging', 'matplotlib', 'pandas', "this_should_fail"]

  for x in imports:
      try:
          success_list.append(__import__(x))
          print ("Successfully imported ", x, '.')

      except ImportError:
          fail_list.append(x)
          print ("Error importing ", x, '.')
  show_results()

def show_results():
  frame_results.tkraise()
  username= ent_username.get()
  lbl_thanks.config(text='Thanks for testing your imports '+ username)
  worked = len(success_list)
  lbl_worked.config(text=str(worked) + ' out of 7 modules imported successfully.')
  lbl_failed.config(text=str(7-worked) + ' imports failed.')
  lbl_failed_imports.config(text='Failed imports: ' + str(fail_list))
  print(opsys.get()) # prints result of radio button
  import_directions(opsys.get())
  

def import_directions(op):
  fail_list.pop()
  imp_needed = ""
  if len(fail_list) >=1:
    if op !=2: # Mac was not selected so show Windows imports
      imp_needed += "Windows import commands needed: \n"
      for imp in fail_list:
        imp_needed += ("pip install " + imp)
        if imp == "godirect":
          imp_needed += "[USB,BLE]"
        imp_needed += ("\n")
    imp_needed += "\n"
    if op !=1: # Windows was not selected so show Mac imports
      imp_needed += "Mac import commands needed: \n"
      for imp in fail_list:
        imp_needed += ("pip3 install " + imp)
        if imp == "godirect":
          imp_needed += "[usb,ble]"
        imp_needed += ("\n") 
  else:
    imp_needed += "No imports needed!"
  lbl_imports_needed.config(text=imp_needed)


def enter_hit(event):  # Added so test runs on enter key or button click
    test_imports()
#GUI
# main window
root = tk.Tk()
root.wm_geometry("400x400")
root.title("Import Test")
root.bind('<Return>', enter_hit) # Added so test runs on enter key or button click
opsys = tk.IntVar()

# create empty frame
frame_name = tk.Frame(root)
frame_name.grid(row=0, column=0, sticky='news')

frame_results = tk.Frame(root)
frame_results.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_name,text='Name:').pack(pady=5)

ent_username = tk.Entry(frame_name, bd=3)
ent_username.pack(pady=5)

btn_win = tk.Radiobutton(frame_name, text="Windows",padx = 20, variable=opsys, indicatoron = 0, value=1)
btn_win.pack(padx=175)
btn_mac = tk.Radiobutton(frame_name, text="Mac", padx = 20, variable=opsys, indicatoron = 0, value=2)
btn_mac.pack(padx=175)

btn_test_imp = tk.Button(frame_name, text='Test imports', command=test_imports)
btn_test_imp.pack(padx=175, pady=20)

lbl_thanks = tk.Label(frame_results,text='')
lbl_thanks.pack(pady=5)

lbl_worked = tk.Label(frame_results,text='')
lbl_worked.pack(pady=5)

lbl_failed = tk.Label(frame_results,text='')
lbl_failed.pack(pady=5)
lbl_failed_imports = tk.Label(frame_results,text='')
lbl_failed_imports.pack(pady=5)

lbl_imports_needed = tk.Label(frame_results,text='')
lbl_imports_needed.pack(pady=5)

frame_name.tkraise()
root.mainloop()