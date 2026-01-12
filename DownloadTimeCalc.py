from tkinter import Tk, ttk, messagebox, StringVar

# Functions
def valueErrorMessageBox():
	messagebox.showerror("Error", "Input values should be integer or float. And file size can't be negative.")

def calcDownTime():
	fs = fileSizeEntry.get().strip()
	speed = speedEntry.get().strip()

	try:
		fs = float(eval(fs))
		speed = float(eval(speed))
	except (ValueError, NameError):
		return valueErrorMessageBox()

	if fs <= 0 or speed <= 0:
		return valueErrorMessageBox()

	s = fs / speed
	h = int(s // 3600)
	m = int((s % 3600) // 60)
	s = int(s % 60)
	resultStr.set(f'{h:02}:{m:02}:{s:02}')

# GUI
root = Tk()
root.title('Download Time Calculator')
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text='File Size (mb)').grid(column=0, row=0)
fileSizeEntry = ttk.Entry(frm)
fileSizeEntry.grid(column=0, row=1)

ttk.Label(frm, text='Download Speed (mb/s)').grid(column=0, row=2)
speedEntry = ttk.Entry(frm)
speedEntry.grid(column=0, row=3)

calcButton = ttk.Button(frm, text='Calculate', command=calcDownTime)
calcButton.grid(column=0, row=4)

ttk.Label(frm, text='Result').grid(column=0, row=5)
resultStr = StringVar()
resultEntry = ttk.Entry(frm, textvariable=resultStr, state='disabled')
resultEntry.grid(column=0, row=6)

root.mainloop()