from tkinter import *

welcome = "American Council of the Blind"
title = welcome.title()
print(title)

root = Tk()

user = Button(root, text = 'User Page', bd = '10', command = root.destroy)
user.pack(side = 'left')
volunteer = Button(root, text = 'Volunteer Page', bd = '10', command = root.destroy)
volunteer.pack(side = 'center')
admin = Button(root, text = 'Admin Page', bd = '10', command = root.destroy)
admin.pack(side = 'right')

root.mainloop()

