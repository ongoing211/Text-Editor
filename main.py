from tkinter import *


root.title('Текстовый редактор ongoing211')

txt_edit = Text(root)
txt_edit.grid()

btn_open = Button(root, text='Открыть файл...')
btn_save = Button(root, text='Сохранить как...')
btn_open.place(x=50, y=150)
btn_save.place(x=50, y=200)

root.mainloop()
