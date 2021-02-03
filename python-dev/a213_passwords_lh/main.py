# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircteownlo app
my_auth = mfg.MultiFactorAuth()
username = "neo"
password = "02"
my_auth.set_authorization(username, password)
# set the users authentication information
question = "Where do you live?"
answer = "spain without the s"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
