import tkinter as tk

window = tk.Tk()

temp_img = tk.PhotoImage(file='hack.png')
zx = int(400 / temp_img.width())
zy = int(300 / temp_img.height())
background_img = temp_img.zoom(zx, zy)

can = tk.Canvas(window, width=400, height=300)
can.pack()

can.create_image(200, 150, image=background_img)

window.mainloop()

