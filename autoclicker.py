try:	
	from tkinter import *
	import pyautogui as pp
	import keyboard

	# Import Success

	root = Tk()

	mouse = StringVar()
	mouse.set("0")
	mousee = StringVar()
	mousee.set("0")

	def loc():
		for i in range(0,999999999):
			act.set('Activated [ Shift+Q [ Deactivate ] ]')
			root.update()
			locc.set('Press Ctrl+Q to Stop')
			if keyboard.is_pressed("ctrl+q"):
				dd = pp.position()
				locc.set("Find Mouse Location")
				mouse.set(f"{dd[0]}")
				mousee.set(f"{dd[1]}")
				break


	Label(text = "Welcome To AUTO CLICKER",font = "comicsansms 14 bold",bg = "black",fg = "white").pack()
	Label(text = "",font = "arial",bg = "white",fg = "white",borderwidth = 1,width = 45).pack()
	def ff():
		Label(text = "",bg = "black").pack()

	ff()
	locc = StringVar()
	locc.set("Find Mouse Location")
	Button(textvariable = locc,font = "comicsansms 14 bold",bg = "black",fg = "white",command = loc).pack(anchor = W)


	f1 = Frame(borderwidth = 10,bg = "black")
	f3 = Frame(borderwidth = 10,bg = "black")
	f4 = Frame(borderwidth = 10,bg = "black")

	Label(f1,text = "Mouse X: ",font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = LEFT)
	Entry(f1,textvariable = mouse,font = "comicsansms 14 bold",bg = "black",fg = "white",width = 7,justify = "right").pack(side = LEFT)
	Label(f1,text = "Mouse Y: ",font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = LEFT)
	Entry(f1,textvariable = mousee,font = "comicsansms 14 bold",bg = "black",fg = "white",width = 7,justify = "right").pack(side = LEFT)
	f1.pack(anchor = W)
	Label(text = "",font = "arial",bg = "white",fg = "white",borderwidth = 1,width = 45).pack()
	ff()

	interval = DoubleVar()
	interval.set(1)
	def plusb():
		interval.set((interval.get())+0.1)
	def subb():
		interval.set((interval.get())-0.1)
	Label(f3,text = "Wait After 1 Click: ",font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = LEFT)
	Entry(f3,textvariable = interval,font = "comicsansms 14 bold",bg = "black",fg = "white",width = 5,justify = "right").pack(side = LEFT)
	Label(f3,text = "  ",font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = LEFT)
	Button(f3,text = "+",font = "comicsansms 14 bold",bg = "black",fg = "white",command = plusb).pack(side = LEFT)
	Label(f3,text = "  ",font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = LEFT)
	Button(f3,text = "-",font = "comicsansms 14 bold",bg = "black",fg = "white",command = subb).pack(side = LEFT)
	f3.pack(anchor = W)

	Label(text = "",font = "arial",bg = "white",fg = "white",borderwidth = 1,width = 45).pack()
	ff()

	ff()
	act = StringVar()
	act.set("[ Shift+A ] Activate")
	Button(textvariable = act,font = "comicsansms 14 bold",bg = "black",fg = "white").pack(side = BOTTOM)

	root.config(bg = "black")

	import time
	for i in range(0,999999999):
		root.update()
		if keyboard.is_pressed('shift+a'):
			act.set('Activated [ Shift+Q [ Deactivate ] ]')
			for i in range(0,999999999999999999999):
				root.update()
				if keyboard.is_pressed('shift+q'):
					root.update()
					act.set("[ Shift+A ] Activate")
					break
				else:
					pp.click(x=eval((mouse.get())),y=eval((mousee.get())))
					pp.click(x=eval((mouse.get()))+1,y=eval((mousee.get())))
					time.sleep((interval.get()))
		act.set("[ Shift+A ] Activate")
	root.mainloop()
except:
	quit()