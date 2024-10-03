from tkinter import *


root.title('Текстовый редактор ongoing211')

txt_edit = Text(root)
txt_edit.grid()

btn_save = Button(root, text='Сохранить как...')
btn_save.place(y=200, x=50)

root.mainloop()
