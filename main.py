from tkinter import *


root = Tk("TextEditor")
root.title('Текстовый редактор ongoing211')

root.rowconfigure(0, minsize=1000, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

frame_btn = Frame(master=root, width=190, bg='grey')
txt_edit = Frame(master=root)
frame_btn.pack(fill=Y, side=LEFT)


btn_open = Button(frame_btn, text='Открыть файл...')
btn_save = Button(frame_btn, text='Сохранить как...')
btn_open.place(x=50, y=150)
btn_save.place(x=50, y=200)

def open_file():
    file_path = fd.askopenfilename(filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_path:
        return

root.mainloop()
