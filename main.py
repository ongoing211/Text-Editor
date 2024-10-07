from tkinter import *


root = Tk("TextEditor")
root.title('Текстовый редактор ongoing211')

frame_btn = Frame(master=root, width=190, bg='grey')
frame_btn.pack(fill=Y, side=LEFT)


btn_open = Button(frame_btn, text='Открыть файл...')
btn_save = Button(frame_btn, text='Сохранить как...')
btn_open.place(x=50, y=150)
btn_save.place(x=50, y=200)

root.mainloop()
