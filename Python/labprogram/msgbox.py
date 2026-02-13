from tkinter import *
from tkinter import messagebox as msg
window=Tk()
window.geometry('800x800')
msg.showerror("Error Box","Oh nooo")
msg.showwarning("Warning box","time over")
msg.askquestion("Confirm Dialog Box")
msg.askokcancel("Redirect to google.com")
msg.askyesno("Application proceeds","go to page")
window.mainloop()

