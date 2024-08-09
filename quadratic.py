# Created by Aaryan Sachdeva 03/08/2024

import cmath, customtkinter
from tkinter import messagebox

root = customtkinter.CTk()
root.resizable(False, False)
width, height = 500, 565
root.geometry(f'{width}x{height}+{int((root.winfo_screenwidth() - width) / 2)}+{int((root.winfo_screenheight() - height) / 2)}')
root.title("Quadratic Solver")

def calculate():
	try:
		a = float(ae.get())
		b = float(be.get())
		c = float(ce.get())

		numerator = cmath.sqrt((b**2)-4*a*c)

		answer1 = -b + numerator
		answer2 = -b - numerator

		denominator = 2*a

		result1 = str(answer1/denominator).replace("+0j", "").replace("j", "i").replace("(", "").replace(")", "")
		result2 = str(answer2/denominator).replace("+0j", "").replace("j", "i").replace("(", "").replace(")", "")

		messagebox.showinfo("Answer(s)", f"{result1}, {result2}" if result1 != result2 else result1)
	
	except ZeroDivisionError:
		messagebox.showerror("Error!", "Make sure a ≠ 0")

	except:
		messagebox.showerror("Error!", "Make sure the inputs have only numerics.")

def clear():
	ae.delete(0, 'end')
	be.delete(0, 'end')
	ce.delete(0, 'end')

lbl = customtkinter.CTkLabel(root, text="ax² + bx + c = 0", text_font=("Helvetica", "42"))
lbl.pack(padx=20, pady=20)

ae = customtkinter.CTkEntry(root, text_font=("Helvetica", "32"))
ae.pack(padx=20, pady=20)

be = customtkinter.CTkEntry(root, text_font=("Helvetica", "32"))
be.pack(padx=20, pady=20)

ce = customtkinter.CTkEntry(root, text_font=("Helvetica", "32"))
ce.pack(padx=20, pady=20)

button = customtkinter.CTkButton(root, text="Calculate", text_font=("Helvetica", "25"), command=calculate)
button.pack(padx=20, pady=20)

clear = customtkinter.CTkButton(root, text="Clear", text_font=("Helvetica", "25"), command=clear)
clear.pack(padx=20, pady=20)

root.mainloop()